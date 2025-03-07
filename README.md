# Med-Insight
Med-Insight works with healthcare information to provide various services and insights. One capability is a demonstration of ETL functionality between a source data warehouse and a target system that receives transformed data via SFTP in the form of text-based flat files.

## Overview
Med-Insight is a full-stack application comprised of the following components:  

- **frontend**: HTML/CSS/JavaScript user interface and client-side logic
- **backend**: PHP driven server-side logic, APIs, and page rendering
- **middleware**: Python based ETL and data management functionality
- _**docs**: Project documentation and user guides

## Getting Started
To get started, clone this repository into a directory of your choice and navigate to the med-insight folder.

```txt
git clone https://github.com/cps-software/med-insight.git  
cd med-insight  
```

## Folder Structure
- `_dbscript`: database creation and update scripts
- `_docs`: application documentation files
- `backend`: PHP code for backend services
- `frontend`: HTML, CSS, and JavaScript files for the user interface
- `middleware`: Python code for ETL and data processing

```txt
med-insight/
├── _dbscript/
├── _docs/
├── backend/
│   ├── api/
│   │   ├── auth.php
│   │   ├── records.php
│   │   ├── analysis.php
│   │   ├── insights.php
│   │   └── tracking.php
│   ├── config/
│   │   └── database.php
│   ├── index.php
├── frontend/
│   ├── css/
│   │   ├── styles.css
│   │   └── dashboard.css
│   ├── js/
│   │   ├── main.js
│   │   ├── dashboard.js
│   │   └── tracking.js
│   ├── pages/
│   │   ├── dashboard.html
│   │   └── tracking.html
│   └── index.html
├── middleware/
│   ├── app/
│   │   ├── model.py
│   │   ├── preprocess.py
│   │   ├── risk_analysis.py
│   │   └── api.py
│   ├── requirements.txt
│   └── run.sh
├── .gitignore
└── README.md
```

## Local Development Environment Setup

### Python
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

Verify Instalation:  
```bash
python3 --version
pip3 --version
```

#### Python Virtual Environment
It is recommended that you set up a Python virtual environment. This provides a self-contained directory with a Python interpreter and a set of installed packages, which isolates the dependencies required for this project.

For my local setup, I selected the root `middleware` folder as the location for the virtual environment.

Create a virtual environment:   
```txt
cd ~/swdev/cps/med-insight/middleware
python3 -m venv cpsenv
```

Replace "cpsenv" with your preferred name for the environment folder that's created.

Activate the virtual environment. Below are the Linux/macOS and Windows commands, respectively.

```txt
source cpsenv/bin/activate
cpsenv\Scripts\activate
```

For Git Bash, use a slightly different command:
```text
source cpsenv\Scripts\Activate
```

After activation, you’ll notice the environment name `(cpsenv)` appears in your terminal prompt. You can invoke Python with the command, `python` (as opposed to `python3`).

You can then install packages as normal using `pip` or install all packages from `requirements.txt`.

To activate an environment and install from the `requirements.txt` file:
```txt
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Python dontenv Module
The middleware component uses the Python `dotenv` module, provided by the `python-dotenv` package. Use of this module requires a `.env` file to be placed in the root middleware folder. This file is not under source control, so you will need to ask a peer developer for information on file contents, or to get a copy for your local development environment.

### Local SQL Server Database
This one is a little more entailed, since it requires a Docker image that runs Microsoft SQL Server 2019 within an Ubuntu Linux container. Refer to the Docker and Microsoft websites for installation instructions.

### SQL Server Database Load
Once Docker, Ubuntu, and Microsft SQL Server are installed and running in a container, proceed to running the SQL scripts located in the `_dbscript\sqlserver\cdwwork` folder. Begin with the "create" scripts, and then run the "insert" scripts.

### Local SQLite Database
(this part not implemented yet)  

## Deployment
For development purposes, each of the three components is run directly from the command line. The current focus is on the middleware component, which runs from a terminal command line, within the Python virtual environment that was created and activated.
