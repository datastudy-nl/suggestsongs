import data.spotifydata as spotifydata
import data.logindata as logindata
import service.trackservice as trackservice



def get_top_tracks_user(user_id):
    access_token = logindata.get_access_token(user_id)
    top_tracks = spotifydata.get_top_tracks_user(access_token)
    trackservice.save_top_tracks_user(user_id, top_tracks)
    return 

def get_recommendations(user_id):
    access_token = logindata.get_access_token(user_id)
    seed_tracks = trackservice.get_track_seed_for_user(user_id)
    recommendations = spotifydata.get_recommendations(access_token, seed_tracks)
    trackservice.save_top_tracks_user(user_id, recommendations)

def get_audio_features(user_id, tracks):
    access_token = logindata.get_access_token(user_id)
    return spotifydata.get_audio_features(access_token, tracks)

def add_random_unrated_tracks(user_id):
    access_token = logindata.get_access_token(user_id)
    random_tracks = trackservice.get_random_tracks()
    trackservice.save_top_tracks_user(user_id, random_tracks)
    return