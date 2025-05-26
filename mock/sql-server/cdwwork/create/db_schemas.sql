/*
|--------------------------------------------------------------------------------
| db_schemas.sql
|--------------------------------------------------------------------------------
| Schema owner: sa
| List schemas: SELECT name AS SchemaName FROM sys.schemas ORDER BY name;
|
*/

USE CDWWork;
GO

-- create schema for Dimension (reference/lookup) tables
CREATE SCHEMA Dim;
GO

-- create schema for Inpatient tables
CREATE SCHEMA Inpat;
GO

-- create schema for SPatient tables
CREATE SCHEMA SPatient;
GO

-- create schema for SStaff tables
CREATE SCHEMA SStaff;
GO
