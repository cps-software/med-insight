# Med-Insight
Med-Insight is a web-based application designed to analyze healthcare information and identify potential drug risks with a focus on female health concerns. The application combines the LAMP stack with AI/ML capabilities to deliver actionable insights.  

Med-Insight provides a robust platform for examining medical records to identify potential drug risks, such as adverse reactions and drug-drug interactions, with a special focus on female health and related risks. The AI/ML component includes natural language processing (NLP) for understanding medical text and machine learning for risk prediction and pattern detection.

A new focus for Med-Insight is to demonstrate CDW integration and data extract file creation.

## Overview
Med-Insight is a full-stack application comprising the following parts:  

- **frontend**: User interface components and client-side logic.
- **backend**: Server-side logic and APIs.
- **middleware**: ETL and data management components.
- _**docs**: Project documentation and user guides.

## Getting Started
To get started, clone this repository into a directory of your choice and navigate to the med-insight folder.

```bash
git clone https://github.com/cps-software/med-insight.git  
cd med-insight  
```

## Folder Structure
- `_dbscript`: database creation and update scripts
- `_docs`: application documentation files
- `backend`: PHP code for backend services
- `frontend`: HTML, CSS, and JavaScript files for the user interface
- `middleware`: Python code for ETL and data processing

```text
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

## Setup
The information below provides guidance on setting up a local development environment.

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

It is recommended that you set up a Python virtual environment: a self-contained directory that contains a Python interpreter and a set of installed packages. This isolates the dependencies required for a specific project, ensuring that changes in one project don’t affect others. For this application, I have selected the root `middleware` folder as the location for the virtual environment.

Create a virtual environment:   
```bash
python3 -m venv venv
```

Replace the second "venv" with your preferred name for the environment folder. I've chosen, "cpsenv".

Activate the virtual environment. Below are the Linux/macOS and Windows commands, respectively.

```text
source venv/bin/activate  

venv\Scripts\activate
```

If using the GitBash shell, use a slightly different command:
```text
source venv\Scripts\Activate
```

After activation, you’ll notice the environment name ((venv)) appears in your terminal prompt. You can also invoke Python with the command, `python` (as opposed to `python3`).

You can then install packages as normal using `pip` or install all packages from `requirements.txt`.

To activate an environment and install from the `requirements.txt` file:
```text
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Local SQL Server Database
This one is a little more entailed, since it requires a Docker image that runs Microsoft SQL Server 2019 within an Ubuntu Linux OS. Refer to ChatGPT.com instructions for this.

### SQL Server Database Load
Once Docker and Microsft SQL Server are installed and running in a container, proceed to running the SQL scripts located in the `_dbscript\sqlserver\cdwwork` folder. Begin with the "create" scripts, and then run the "insert" scripts.

### Local SQLite Database
(this part not implemented yet)  

## Deployment
Use Docker to containerize the application and deploy it on a cloud provider.

## Contact
For questions or support, contact the MedInsight team at support@medinsight.com.