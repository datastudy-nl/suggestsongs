import data.logindata as logindata
import data.userdata as userdata

def get_user_data(jwt_token):
    if not jwt_token: return None
    id = logindata.get_id(jwt_token)
    return userdata.get_user_data(id)