# Med-Insight
Med-Insight is a reference application that works with healthcare information to provide various services and insights. It demonstrates a fullstack, end-to-end processing flow for extracting data from multiple source systems, transforming and loading the data into a database, and performing backend processing and analytics.

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
| data-source | Mock SQL database, Parquet files, REST service, and website that simulate data sources |
| etl-process | Python-based ETL and medallion architecture data management functionality |
| web-app     | PHP-based web application that includes a dashboard and other functionality |

Figure: Static View

## Processign Flow
This section describes the end-to-end processing flow, from original data source, through ETL processing, to user-facing web application. Additional subsyste-specific specifications can be found in the respsctive subsystem folders.

Figure: Dynamic View

## Deployment
Add a section to each of the subsystem README files.  

_Old Text:_ For development purposes, each of the three components is run directly from the command line. The current focus is on the middleware component, which runs from a terminal command line, within the Python virtual environment that was created and activated.
