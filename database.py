import mysql.connector as mysql
import os


MYSQL_SERVER = os.environ.get('DB_HOST', 'localhost')
MYSQL_USER = os.environ.get('DB_USER', 'root')
MYSQL_PASSWORD = os.environ.get('DB_PASS', 'root')
MYSQL_DATABASE = os.environ.get('DB_NAME', 'suggestsongs')

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