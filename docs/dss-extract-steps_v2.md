# **DSS Extract Processing Flow Guide**

## **1. Overview**
This document provides a structured and instructive guide to the processing flow for generating DSS Extracts from the **CDWWork** database in the **CDW Data Warehouse**. The DSS extracts are produced monthly or on-demand and contain critical patient and treatment data.

## **2. DSS Extract Types**
The current set of DSS extracts includes:
- **ADM** - Admissions
- **BCM** - Barcode Medication Administration
- **CLI** - Clinic
- **ECS** - Event Capture
- **IVP** - IV
- **LAB** - Laboratory
- **LBB** - Blood Bank
- **MOV** - Physical Movement
- **PRE** - Prescription
- **PRO** - Prosthetics
- **RAD** - Radiology
- **SUR** - Surgery
- **TRT** - Treating Specialty Change
- **UDP** - Unit Dose

## **3. ETL Processing Flow**
The DSS Extracts are generated using the following structured ETL (Extract, Transform, Load) workflow.

### **Step 1: Connect to CDW**
1. Connect to the proper **SQL Server database server**.
2. Use the **CDWWork** database.

### **Step 2: Extract Data from the Patient Transfer Table**
1. Select **Patient Transfer** records for a given **VistA Station Number** and date range.
   - The system prompts the user to enter:
     - **VistA Station Number**
     - **Start date** (YYYYMMDD format)
     - **End date** (YYYYMMDD format)
2. Include only records classified as **Inpatient** or **Transfer** actions.
   - This classification is determined via a coded field within the **Patient Transfer table** or related foreign key tables.

### **Step 3: Transform Data by Joining Supporting Tables**
1. **Enhance** the Patient Transfer data by joining it with related tables using **primary/foreign key relationships**.
   - Data enrichment includes:
     - **Patient demographics** (e.g., age, gender)
     - **Treatment information**
     - **Veteran status**
     - **Employment status**
     - **Insurance status**
     - Other **relevant attributes**
2. **Perform data mapping & transformation** where needed.
   - Example: Employment status transformation
     - 'Employed Full-Time' → `1`
     - 'Employed Part-Time' → `2`
     - 'Retired' → `5`
     - 'Unknown' → `9`
3. **Validate data consistency and completeness** before proceeding.

### **Step 4: Load Transformed Data into the Extract Results Table**
1. Store the processed data into an **extract results table** corresponding to the extract type (e.g., **ADM, CLI**).
2. Insert a new record into the **extract log table** for auditing and tracking purposes.
   - The log includes:
     - **Primary key**
     - **Foreign key references**
     - **Creation date**
     - **Extract type**
     - **Username of the requesting user**
3. Ensure **error handling** is implemented for failed inserts or data anomalies.

### **Step 5: Generate an Extract Text File**
1. **Users can view all extract records** for a selected extract type within a specified date range.
2. **Select a specific extract record** to generate a text-based file.
3. **Formatting rules:**
   - Fields are **separated by caret (`^`)** characters.
   - Each record ends with a **tilde (`~`)** followed by a **newline**.

### **Step 6: Transmit Extract File to Target System**
1. Securely transfer the extract text file to the target system using:
   - **SFTP (Secure File Transfer Protocol)**
   - **Other approved secure transmission methods**
2. Implement **file integrity checks** post-transfer to ensure successful delivery.

### **Step 7: Support End-User Data Analysis & Visualization**
1. Provide access to extract data through **analytics and visualization tools**, such as:
   - **Microsoft SQL Server Management Studio (SSMS)**
   - **Azure Data Studio**
   - **Power BI**
   - **Excel with ODBC connections**
2. Implement role-based access control (RBAC) to **restrict access** to authorized users only.

---

## **4. Best Practices and Recommendations**
### **Data Quality and Integrity**
- Implement **data validation** rules to catch missing or invalid values.
- Ensure referential integrity when joining tables.
- Perform periodic audits on extract logs.

### **Performance Optimization**
- Index frequently queried columns.
- Use **batch processing** for large datasets.
- Optimize queries by leveraging **SQL execution plans**.

### **Security and Compliance**
- Encrypt sensitive data during transmission and at rest.
- Follow **HIPAA** and other applicable regulatory guidelines.
- Implement **audit trails** for all data extraction operations.

### **Automation and Monitoring**
- Schedule extracts using **SQL Server Agent Jobs** or **cron jobs**.
- Implement **email or log-based notifications** for failed extract jobs.
- Monitor **ETL performance metrics** using database performance tools.

---
## **5. Conclusion**
This document provides a structured ETL process for generating DSS extracts while incorporating best practices in **data integrity, performance, and security**. Proper adherence to this guide will ensure efficient and secure extract processing while enabling end-user access to critical analytics.

For further details or troubleshooting, contact the **ETL Operations Team**.

