import data.spotifydata as spotifydata
import data.logindata as logindata
import data.userdata as userdata

def get_spotify_auth_url():
    return spotifydata.get_spotify_auth_url()

def login_user(code):
    auth_token = spotifydata.convert_spotify_code(code)
    me_data = spotifydata.get_user_data(auth_token['access_token'])
    userdata.create_user(me_data)
    logindata.store_authentication_code(me_data['id'], auth_token['access_token'], auth_token['refresh_token'])
    return logindata.create_login_token(me_data['id'], me_data['display_name'], me_data['email'], me_data['product'])

def get_user_id(jwt_token):
    return logindata.get_id(jwt_token)

def get_access_token(user_id):
    return logindata.get_access_token(user_id)[0]

def refresh_access_token(user_id):
    auth_token = spotifydata.refresh_access_token(logindata.get_access_token(user_id)[1])
    logindata.store_authentication_code(user_id, auth_token['access_token'], auth_token['refresh_token'])
    return auth_token['access_token']