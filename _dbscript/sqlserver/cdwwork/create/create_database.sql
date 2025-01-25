/*
|--------------------------------------------------------------------------------
| create_database.sql
|--------------------------------------------------------------------------------
| Create CDWWork database based on VA CDW database
|
*/

-- Drop the database if it exists
IF EXISTS (SELECT * FROM sys.databases WHERE name = 'CDWWork')
BEGIN
    DROP DATABASE CDWWork;
END;
GO

-- Create the database
CREATE DATABASE CDWWork;
GO