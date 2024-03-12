import data.logindata as logindata
import data.userdata as userdata

def get_user_data(jwt_token):
    if not jwt_token: return None
    id = logindata.get_id(jwt_token)
    return userdata.get_user_data(id)

def save_feedback(user_id, feedback):
    if len(feedback) > 1000: raise ValueError('Feedback too long')
    if len(feedback) < 10: raise ValueError('Feedback too short')
    userdata.save_feedback(user_id, feedback)