/*
|--------------------------------------------------------------------------------
| insert_row-Spatient_Spatient.sql
|--------------------------------------------------------------------------------
| Insert sample data into table:  Spatient_Spatient
| Original CDW SQL Server object: CDWWork.SPatient.Spatient
|
*/

-- Set the active database
USE CDWWork;
GO

-- Insert data into the SPatient.SPatient table
INSERT INTO SPatient.SPatient
(
  PatientSID, PatientIEN, Sta3n, PatientName, PatientLastName, PatientFirstName, TestPatientFlag, CDWPossibleTestPatientFlag, VeteranFlag, PatientType, PatientTypeSID, PatientICN, ScrSSN, PatientSSN, PseudoSSNReason, SSNVerificationStatus, GovernmentEmployeeFlag, SensitiveFlag, Age, BirthDateTime, BirthVistaErrorDate, BirthDateTimeTransformSID, DeceasedFlag, DeathDateTime, DeathVistaErrorDate, DeathDateTimeTransformSID, DeathEnteredByStaffSID, DeathNotificationSource, DeathDocumentationType, DeathModifiedDateTime, DeathModifiedVistaErrorDate, DeathModifiedDateTimeTransformSID, DeathLastUpdatedByStaffSID, Gender, SelfIdentifiedGender, Religion, ReligionSID, MaritalStatus, MaritalStatusSID, CollateralSponsorPatientSID, CurrentEnrollmentSID, MeansTestStatus, CurrentMeansTestStatusSID, PeriodOfService, PeriodOfServiceSID, OperationDesertShieldRank, ODSRankType, ODSRecalledCode, ODSTreatmentDateTime, ODSTreatmentVistaErrorDate, ODSTreatmentDateTimeTransformSID, FederalAgencySID, FilipinoVeteranCode, ServiceConnectedFlag, Eligibility, EligibilityVACode, EligibilitySID, EligibilityStatus, EligibilityStatusDateTime, EligibilityStatusVistaErrorDate, EligibilityStatusDateTimeTransformSID, EligibilityVerificationSource, EligibilityVerificationMethod, EligibilityInterimDateTime, EligibilityInterimVistaErrorDate, EligibilityInterimDateTimeTransformSID, EligibilityEnteredStaffSID, IneligibleReason, IneligibleVAROReason, IneligibleCity, IneligibleStateSID, IneligibleDateTime, IneligibleVistaErrorDate, IneligibleDateTimeTransformSID, IneligibleSource, PatientMissingSource, PatientMissingDateTime, PatientMissingVistaErrorDate, PatientMissingDateTimeTransformSID, PatientMissingCity, PatientMissingStateSID, FugitiveFelonFlag, FFFEnteredDateTime, FFFEnteredVistaErrorDate, FFFEnteredDateTimeTransformSID, FFFEnteredStaffSID, FFFRemovedReason, FFFRemovedDateTime, FFFRemovedVistaErrorDate, FFFRemovedDateTimeTransformSID, FFFRemovedStaffSID, PatientEnteredByStaffSID, PatientEnteredCode, PatientEnteredRemark, PatientEnteredDateTime, PatientEnteredVistaErrorDate, PatientEnteredDateTimeTransformSID, DuplicateRecordStatus, DestinationMergePatientSID, PreferredInstitutionSID, PreferredInstitutionSource, EmergencyResponseIndicator, InsuranceCoverageFlag, MedicaidEligibleFlag, MedicaidNumber, MedicaidInquireDateTime, MedicaidInquireVistaErrorDate, MedicaidInquireDateTimeTransformSID, VeteranTransportationProgramFlag
)
VALUES
-- First Record
(110011001, 'IEN100001', 508, 'Adam Doe', 'Doe', 'Adam', 'N', 'N', 'Y', 'Regular', 101, 'ICN100001', '123-45-6789', '123-45-6789', 'None', 'Verified', 'N', 'N', 45, '1980-01-01', NULL, NULL, 'N', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'M', 'Male', 'Christian', 1, 'Single', 1, NULL, 1001, 'None', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2025-01-21', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),

-- Second Record
(110011002, 'IEN100002', 508, 'Barry Doe', 'Doe', 'Mary', 'N', 'N', 'Y', 'Regular', 102, 'ICN100002', '987-65-4321', '987-65-4321', 'None', 'Verified', 'N', 'N', 50, '1975-05-15', NULL, NULL, 'N', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'F', 'Female', 'Muslim', 2, 'Married', 2, NULL, 1002, 'None', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2025-01-21', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),

-- Third Record
(110011003, 'IEN100003', 516, 'Carol Doe', 'Carol', 'Doe', 'N', 'N', 'Y', 'Regular', 102, 'ICN100003', '987-65-4321', '987-65-4321', 'None', 'Verified', 'N', 'N', 50, '1975-05-15', NULL, NULL, 'N', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'F', 'Female', 'Muslim', 2, 'Married', 2, NULL, 1002, 'None', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2025-01-21', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
GO
