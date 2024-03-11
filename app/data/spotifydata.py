import requests

SCOPES = 'user-read-private user-read-email user-library-read user-top-read'
CLIENT_ID = '68b1593faf144e20a8a0c326fadea242'
CLIENT_SECRET = 'b15e6a71e6eb49988b6b9411f870e5bd'
REDIRECT_URL = 'https://suggestsongs.com/callback/spotify'

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
    return requests.get(f'https://api.spotify.com/v1/me/top/tracks', headers={
        'Authorization': f'Bearer {access_token}'}).json()