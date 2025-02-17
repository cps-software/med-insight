# db_query.py
"""Custom queries to get DSS extract data for each extract type"""

# import required dependencies
from src.constants import *
from src.db_config import create_connection, close_connection
import pyodbc

# -----------------------------------------------------------
# Fetch ADM records
# -----------------------------------------------------------
def fetch_adm_records(station, start_date, end_date):
    """Run query(s) to fetch records from tables in the CDWWork database."""
    connection = create_connection()
    if connection is None:
        return

    try:       
        # create a cursor
        cursor = connection.cursor()

        # execute query
        cursor.execute(ADM_QUERY_01, station, start_date, end_date)

        # fetch all records (into list)
        records = cursor.fetchall()

        if records:
            print(f"{len(records)} Records found\n")
            print(f"{GREEN}{ADM_SEQUENCE_NUMBER}{ADM_YEAR_MONTH}{EXTRACT_NUMBER}{RESET}\n")
            # Print each row using caret as delimiter
            for row in records:
                print(GREEN + "^".join(str(value) for value in row), end="~\n")
                print(RESET)

            # print("Records found:\n")
            # print(f"{GREEN}{ADM_SEQUENCE_NUMBER}{ADM_YEAR_MONTH}{EXTRACT_NUMBER}{RESET}\n")
            # for row in records:
            #     print(f"{GREEN}{row}{RESET}")
            #     print()
        else:
            print("No records found from this select statement.")

        print()

    except pyodbc.Error as e:
        print(f"Error fetching records: {e}")
    finally:
        cursor.close()
        close_connection(connection)

# -----------------------------------------------------------
# Fetch RAD records
# -----------------------------------------------------------
def fetch_rad_records(station, start_date, end_date):
    """Run query(s) to fetch records from tables in the CDWWork database."""
    connection = create_connection()
    if connection is None:
        return

    try:       
        # create a cursor
        cursor = connection.cursor()

        # execute query
        cursor.execute(RAD_QUERY_01, station, start_date, end_date)

        # fetch all records (into list)
        records = cursor.fetchall()

        if records:
            print("Records found:\n")
            print(f"{GREEN}{ADM_SEQUENCE_NUMBER}{ADM_YEAR_MONTH}{EXTRACT_NUMBER}{RESET}")
            for row in records:
                print(f"{GREEN}{row}{RESET}")
                print()
        else:
            print("No records found from this select statement.")

        print()

    except pyodbc.Error as e:
        print(f"Error fetching records: {e}")
    finally:
        cursor.close()
        close_connection(connection)