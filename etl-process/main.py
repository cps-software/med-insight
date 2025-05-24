# main.py
"""Main application for DSS extract ETL functions"""

# import required dependencies
from src.extract_adm import create_and_write_file
from src.constants_general import *
from src.constants_sql_adm import *
from src.fetch_records import *
import os

def main():
    """
    Prompt user for DSS extract processing parameters
    Run fetch function for selected extract tyoe
    Create extract(s)
    Update database with logging info
    Returns: None
    """
    print()
    print(f"{YELLOW}           +---------------------------------------+   {RESET}")
    print(f"{YELLOW}           |   CREATE DSS EXTRACT FROM CDW DATA    |   {RESET}")
    print(f"{YELLOW}           +---------------------------------------+   {RESET}")
    print()
    station    = input(f"{YELLOW}     Please enter a VistA Station Number: {RESET}")
    extract    = input(f"{YELLOW}   Please enter an extract name (or ALL): {RESET}").upper()
    start_date = input(f"{YELLOW}    Please enter start date (YYYY-MM-DD): {RESET}")
    end_date   = input(f"{YELLOW}      Please enter end date (YYYY-MM-DD): {RESET}")
    print()
    
    # fetch records for selected extract
    if extract == "ADM":
        fetch_adm_records(station, start_date, end_date)
    elif extract =="RAD":
        fetch_rad_records(station, start_date, end_date)
    else:
        print(f"{RED}\nInvalid Extract Name: {extract}\n{RESET}")
    
    print(f"\nExtract files will be written to: {os.getenv('EXTRACT_FOLDER')}")
    create_and_write_file()

    print("\nmain.py complete...\n")

if __name__ == "__main__":
    main()