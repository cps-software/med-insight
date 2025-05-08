# Med-Insight
Med-Insight works with healthcare information to provide various services and insights. One capability is a demonstration of ETL functionality between a source data warehouse and a target system that receives transformed data via SFTP in the form of text-based flat files.

## Overview
Med-Insight is a full-stack application comprised of the following components:  

| Component   | Description |
| ----------- | ----------- |
| data-source | Mock SQL database, REST service, and website that simulate data sources |
| etl-layer   | Python-based ETL and medallion architecture data management functionality |
| web-app     | PHP-based web application that includes a dashboard and other functionality |

## Getting Started
To get started, clone this repository into a directory of your choice and navigate to the med-insight folder.

```txt
git clone https://github.com/cps-software/med-insight.git  
cd med-insight  
```

## Local Development Environment Setup
Each component uses one or more technology. Refer to the README.md file within each of these subsystems for information on local development environmetn setup.  

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

Note: After installing via homebrew, the new version may not be recognized. If this is the case, refresh (or open/close) your terminal session.

Verify Installation:  
```bash
python3 --version
pip3 --version
```

This will show the latest Python3 and PIP3 versions, e.g., 3.13.2.

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

### Local SQLite Database
(this part not implemented yet)  

## Deployment
For development purposes, each of the three components is run directly from the command line. The current focus is on the middleware component, which runs from a terminal command line, within the Python virtual environment that was created and activated.
