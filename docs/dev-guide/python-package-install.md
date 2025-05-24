To install a Python package using `pip`, you typically follow these steps. I'll use `mysql-connector-python` as an example to demonstrate the process:

1. **Open a Terminal**: On macOS, you can open the Terminal application.

2. **Activate your virtual environment (optional but recommended)**: It's a good practice to use virtual environments to manage dependencies for your Python projects. If you don't have a virtual environment set up, you can create one using the following commands:
    ```sh
    python3 -m venv myenv
    source myenv/bin/activate
    ```
    Replace `myenv` with the name of your virtual environment.

3. **Install the package using pip**:
    - You do not need to be in the root folder of your Python project to run the `pip` command, but it's often convenient to do so.
    - Run the following command to install `mysql-connector-python`:
    ```sh
    pip install mysql-connector-python
    ```

4. **Verify the installation**:
    - To verify that the package has been installed correctly, you can list the installed packages using:
    ```sh
    pip list
    ```
    - You should see `mysql-connector-python` in the list of installed packages.

5. **Use the package in your Python script**:
    - Now, you can import and use the `mysql-connector-python` package in your Python script as needed. For example:
    ```python
    import mysql.connector

    # Create a connection to the database
    connection = mysql.connector.connect(
        host='localhost',
        database='CDWWork',
        user='your_username',
        password='your_password'
    )

    # Check if the connection is successful
    if connection.is_connected():
        print("Successfully connected to the database")
        connection.close()
    ```

### Summary of Steps:
1. Open Terminal.
2. (Optional) Create and activate a virtual environment.
3. Run `pip install mysql-connector-python` to install the package.
4. Verify the installation with `pip list`.
5. Use the package in your Python script.

By following these steps, you should be able to install and use `mysql-connector-python` or any other Python package in your projects.