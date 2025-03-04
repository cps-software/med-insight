/*
|--------------------------------------------------------------------------------
| Inpat.Inpatient.sql
|--------------------------------------------------------------------------------
| Insert test data
| InpatientSID => 1638001 series
|
*/

-- Set the active database
USE CDWWork;
GO

-- Insert data into the Inpat.Inpatient table
INSERT INTO Inpat.Inpatient
(
  InpatientSID, PTFIEN, Sta3n, PatientSID, MeansTestIndicator, PatientFirstName, AdmitDateTime, AdmitDateSID, AdmitSourceSID, AdmitEligibilitySID, TransferFromFacility, ASIHDays, AdmitMASMovementTypeSID, AdmitFacilityMovementTypeSID, AdmitFromInstitutionSID, AdmitWardLocationSID, AdmitRoomBedSID, AdmitDiagnosis, ProviderSID, HeadNeckCancerFlag, IonizingRadiationFlag, SHADFlag, PatientSSN, PseudoSSNReason, SSNVerificationStatus, GovernmentEmployeeFlag, SensitiveFlag, Age, BirthDateTime
)
VALUES
(1638001, 'PFIEN001', 508, 1001, 'MeansTestIndicator', 'Adam', '2025-01-01 03:30:25', 20250101, 8001, 3001, 508, 3, 100001, 100001, 100001, 2001, 100001, 'AdmitDiagnosis', 1001, 'N', 'N', 'N', '123456789', 'PseudoSSNReason', 'SSNVerificationStatus', 'N', 'N', 45, '1980-01-01 00:00:00'),

(1638002, 'PFIEN002', 508, 1002, 'MeansTestIndicator', 'Barry', '2025-01-02 11:11:06', 20250102, 8001, 3001, 508, 5, 100001, 100001, 100001, 2001, 100001, 'AdmitDiagnosis', 1002, 'N', 'N', 'N', '987654321', 'PseudoSSNReason', 'SSNVerificationStatus', 'N', 'N', 64, '1961-01-02 00:00:00'),

(1638003, 'PFIEN003', 508, 1003, 'MeansTestIndicator', 'Carol', '2025-01-02 13:22:30', 20250102, 8001, 3001, 508, 5, 100001, 100001, 100001, 2001, 100001, 'AdmitDiagnosis', 1003, 'N', 'N', 'N', '111111111', 'PseudoSSNReason', 'SSNVerificationStatus', 'N', 'N', 35, '1990-01-02 00:00:00'),

(1638004, 'PFIEN004', 508, 1004, 'MeansTestIndicator', 'Debby', '2025-01-01 12:25:06', 20250101, 8001, 3001, 508, 4, 100001, 100001, 100001, 2001, 100001, 'AdmitDiagnosis', 1004, 'N', 'N', 'N', '111112222', 'PseudoSSNReason', 'SSNVerificationStatus', 'N', 'N', 71, '1954-01-02 00:00:00'),

(1638005, 'PFIEN005', 508, 1005, 'MeansTestIndicator', 'Edward', '2025-01-03 12:35:30', 20250103, 8001, 3001, 508, 2, 100001, 100001, 100001, 2001, 100001, 'AdmitDiagnosis', 1005, 'N', 'N', 'N', '111111105', 'PseudoSSNReason', 'SSNVerificationStatus', 'N', 'N', 44, '1981-05-15 00:00:00'),

(1638006, 'PFIEN006', 508, 1006, 'MeansTestIndicator', 'Francine', '2025-01-02 09:01:06', 20250102, 8001, 3001, 508, 5, 100001, 100001, 100001, 2001, 100001, 'AdmitDiagnosis', 1006, 'N', 'N', 'N', '111111106', 'PseudoSSNReason', 'SSNVerificationStatus', 'N', 'N', 44, '1981-05-15 00:00:00');

GO
