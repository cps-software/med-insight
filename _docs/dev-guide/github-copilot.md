To configure Visual Studio Code (VS Code) to recognize and use a Python virtual environment that was created in the same folder as your Python program, follow these steps:

### Step-by-Step Guide

1. **Create the Virtual Environment**:
   If you haven't already created a virtual environment, you can do so by running the following command in the terminal:
   ```sh
   python3 -m venv venv
   ```
   This creates a virtual environment named `venv` in the current directory.

2. **Open the Project in VS Code**:
   Open VS Code and navigate to the folder containing your Python project and the `venv` virtual environment.

3. **Activate the Virtual Environment** (Optional):
   Although VS Code can automatically detect the virtual environment, it's a good practice to activate it in the terminal to verify it's working correctly.
   - On macOS and Linux:
     ```sh
     source venv/bin/activate
     ```
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```

4. **Select the Python Interpreter**:
   - Open the Command Palette in VS Code by pressing `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS).
   - Type `Python: Select Interpreter` and press Enter.
   - VS Code will display a list of available Python interpreters, including the ones in your virtual environments.
   - Select the interpreter from your `venv` directory (something like `./venv/bin/python` or `./venv/Scripts/python.exe`).

5. **Verify the Environment**:
   - Open a new terminal in VS Code by going to `Terminal` > `New Terminal`.
   - Ensure the terminal is using the virtual environment by checking if the prompt includes the name of the virtual environment (e.g., `(venv)`).
   - You can also verify by running:
     ```sh
     which python  # macOS/Linux
     where python  # Windows
     ```
     The output should point to the Python executable inside the `venv` directory.

6. **Install Necessary Packages**:
   - With the virtual environment activated, install any required packages using `pip`:
     ```sh
     pip install <package_name>
     ```

7. **Ensure VS Code Settings Are Correct**:
   - Open the settings in VS Code by going to `File` > `Preferences` > `Settings` (or `Code` > `Preferences` > `Settings` on macOS).
   - Search for `Python: Python Path` and ensure it points to the Python interpreter in your virtual environment.

### Example Python Script

Here's an example of how your Python script might look:

```python
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_connection():
    """Creates and returns a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='CDWWork',
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
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

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        close_connection(conn)
```

### Using a `.env` File

Create a `.env` file in the root of your project and add your sensitive values:

```sh
DB_USER=your_username
DB_PASSWORD=your_password
```

This setup ensures that your Python program uses the virtual environment, keeping dependencies isolated and your project organized.