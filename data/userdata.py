import database as db

def get_user_data(id):
    query = """
        SELECT id, display_name, email, product, country, image
        FROM users
        WHERE id = %s
    """
    with db.get_connection() as conn:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(query, (id,))
            return cursor.fetchone()
        

def create_user(user_data):
    query = """
        INSERT INTO users (id, display_name, email, product, country, image)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        display_name = VALUES(display_name),
        email = VALUES(email),
        product = VALUES(product),
        country = VALUES(country),
        image = VALUES(image)
    """
    with db.get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (
                user_data.get('id'),
                user_data.get('display_name'),
                user_data.get('email'),
                user_data.get('product'),
                user_data.get('country'),
                user_data.get('images')[0].get('url')
            ))
        conn.commit()