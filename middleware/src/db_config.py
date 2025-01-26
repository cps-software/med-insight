# db_config.py

import pyodbc                      # import entire module
from dotenv import load_dotenv     # import load_dotenv function
import os                          # import entire module

# load environment variables from the .env file
load_dotenv()

def create_connection():
    """Creates and returns a connection to the MySQL database."""

    # Print driver f-string for debugging
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    
    # Print environment variables for debugging
    print("DB_SERVER:", os.getenv('DB_SERVER'))
    print("DB_NAME:", os.getenv('DB_NAME'))
    print("DB_USER:", os.getenv('DB_USER'))
    print("DB_PASSWORD:", os.getenv('DB_PASSWORD'))
    print("TRUST_CERT:", os.getenv('TRUST_CERT'))
    print()

    try:
        connection_string = (
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={os.getenv('DB_SERVER')};"
            f"DATABASE={os.getenv('DB_NAME')};"
            f"UID={os.getenv('DB_USER')};"   
            f"PWD={os.getenv('DB_PASSWORD')};"
            f"TrustServerCertificate={os.getenv('TRUST_CERT')};"
        )
        connection = pyodbc.connect(connection_string)
        print("Successfully connected to the database")
        return connection
    except pyodbc.Error as e:
        print(f"Error while connecting to SQL Server: {e}")
        return None

def close_connection(connection):
    """Closes the given database connection."""
    try:
        connection.close()
        print("SQL Server connection is closed")
    except pyodbc.Error as e:
        print(f"Error while closing the connection: {e}")