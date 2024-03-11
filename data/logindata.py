import jwt
import database as db

class UnauthorizedError(Exception): pass

SECRET_KEY = 'verysecretkey'

def create_login_token(id, display_name, email, product):
    return jwt.encode({'id': id, 'display_name': display_name, 'email': email, 'product': product}, SECRET_KEY, algorithm='HS256')

def get_id(jwt_token):
    try: return jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])['id']
    except jwt.ExpiredSignatureError: raise UnauthorizedError('Token expired')
    except jwt.InvalidTokenError: raise UnauthorizedError('Invalid token')

    
def store_authentication_code(id, access_token, refresh_token):
    query = """
        INSERT INTO authentication (id, access_token, refresh_token)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
        access_token = VALUES(access_token),
        refresh_token = VALUES(refresh_token)
    """
    with db.get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (id, access_token, refresh_token))
            conn.commit()

def get_access_token(id):
    query = 'SELECT access_token FROM authentication WHERE id = %s'
    with db.get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (id,))
            return cursor.fetchone()[0]