/*
|--------------------------------------------------------------------------------
| SPatient.SPatientInsurance.sql
|--------------------------------------------------------------------------------
| Insert test data
| SPatientInsuranceSID => 1001 series
|
*/

-- Set the active database
USE CDWWork;
GO

-- Insert data into SPatient.SpatientInsurance table
INSERT INTO SPatient.SpatientInsurance
(
    SPatientInsuranceSID, PatientSID, PatientIEN, SPatientInsuranceIEN, Sta3n, InsuranceCompanySID, EmploymentStatus, RetirementDate
)
VALUES
(1001, 1001, 'PtIEN15401', 'PtInsIEN0001', 508, 130001, 'RETIRED', '2021-01-02'),
(1002, 1002, 'PtIEN15402', 'PtInsIEN0002', 508, 130001, 'RETIRED', '2021-02-02'),
(1003, 1003, 'PtIEN15403', 'PtInsIEN0003', 508, 130001, 'FULL TIME', '2021-03-02'),
(1004, 1004, 'PtIEN15404', 'PtInsIEN0004', 508, 130001, 'PART TIME', '2021-04-02'),
(1005, 1005, 'PtIEN15405', 'PtInsIEN0005', 516, 130001, 'RETIRED', '2021-05-02');
GO
