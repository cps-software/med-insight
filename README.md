# Med-Insight
**Med-Insight** is an AI-powered, full-stack healthcare analytics application designed to help providers deliver safer, higher-quality care by transforming complex patient treatment data into actionable insights. The platform enables clinicians to easily assess outcomes, identify best practices, and monitor the effectiveness of care delivery across diverse treatment settings.

Built as an end-to-end solution, Med-Insight integrates data from multiple clinical systems, performs ETL (extract, transform, load) processing into a structured database or data warehouse, and applies advanced AI/ML techniques to uncover patterns, trends, and recommendations that support data-informed decision making at the point of care.

The application is developed using a modern, modular technology stack:

* **Frontend:** JavaScript and React for building a responsive, user-friendly web interface
* **Backend:** Node.js with Express to provide RESTful APIs and application logic
* **AI/ETL Layer:** Python for data extraction, transformation, analytics, and machine learning
* **Database:** SQL Server for external data and PostgreSQL for internal processing and analytics
* **Mock Services:** A mock layer simulates external systems and data sources to support product validation
* **Deployment:** Cloud infrastructure with support for containerization, CI/CD pipelines, and data storage

## Getting Started
To get started, clone this repository into a directory of your choice and navigate to the med-insight folder.

```txt
git clone https://github.com/cps-software/med-insight.git  
cd med-insight  
```

## Local Development Environment Setup
Each subsystem uses one or more technology. Refer to the README.md file within each of the subsystem root folders for information on local environment setup and development.  

## Application Architecture
### Subsystems
Med-Insight is comprised of the following subsystems:  

| Subsystem   | Description |
| ----------- | ----------- |
| app         | Parent folder for the Med-Insight application, with subfolders for each of the application layers (frontend, middleware, backend) |
| docs        | Design specifications, diagrams, and other useful information related to the Med-Insight application |
| mock        | Mock SQL database, Parquet files, REST service, and website that simulate data sources |

The figure below shows how each of the core Med-Insight system components interact to form the full system.  

┌───────────────────────────────────────┐  
└───────────────────────────────────────┘  
Figure 1: Static View

## Processing Flow
This section describes the end-to-end processing flow, from original data source, through ETL processing, to user-facing web application. Additional subsyste-specific specifications can be found in the respsctive subsystem folders.

The figure below shows how the system components collaborate to support the full end-to-end processing workflow.

┌───────────────────────────────────────┐  
└───────────────────────────────────────┘  
Figure 2: Dynamic View

## Deployment
Refer to the README.md file for each subsystem for information on how to build and deploy each component.  
