import data.spotifydata as spotifydata
import data.logindata as logindata



def get_top_tracks_user(user_id):
    access_token = logindata.get_access_token(user_id)
    return spotifydata.get_top_tracks_user(access_token)