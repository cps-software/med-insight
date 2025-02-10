/*
|--------------------------------------------------------------------------------
| SPatient.SPatientAddress.sql
|--------------------------------------------------------------------------------
| Insert test data
| SpatientAddressSID => 1001 series
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
(1001, 1001, 'PtIEN15401', 508, 1, 'HOME', '110 Main St', 'Apt 1', '', 'Atlanta', 'Dekalb', 'GA', NULL, '30303', '303031001', '', 'EMPLOYED FULL TIME'),
(1002, 1002, 'PtIEN15402', 508, 1, 'HOME', '110 Main St', 'Apt 2', '', 'Atlanta', 'Dekalb', 'GA', NULL, '30303', '303031002', '', 'EMPLOYED FULL TIME'),
(1003, 1003, 'PtIEN15403', 508, 1, 'HOME', '110 Main St', 'Apt 3', '', 'Atlanta', 'Dekalb', 'GA', NULL, '30303', '303031003', '', 'EMPLOYED PART TIME'),
(1004, 1004, 'PtIEN15404', 508, 1, 'HOME', '110 Main St', 'Apt 4', '', 'Atlanta', 'Dekalb', 'GA', NULL, '30303', '303031004', '', 'RETIRED'),
(1005, 1005, 'PtIEN15405', 516, 1, 'HOME', '110 Main St', 'Apt 5', '', 'Atlanta', 'Dekalb', 'GA', NULL, '33744', '337441005', '', 'RETIRED'),
(1006, 1001, 'PtIEN15401', 508, 2, 'HOME', '110 Dogwood Dr', '', '', 'Atlanta', 'Fulton', 'GA', NULL, '30303', '303031001', '', 'EMPLOYED FULL TIME'),
(1007, 1001, 'PtIEN15401', 508, 3, 'HOME', '210 Dogwood Dr', '', '', 'Atlanta', 'Fulton', 'GA', NULL, '30303', '303031001', '', 'EMPLOYED FULL TIME');
GO
