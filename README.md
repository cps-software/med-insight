# MedInsight
MedInsight is a web-based application designed to analyze healthcare information and identify potential drug risks with a focus on female health concerns. The application combines the LAMP stack with AI/ML capabilities to deliver actionable insights.  

MedInsight provides a robust platform for examining medical records to identify potential drug risks, such as adverse reactions and drug-drug interactions, with a special focus on female health and related risks. The AI/ML component includes natural language processing (NLP) for understanding medical text and machine learning for risk prediction and pattern detection.

## Overview
MedInsight is a full-stack application comprising the following parts:
- **Frontend**: User interface components and client-side logic.
- **Backend**: Server-side logic and APIs.
- **AI/ML**: Machine learning and artificial intelligence components.
- **Docs**: Project documentation and user guides.

## Getting Started
To get started, clone this repository and navigate to the respective components (frontend, backend, ai_ml).

```bash
git clone https://github.com/cps-software/med-insight.git  
cd med-insight  
```

## Features
- User authentication and secure data management.
- AI-driven analysis of medical records.
- Dashboard with charts and tabular data.
- CRUD interface for tracking work progress.

## Folder Structure
- `backend`: Contains PHP backend scripts.
- `frontend`: Contains HTML, CSS, and JavaScript files for the user interface.
- `ai_ml`: Contains Python scripts for AI/ML processing.
- `docs`: Contains documentation files.

```text
MedInsight/
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
├── ai_ml/
│   ├── app/
│   │   ├── model.py
│   │   ├── preprocess.py
│   │   ├── risk_analysis.py
│   │   └── api.py
│   ├── requirements.txt
│   └── run.sh
├── docs/
│   └── README.md
├── .gitignore
└── README.md
```

## Setup
1. Configure the database using `backend/config/database.php`.
2. Serve the `frontend/index.html` file through a web server.
3. Run the AI/ML API by navigating to `ai_ml/` and executing:
   ```
   pip install -r requirements.txt
   bash run.sh
   ```
4. Access the application through the frontend URL.

## Deployment
Use Docker to containerize the application and deploy it on a cloud provider.

## Contact
For questions or support, contact the MedInsight team at support@medinsight.com.