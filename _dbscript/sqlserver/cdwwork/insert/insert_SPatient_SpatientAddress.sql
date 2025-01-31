/*
|--------------------------------------------------------------------------------
| insert_SPatient_SPatientAddress.sql
|--------------------------------------------------------------------------------
| Insert sample data into table:  SPatient.SpatientAddress
|
*/

-- Set the active database
USE CDWWork;
GO

-- Insert data into SPatient.SpatientAddress table
INSERT INTO SPatient.SpatientAddress
(
    SPatientAddressSID, PatientSID, PatientIEN, Sta3n, OrdinalNumber, AddressType, StreetAddress1, StreetAddress2, StreetAddress3, City, County, [State], StateSID, Zip, Zip4, PostalCode, EmploymentStatus
)
VALUES
(100010001, 160016001, 'PtIEN15401', 508, 1, 'HOME', '110 Main St', 'Apt 1', '', 'Atlanta', 'Dekalb', 'GA', NULL, '12345', '', '', 'FULL TIME'),
(100010002, 160016002, 'PtIEN15402', 508, 1, 'HOME', '110 Main St', 'Apt 2', '', 'Atlanta', 'Dekalb', 'GA', NULL, '12345', '', '', 'FULL TIME'),
(100010003, 160016003, 'PtIEN15403', 508, 1, 'HOME', '110 Main St', 'Apt 3', '', 'Atlanta', 'Dekalb', 'GA', NULL, '12345', '', '', 'PART TIME'),
(100010004, 160016004, 'PtIEN15404', 508, 1, 'HOME', '110 Main St', 'Apt 4', '', 'Atlanta', 'Dekalb', 'GA', NULL, '12345', '', '', 'RETIRED'),
(100010005, 160016005, 'PtIEN15405', 516, 1, 'HOME', '110 Main St', 'Apt 5', '', 'Atlanta', 'Dekalb', 'GA', NULL, '12345', '', '', 'RETIRED');
GO
