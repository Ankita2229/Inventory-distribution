import mysql.connector, os
from mysql.connector import connect, ClientFlag
from dotenv import load_dotenv

load_dotenv()

def returnConnection():
    conn = connect(
        host = os.getenv('db_host'),
        user = os.getenv('db_user'),
        password = os.getenv('db_password'),
        database = os.getenv('db_name'),
    )
    return conn