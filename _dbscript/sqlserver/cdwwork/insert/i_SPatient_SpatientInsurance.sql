/*
|--------------------------------------------------------------------------------
| insert_SPatient_SPatientInsurance.sql
|--------------------------------------------------------------------------------
| Insert sample data into table:  SPatient.SpatientInsurance
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
(900090001, 160016001, 'PtIEN15401', 'PtInsIEN0001', 508, 130001, 'RETIRED', '2021-01-02'),
(900090002, 160016002, 'PtIEN15402', 'PtInsIEN0002', 508, 130001, 'RETIRED', '2021-02-02'),
(900090003, 160016003, 'PtIEN15403', 'PtInsIEN0003', 508, 130001, 'FULL TIME', '2021-03-02'),
(900090004, 160016004, 'PtIEN15404', 'PtInsIEN0004', 508, 130001, 'PART TIME', '2021-04-02'),
(900090005, 160016005, 'PtIEN15405', 'PtInsIEN0005', 516, 130001, 'RETIRED', '2021-05-02');
GO
