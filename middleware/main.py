# main.py
"""Main application for DSS extract ETL functions"""

# import sql query statement and other constants
from src.constants import *

# import helper functions
from src.db_config import create_connection, close_connection
from src.extract_adm import create_and_write_file

# import os routines module
import os

# import odbc driver module
import pyodbc

def fetch_all_records(station, start_date, end_date):
    """Run query(s) to fetch records from tables in the CDWWork database."""
    connection = create_connection()
    if connection is None:
        return

    try:       
        # create a cursor
        cursor = connection.cursor()

        # execute query
        cursor.execute(ADM_QUERY_02, station, start_date, end_date)

        # fetch all records (into key/value tupples)
        # columns = [column[0] for column in cursor.description]  # Get column names
        # records = [dict(zip(columns, row)) for row in cursor.fetchall()]  # Convert to list of dicts

        # fetch all records (into list)
        records = cursor.fetchall()

        if records:
            print("Records found:\n")
            print(f"{GREEN}{ADM_SEQUENCE_NUMBER}{ADM_YEAR_MONTH}{EXTRACT_NUMBER}{RESET}")
            for row in records:
                print(f"{GREEN}{row}{RESET}")
        else:
            print("No records found from this select statement.")

        print()

    except pyodbc.Error as e:
        print(f"Error fetching records: {e}")
    finally:
        cursor.close()
        close_connection(connection)

def main():
    station = input(f"{YELLOW}\n   Please enter a VistA Station Number: {RESET}")
    start_date = input(f"{YELLOW}  Please enter start date (YYYY-MM-DD): {RESET}")
    end_date = input(f"{YELLOW}    Please enter end date (YYYY-MM-DD): {RESET}")
    print()
    
    fetch_all_records(station, start_date, end_date)
    
    print(f"\nExtract files will be written to: {os.getenv('EXTRACT_FOLDER')}")
    create_and_write_file()

    print("\nmain.py complete...\n")

if __name__ == "__main__":
    main()