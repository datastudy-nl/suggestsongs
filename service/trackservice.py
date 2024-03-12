import dto.track as track
import data.trackdata as trackdata
import service.spotifyservice as spotifyservice

def save_top_tracks_user(user_id, top_tracks):
    if not top_tracks: return
    trackdata.save_tracks(top_tracks)
    features = spotifyservice.get_audio_features(user_id, [track.id for track in top_tracks])
    trackdata.save_audio_features(features)
    trackdata.add_unrated_tracks(user_id, top_tracks)
    return

def get_top_rated_tracks(user_id):
    return [track.to_dict() for track in trackdata.get_top_rated_tracks(user_id)]

def get_next_songs(user_id):
    next_tracks = trackdata.get_unrated_tracks(user_id)
    if not next_tracks:
        spotifyservice.get_recommendations(user_id)
        next_tracks = trackdata.get_unrated_tracks(user_id)
    if not next_tracks:
        spotifyservice.add_random_unrated_tracks(user_id)
        next_tracks = trackdata.get_unrated_tracks(user_id)
    
    return [track.to_dict() for track in next_tracks]

def rate_track(user_id, track_id, rating):
    trackdata.rate_track(user_id, track_id, rating)
    return

def get_track_seed_for_user(user_id):
    return trackdata.get_track_seed_for_user(user_id)

def get_random_tracks():
    return trackdata.get_random_tracks()