# extract_adm.py
"""Sample program to create and write csv file to local storage"""

from dotenv import load_dotenv  # import load_dotenv function
import os                       # import entire module
import csv                      # import entire module

# load environment variables from the .env file
load_dotenv()

# Specify the folder and file name
output_folder = os.getenv('EXTRACT_FOLDER')
adm_extract_filename = os.getenv('ADM_EXTRACT_FILENAME')

# Sample data: Key, Book Title, Date Checked Out, Person's Name
data = [
    [1, "To Kill a Mockingbird", "2025-01-15", "Alice Johnson"],
    [2, "1984", "2025-01-16", "Bob Smith"],
    [3, "The Great Gatsby", "2025-01-17", "Charlie Brown"],
    [4, "Dylon Goes Electric", "2025-01-17", "Shimmer Patrick"],
]

def create_and_write_file():
    """Creates and writes a CSV file in the specified folder."""
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Define the full file path
    file_path = os.path.join(output_folder, adm_extract_filename)

    # Write the data to the CSV file
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(["key", "book_title", "date_checked_out", "checked_out_by"])
        
        # Write the data rows
        writer.writerows(data)
    
    print(f"File '{adm_extract_filename}' has been created and saved in '{output_folder}'.")
