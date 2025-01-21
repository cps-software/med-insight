# db_config.py

import mysql.connector             # import entire module
from mysql.connector import Error  # import Error class into global namespace
from dotenv import load_dotenv     # import load_dotenv function
import os                          # import entire module

# load environment variables from the .env file
load_dotenv()

def create_connection():
    """Creates and returns a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_SERVER'),       # get from .env
            database=os.getenv('DB_NAME'),     # get from .env
            user=os.getenv('DB_USER'),         # get from .env
            password=os.getenv('DB_PASSWORD')  # get from .env
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def close_connection(connection):
    """Closes the given database connection."""
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")


DB_CONFIG = {
    'server': os.getenv('DB_SERVER'),
    'database': os.getenv('DB_NAME'),
    'username': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
}