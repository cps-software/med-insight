### Project Plan and Strategy

#### Agile Project Plan

1. **Sprint 0: Project Setup and Planning**
   - Define project scope and objectives.
   - Set up GitHub repository with recommended folder structure.
   - Set up Docker environment for local development.
   - Set up SQL Server instance (local or cloud-based).
   - Define user stories and acceptance criteria.
   - Create a product backlog.

2. **Sprint 1: Data Extraction**
   - Develop Python script to connect to the source SQL Server database.
   - Extract data from the source database.
   - Implement basic error handling and logging.
   - Create initial version of the "extract output" database and tables.

3. **Sprint 2: Data Transformation**
   - Develop Python script to transform extracted data.
   - Implement data validation and cleansing.
   - Add more detailed logging and error handling.

4. **Sprint 3: Data Loading**
   - Develop Python script to load transformed data into the "extract output" database.
   - Generate the delimited text file.
   - Implement terminal-based UI for user interaction.

5. **Sprint 4: Testing and Refinement**
   - Conduct unit tests, integration tests, and user acceptance tests.
   - Refine code based on feedback and test results.
   - Optimize performance and ensure security best practices.

6. **Sprint 5: Deployment and Documentation**
   - Prepare deployment package.
   - Document the application, including setup instructions, user guide, and API documentation.
   - Conduct final review and project retrospective.

### Recommended Software Code Repository Structure

```
etl-health-info/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── .vscode/
│   └── settings.json
├── config/
│   └── .env
├── data/
│   └── sample_data.sql
├── docs/
│   └── README.md
├── scripts/
│   └── setup_db.sql
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── main.py
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       └── db_connector.py
├── tests/
│   ├── __init__.py
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

### Starter Code

#### `src/extract.py`

```python
import pyodbc
import pandas as pd
from utils.db_connector import get_db_connection
from utils.logger import setup_logger

logger = setup_logger('extract')

def extract_data(connection_string):
    try:
        conn = get_db_connection(connection_string)
        query = "SELECT * FROM PatientData"
        df = pd.read_sql(query, conn)
        logger.info("Data extraction successful")
        return df
    except Exception as e:
        logger.error(f"Error during data extraction: {e}")
        raise
```

#### `src/transform.py`

```python
import pandas as pd
from utils.logger import setup_logger

logger = setup_logger('transform')

def transform_data(df):
    try:
        # Example transformation: Convert patient names to uppercase
        df['PatientName'] = df['PatientName'].str.upper()
        logger.info("Data transformation successful")
        return df
    except Exception as e:
        logger.error(f"Error during data transformation: {e}")
        raise
```

#### `src/load.py`

```python
import pyodbc
import pandas as pd
from utils.db_connector import get_db_connection
from utils.logger import setup_logger

logger = setup_logger('load')

def load_data(df, connection_string):
    try:
        conn = get_db_connection(connection_string)
        cursor = conn.cursor()
        
        # Insert into extract output table
        for index, row in df.iterrows():
            cursor.execute("INSERT INTO ExtractOutput (PatientID, PatientName) VALUES (?, ?)", row['PatientID'], row['PatientName'])
        
        # Insert into log table
        cursor.execute("INSERT INTO ETLLog (RecordsProcessed) VALUES (?)", len(df))
        
        conn.commit()
        logger.info("Data loading successful")
    except Exception as e:
        logger.error(f"Error during data loading: {e}")
        raise

def generate_delimited_file(df, file_path):
    try:
        df.to_csv(file_path, sep='^', line_terminator='~\n', index=False)
        logger.info("Delimited file generation successful")
    except Exception as e:
        logger.error(f"Error during delimited file generation: {e}")
        raise
```

#### `src/main.py`

```python
import os
from dotenv import load_dotenv
from extract import extract_data
from transform import transform_data
from load import load_data, generate_delimited_file
from utils.logger import setup_logger

logger = setup_logger('main')

def main():
    load_dotenv()
    source_connection_string = os.getenv('SOURCE_DB_CONNECTION_STRING')
    target_connection_string = os.getenv('TARGET_DB_CONNECTION_STRING')
    output_file_path = os.getenv('OUTPUT_FILE_PATH')

    try:
        # Extract
        df = extract_data(source_connection_string)
        print("Data extracted successfully.")
        
        # Transform
        df = transform_data(df)
        print("Data transformed successfully.")
        
        # Load
        load_data(df, target_connection_string)
        generate_delimited_file(df, output_file_path)
        print("Data loaded and delimited file generated successfully.")
        
        # Display results
        print("\nExtract Records:")
        print(df)
        print(f"\nTotal Records Processed: {len(df)}")
    except Exception as e:
        logger.error(f"Error in ETL pipeline: {e}")

if __name__ == "__main__":
    main()
```

#### `utils/db_connector.py`

```python
import pyodbc

def get_db_connection(connection_string):
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        raise e
```

#### `utils/logger.py`

```python
import logging

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
```

### Supporting Files

#### `.env`

```
SOURCE_DB_CONNECTION_STRING=your_source_db_connection_string
TARGET_DB_CONNECTION_STRING=your_target_db_connection_string
OUTPUT_FILE_PATH=output/output_file.txt
```

#### `.gitignore`

```
.env
__pycache__/
*.pyc
*.pyo
*.pyd
*.db
*.sqlite3
output/
```

#### `README.md`

```markdown
# ETL Health Information Management

This project performs ETL (Extract, Transform, Load) operations for health information management.

## Setup

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set up your `.env` file with the necessary connection strings and file paths.
4. Run the application: `python src/main.py`.

## Requirements

- Python 3.x
- pyodbc
- pandas
- python-dotenv
```

#### `requirements.txt`

```
pyodbc
pandas
python-dotenv
```

### Recommended Practices for Securing Sensitive Information

- Use `.env` files to store sensitive information like connection strings and passwords.
- Add `.env` to `.gitignore` to prevent it from being committed to the repository.
- Use environment variables in your CI/CD pipeline to inject sensitive information during deployment.

### Terminal-Based UI

For a nice and intuitive terminal-based UI, consider using the `colorama` library to add color to your text prompts. Here’s an example:

```python
from colorama import Fore, Style

print(Fore.GREEN + "Data extracted successfully." + Style.RESET_ALL)
print(Fore.BLUE + "Data transformed successfully." + Style.RESET_ALL)
print(Fore.YELLOW + "Data loaded and delimited file generated successfully." + Style.RESET_ALL)
```

This will make the output more readable and visually appealing.

### Docker Setup

#### `Dockerfile`

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]
```

#### `docker-compose.yml`

```yaml
version: '3.8'

services:
  etl:
    build: .
    environment:
      - SOURCE_DB_CONNECTION_STRING=${SOURCE_DB_CONNECTION_STRING}
      - TARGET_DB_CONNECTION_STRING=${TARGET_DB_CONNECTION_STRING}
      - OUTPUT_FILE_PATH=${OUTPUT_FILE_PATH}
    volumes:
      - .:/app
```

This setup will allow you to run the ETL application in a Docker container, ensuring consistency across different development environments.

By following this plan and structure, your team should be well-equipped to develop a robust and maintainable ETL application for health information management.