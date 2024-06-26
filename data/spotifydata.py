import requests
import os
import dto.track as track

SCOPES = os.getenv('SCOPES')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URL = os.getenv('REDIRECT_URL')


def convert_spotify_code(code):
    return requests.post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URL,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()


def get_spotify_auth_url():
    return f'https://accounts.spotify.com/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URL}&scope={SCOPES}'


def get_user_data(access_token):
    return requests.get('https://api.spotify.com/v1/me', headers={'Authorization': f'Bearer {access_token}'}).json()

def get_top_tracks_user(access_token):
    response = requests.get(f'https://api.spotify.com/v1/me/top/tracks', headers={
        'Authorization': f'Bearer {access_token}'}).json()
    tracks = []
    if not response.get('items'): return []
    for item in response.get('items'):
        tracks.append(
            track.Track(
                item.get('id'),
                item.get('name'),
                item.get('artists')[0].get('name') if item.get('artists') else None,
                item.get('album').get('name') if item.get('album') else None,
                item.get('duration_ms'),
                item.get('popularity'),
                item.get('explicit'),
                item.get('external_urls').get('spotify')
            )
        )
    return tracks

def get_recommendations(access_token, seed_tracks):
    seed_tracks_text = ','.join(seed_tracks)
    response = requests.get(f'https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks_text}', headers={
        'Authorization': f'Bearer {access_token}'}).json()
    tracks = []
    if not response.get('tracks'): return []
    for item in response.get('tracks'):
        tracks.append(
            track.Track(
                item.get('id'),
                item.get('name'),
                item.get('artists')[0].get('name') if item.get('artists') else None,
                item.get('album').get('name') if item.get('album') else None,
                item.get('duration_ms'),
                item.get('popularity'),
                item.get('explicit'),
                item.get('external_urls').get('spotify')
            )
        )
    return tracks

def get_audio_features(access_token, tracks):
    track_ids = ','.join(tracks)
    response = requests.get(f'https://api.spotify.com/v1/audio-features?ids={track_ids}', headers={
        'Authorization': f'Bearer {access_token}'}).json()
    features = {}
    for item in response.get('audio_features'):
        features[item.get('id')] = {
            'danceability': item.get('danceability'),
            'energy': item.get('energy'),
            'key': item.get('key'),
            'loudness': item.get('loudness'),
            'mode': item.get('mode'),
            'speechiness': item.get('speechiness'),
            'acousticness': item.get('acousticness'),
            'instrumentalness': item.get('instrumentalness'),
            'liveness': item.get('liveness'),
            'valence': item.get('valence'),
            'tempo': item.get('tempo'),
            'time_signature': item.get('time_signature')
        }
    return features


def refresh_access_token(refresh_token):
    return requests.post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()