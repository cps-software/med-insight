# main.py
"""Main application for DSS extract ETL functions"""

# import sql query statement constants
from src.constants import SELECT_ALL_Dim_Sta3n, SELECT_COLUMNS_Sta3n
from src.constants import SELECT_ALL_Spatient_Spatient, SELECT_COLUMNS_Spatient_Spatient
from src.constants import SELECT_INNER_JOIN_Spatient_Sta3n

# import helper functions
from src.db_config import create_connection, close_connection
from src.extract_adm import create_and_write_file

# import os routines module
import os

def fetch_all_records():
    """Run query(s) to fetch records from tables in the CDWWork database."""
    connection = create_connection()
    if connection is None:
        return

    try:       
        # cursor = connection.cursor()               # return rows as tuples
        cursor = connection.cursor(dictionary=True)  # return rows as key/value pairs
        cursor.execute(SELECT_INNER_JOIN_Spatient_Sta3n)
        records = cursor.fetchall()
        
        if records:
            print("Records found:")
            for row in records:
                print(row)
                print()
        else:
            print("No records found from this select statement.")
    except Error as e:
        print(f"Error fetching records: {e}")
    finally:
        cursor.close()
        close_connection(connection)

def main():
    print(f"\nStarting main.py... {__name__}\n")
    fetch_all_records()
    print(f"\nExtract files will be written to: {os.getenv('EXTRACT_FOLDER')}")
    create_and_write_file()
    print("\nmain.py complete...\n")

if __name__ == "__main__":
    main()