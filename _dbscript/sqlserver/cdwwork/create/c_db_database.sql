/*
|--------------------------------------------------------------------------------
| c_db_database.sql
|--------------------------------------------------------------------------------
*/

-- Drop database if it exists
IF EXISTS (SELECT * FROM sys.databases WHERE name = 'CDWWork')
BEGIN
    DROP DATABASE CDWWork;
END;
GO

-- Create database
CREATE DATABASE CDWWork;
GO
