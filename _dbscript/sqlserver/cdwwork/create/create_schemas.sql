/*
|--------------------------------------------------------------------------------
| create_schemas.sql
|--------------------------------------------------------------------------------
| Create all needed CDWWork schemas (schema owner: sa)
| List schemas: SELECT name AS SchemaName FROM sys.schemas ORDER BY name;
|
*/

USE CDWWork;
GO

-- Dimension/reference/lookup tables
CREATE SCHEMA Dim;
GO

-- Inpatient tables
CREATE SCHEMA Inpat;
GO

-- CDW Patient tables
CREATE SCHEMA SPatient;
GO
