import sqlite3

DATABASE_NAME = './database/magazine.db'

def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='DATABASE_NAME',
            user='yourusername',
            password='yourpassword'
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"An error occurred: {e}")
        return None

