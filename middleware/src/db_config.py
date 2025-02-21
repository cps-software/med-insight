# db_config.py

import pyodbc                      # import entire module
from dotenv import load_dotenv     # import load_dotenv function
import os                          # import entire module

# load environment variables from the .env file
load_dotenv()

def create_connection():
    """
    Creates and returns a connection to designated SQL Server database. The
    two 'Trust' related string literal parameters are specific to either macOS
    or Windows, so depending on your envirionment, one will be commented out.
    Yes, this is a cludge, but hey, I'm just one person with a lot of code to write!
    """
    try:
        connection_string = (
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={os.getenv('DB_SERVER')};"
            f"DATABASE={os.getenv('DB_NAME')};"
            f"UID={os.getenv('DB_USER')};"
            f"PWD={os.getenv('DB_PASSWORD')};"
            # f"Trusted_Connection={os.getenv('TRUST_CONNECTION')};"
            f"TrustServerCertificate={os.getenv('TRUST_CERT')};"
        )
        connection = pyodbc.connect(connection_string)
        print("Successfully connected to the database")
        return connection
    except pyodbc.Error as e:
        print(f"Error while connecting to SQL Server: {e}")
        return None

def close_connection(connection):
    """Close the given database connection."""
    try:
        connection.close()
        print("SQL Server connection is closed")
    except pyodbc.Error as e:
        print(f"Error while closing the connection: {e}")