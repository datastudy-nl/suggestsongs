import database as db
from dto.track import Track

def get_top_rated_tracks(user_id):
    query = """
        SELECT t.id, t.name, t.artist, t.album, t.duration_ms, t.popularity, t.explicit, t.url, tr.rating
        FROM track_rating tr
        JOIN tracks t ON tr.track_id = t.id
        WHERE tr.user_id = %s
        AND tr.rating IS NOT NULL
        ORDER BY tr.rating DESC
        LIMIT 50
    """
    with db.get_connection() as conn:
        with conn.cursor(dictionary=True) as cursor:
            tracks = []
            cursor.execute(query, (user_id,))
            for track in cursor.fetchall(): tracks.append(Track(**track))
            return tracks

def get_random_tracks():
    query = """
        SELECT id, name, artist, album, duration_ms, popularity, explicit, url
        FROM tracks
        ORDER BY RAND()
        LIMIT 5
    """
    with db.get_connection() as conn:
        with conn.cursor(dictionary=True) as cursor:
            tracks = []
            cursor.execute(query)
            for track in cursor.fetchall(): tracks.append(Track(**track))
                

def save_tracks(tracks):
    with db.get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.executemany('''
                INSERT INTO tracks (id, name, artist, album, duration_ms, popularity, explicit, url) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
                ON DUPLICATE KEY UPDATE
                name = VALUES(name),
                artist = VALUES(artist),
                album = VALUES(album),
                duration_ms = VALUES(duration_ms),
                popularity = VALUES(popularity),
                explicit = VALUES(explicit),
                url = VALUES(url)
                ''',
                [(track.id, track.name, track.artist, track.album, track.duration_ms, track.popularity, track.explicit, track.url) for track in tracks])
        conn.commit()

def add_unrated_tracks(user_id, tracks):
    with db.get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.executemany('''
                INSERT IGNORE INTO track_rating (user_id, track_id, rating)
                VALUES (%s, %s, NULL)
                ''',
                [(user_id, track.id) for track in tracks])
        conn.commit()


def get_unrated_tracks(user_id):
    query = """
        SELECT t.id, t.name, t.artist, t.album, t.duration_ms, t.popularity, t.explicit, t.url
        FROM track_rating tr
        JOIN tracks t ON tr.track_id = t.id
        WHERE tr.user_id = %s
        AND tr.rating IS NULL
        LIMIT 5
    """
    with db.get_connection() as conn:
        with conn.cursor(dictionary=True) as cursor:
            tracks = []
            cursor.execute(query, (user_id,))
            for track in cursor.fetchall(): tracks.append(Track(**track))
            return tracks
        
def rate_track(user_id, track_id, rating):
    query = """
        UPDATE track_rating
        SET rating = %s, date = NOW()
        WHERE user_id = %s
        AND track_id = %s
    """
    with db.get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (rating, user_id, track_id))
        conn.commit()

def get_track_seed_for_user(user_id):
    query = """
        SELECT track_id
        FROM track_rating
        WHERE user_id = %s
        AND rating IS NOT NULL
        ORDER BY rating DESC, RAND()
        LIMIT 5
    """
    with db.get_connection() as conn:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(query, (user_id,))
            return [dict(track).get('track_id') for track in cursor.fetchall()]
        
def save_audio_features(tracks):
    with db.get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.executemany('''
                INSERT INTO audio_features (track_id, danceability, energy, key_, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms, time_signature)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                danceability = VALUES(danceability),
                energy = VALUES(energy),
                key_ = VALUES(key_),
                loudness = VALUES(loudness),
                mode = VALUES(mode),
                speechiness = VALUES(speechiness),
                acousticness = VALUES(acousticness),
                instrumentalness = VALUES(instrumentalness),
                liveness = VALUES(liveness),
                valence = VALUES(valence),
                tempo = VALUES(tempo),
                duration_ms = VALUES(duration_ms),
                time_signature = VALUES(time_signature)
                ''',
                [(track, features.get('danceability'), features.get('energy'), features.get('key'), features.get('loudness'), features.get('mode'), features.get('speechiness'), features.get('acousticness'), features.get('instrumentalness'), features.get('liveness'), features.get('valence'), features.get('tempo'), features.get('duration_ms'), features.get('time_signature')) for track, features in tracks.items()])
            conn.commit()