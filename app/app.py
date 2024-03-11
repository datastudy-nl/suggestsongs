from flask import Flask, request, jsonify, redirect, make_response, render_template
import datastudy_commons as dsc
import service.loginservice as loginservice
import service.userservice as userservice
import service.spotifyservice as spotifyservice

main = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

@main.route('/', methods=['GET'])
def index():
    user_data = userservice.get_user_data(request.cookies.get('auth_token'))
    if not user_data: return render_template('index.html')
    return render_template('index.html', name=user_data.get('display_name'), email=user_data.get('email'), product=user_data.get('product'))

@main.route('/login', methods=['GET'])
def login():
    return redirect(loginservice.get_spotify_auth_url())

@main.route('/callback/spotify', methods=['GET'])
@dsc.flask.required_query_keys(['code'])
def spotify_callback():
    jwt_token = loginservice.login_user(request.args.get('code'))
    response = make_response(redirect('/'))
    response.set_cookie('auth_token', jwt_token, max_age=3600)
    user_id = loginservice.get_user_id(jwt_token)
    spotifyservice.get_top_tracks_user(user_id)
    return response

@main.route('/logout', methods=['GET'])
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('auth_token', '', expires=0)
    return response

if __name__ == '__main__':
    main.run(debug=True, host='0.0.0.0', port=80)