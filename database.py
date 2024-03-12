import mysql.connector as mysql
import os


MYSQL_SERVER = os.environ.get('DB_HOST', '192.168.1.36')
MYSQL_USER = os.environ.get('DB_USER', 'datastudy_api')
MYSQL_PASSWORD = os.environ.get('DB_PASS', 'INFLUSTRAT_PASSWORD_FOR_MYSQL_THING_MUCH_YES')
MYSQL_DATABASE = os.environ.get('DB_NAME', 'spotimatcher')

def get_connection():
    return mysql.connect(
        host=MYSQL_SERVER,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

def create_tables():
    with open('setup.sql') as f: query = f.read()

    with get_connection() as conn:
        with conn.cursor() as cursor:
            queries = query.split(';')
            for q in queries:
                if q.strip(): cursor.execute(q)

create_tables()