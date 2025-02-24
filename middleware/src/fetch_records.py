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

        # execute query 01
        print("Executing query to select Patient Cohort into global temp table")
        cursor.execute(ADM_QUERY_01, station, start_date, end_date)

        # execute query 02
        print("Executing query to select all rows from global temp table")
        cursor.execute(ADM_QUERY_02)

        # fetch all records from query 02 into a list
        records = cursor.fetchall()

        if records:
            print(f"{len(records)} Records found\n")
            # Print each row with pipe delimiter
            for row in records:
                print(GREEN + "|".join(str(value) for value in row), end="\n")
                print(RESET, end="")
        else:
            print("No records found from this select statement.")

        print()

        # execute query 03
        print("Executing query to select ADM extract dataset into global temp table")
        cursor.execute(ADM_QUERY_03)

        # execute query 04
        print("Executing query to select all rows from global temp table (unsorted)")
        cursor.execute(ADM_QUERY_04)

        # fetch all records (into list)
        records = cursor.fetchall()

        if records:
            print(f"{len(records)} Records found\n")
            # Print each row with pipe delimiter
            for row in records:
                print(GREEN + "|".join(str(value) for value in row), end="\n")
                print(RESET)
        else:
            print("No records found from this select statement.")

        print()

        # execute query 05
        print("Executing query to select all rows from global temp table (transformed & sorted)")
        cursor.execute(ADM_QUERY_05)

        # fetch all records (into list)
        records = cursor.fetchall()

        if records:
            print(f"{len(records)} Records found\n")
            print(f"{GREEN}{ADM_SEQUENCE_NUMBER}{ADM_YEAR_MONTH}{EXTRACT_NUMBER}{RESET}\n")
            # Print each row with pipe delimiter
            for row in records:
                print(GREEN + "|".join(str(value) for value in row), end="\n")
                print(RESET)
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