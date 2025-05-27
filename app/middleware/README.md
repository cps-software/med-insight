# ETL Process Subsystem

## Python
For Macbook users, macOS comes with a system version of Python pre-installed, but it is often outdated and not recommended for development.

You can check the version:
```bash
python3 --version
```

If it's an older version, consider a new installation via Homebrew.

Install Homebrew (if not already installed):  
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install Python:  
```bash
brew install python
```

Note: After installing via homebrew, the new version may not be recognized. If this is the case, refresh (or open/close) your terminal session.

Verify Installation:  
```bash
python3 --version
pip3 --version
```

This will show the latest Python3 and PIP3 versions, e.g., 3.13.3 and 25.0.1.

### Python Virtual Environment
It is recommended that you set up a Python virtual environment. This provides a self-contained directory with a Python interpreter and a set of installed packages, which isolates the dependencies required for this project.

For my local setup, I selected the root `middleware` folder as the location for the virtual environment.

Create a virtual environment:   
```bash
cd ~/swdev/cps/med-insight/app/middleware
python3 -m venv mypyenv
```

Replace "mypyenv" with your preferred name for the environment folder that's created. It is common to use "venv" for the name of the environment, so that's what I'll assume for the subsequent steps below.

Activate the virtual environment. Below are the Linux/macOS and Windows commands, respectively.

```bash
source cpsenv/bin/activate
cpsenv\Scripts\activate
```

For Git Bash, use a slightly different command:
```bash
source cpsenv\Scripts\Activate
```

After activation, you’ll notice the environment name `(venv)` appears in your terminal prompt. You can invoke Python with the command, `python` (as opposed to `python3`).

You can then install packages as normal using `pip` or install all packages from `requirements.txt`.

To activate an environment and install from the `requirements.txt` file:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Python dontenv Module
The middleware component uses the Python `dotenv` module, provided by the `python-dotenv` package. Use of this module requires a `.env` file to be placed in the root middleware folder. This file is not under source control, so you will need to ask a peer developer for information on file contents, or to get a copy for your local development environment.

Below are the contents of a sample .env file, with sensitive values removed.

```txt
# Database configuration
DB_ENGINE=MS_SQL_SERVER_2019
DB_SERVER=127.0.0.1,1433
DB_NAME=CDWWork
DB_USER=sa
DB_PASSWORD=**********
TRUST_CONNECTION=yes
TRUST_CERT=yes

# Other configuration settings
EXTRACT_FOLDER=./extract/
ADM_EXTRACT_FILENAME=adm_extract_01.csv
```

or (an older version that is tailored for external hosted SQL Server)...

```txt
# Database configuration
DB_SERVER=vhacdwdwhsql33.vha.med.va.gov/
DB_NAME=CDWWork
DB_USER=VHAMASTER\VHAISWSYLVEC
DB_PASSWORD=

# Other configuration settings
EXTRACT_FOLDER=./extracts/
ADM_EXTRACT_FILENAME=adm_extract_01.csv
```