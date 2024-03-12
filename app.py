from flask import Flask, request, jsonify, redirect, make_response, render_template
import datastudy_commons as dsc
import service.loginservice as loginservice
import service.userservice as userservice
import service.spotifyservice as spotifyservice
import service.trackservice as trackservice
import dotenv, os

main = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

@main.route('/', methods=['GET'])
@dsc.flask.catch_exceptions
def index():
    try:
        user_data = userservice.get_user_data(request.cookies.get('auth_token'))
        if not user_data: return render_template('index.html')
        return render_template('index.html', name=user_data.get('display_name'), email=user_data.get('email'), product=user_data.get('product'))
    except:
        return render_template('index.html')

@main.route('/login', methods=['GET'])
@dsc.flask.catch_exceptions
def login():
    return redirect(loginservice.get_spotify_auth_url())

@main.route('/callback/spotify', methods=['GET'])
@dsc.flask.required_query_keys(['code'])
@dsc.flask.catch_exceptions
def spotify_callback():
    jwt_token = loginservice.login_user(request.args.get('code'))
    response = make_response(redirect('/'))
    response.set_cookie('auth_token', jwt_token, max_age=3600)
    user_id = loginservice.get_user_id(jwt_token)
    spotifyservice.get_top_tracks_user(user_id)
    return response

@main.route('/logout', methods=['GET'])
@dsc.flask.catch_exceptions
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('auth_token', '', expires=0)
    return response

@main.route('/api/next-songs', methods=['GET'])
@dsc.flask.catch_exceptions
def next_songs():
    user_id = loginservice.get_user_id(request.cookies.get('auth_token'))
    return jsonify({'data': trackservice.get_next_songs(user_id)})

@main.route('/api/rate-track', methods=['POST'])
@dsc.flask.required_body_keys(['id', 'rating'])
@dsc.flask.catch_exceptions
def rate_track():
    user_id = loginservice.get_user_id(request.cookies.get('auth_token'))
    trackservice.rate_track(user_id, request.json.get('id'), request.json.get('rating'))
    return jsonify({'status': 'ok'})

if __name__ == '__main__': main.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 80))