/*
|--------------------------------------------------------------------------------
| insert_row-Inpat_PatientTransfer.sql
|--------------------------------------------------------------------------------
*/

-- Set the active database
USE CDWWork;
GO

-- Insert data into the Inpat.PatientTransfer table
INSERT INTO Inpat.PatientTransfer
(
  PatientTransferSID, PatientMovementIEN, Sta3n, InpatientSID, OrdinalNumber, PatientSID, PatientTransferDateTime, PatientTransferVistaErrorDate, PatientTransferDateTimeTransformSID, PatientTransferDateSID, MASMovementTypeSID, FacilityMovementTypeSID, TransferInstitutionSID, GainingWardLocationSID, RoomBedSID, PrimaryPhysicianStaffSID, ASIHInpatientSID, AttendingPhysicianStaffSID, ASIHSequence, EnteredByStaffSID, EnteredOnDateTime, LastEditedByStaffSID, LastEditedOnDateTime, MPCRChangeFlag, AdmitDateTime, AdmitVistaErrorDate, AdmitDateTimeTransformSID, DischargeDateTime, DischargeVistaErrorDate, DischargeDateTimeTransformSID, LosingSpecialtySID, LosingWardLocationSID, LosingWardCDR, LeaveDays, PassDays, DischargeMovementFlag, TransmitFlag
)
VALUES
-- First record
(120011001, 'IEN00001', 508, 120120001, NULL, 110011001, '2025-01-01 10:00:00', 'vista_error_date', 330033001, 101, 101, 
 101, -1, 2010001, 3010001, -1, 990000001, -1, 0, 60000001, '2025-01-01 09:00:00', 70000001, '2025-01-01 09:30:00', 'N', 
 '2025-01-01 08:00:00', 'error_date', 99099001, NULL, 'error_date', 990099001, NULL, 201, 5, 3, 5, NULL, NULL),

-- Second record
(120011002, 'IEN00002', 508, 120120002, NULL, 110011002, '2025-01-02 11:00:00', 'vista_error_date', 330033002, 102, 102, 
 102, -1, 2010002, 3010002, -1, 990000001, -1, 1, 60000002, '2025-01-02 09:00:00', 70000002, '2025-01-02 09:30:00', 'N', 
 '2025-01-02 08:00:00', 'error_date', 99099002, '2025-01-02 20:00:00', 'error_date', 990099002, NULL, 202, 4, 2, 5, 'N', 'N'),

-- Third record
(120011003, 'IEN00003', 516, 120120003, NULL, 110011003, '2025-01-03 12:00:00', 'vista_error_date', 330033003, 103, 103, 
 103, -1, 2010003, 3010003, -1, 990000001, -1, 0, 60000003, '2025-01-03 09:00:00', 70000003, '2025-01-03 09:30:00', 'N', 
 '2025-01-03 08:00:00', 'error_date', 99099003, NULL, 'error_date', 990099003, NULL, 203, 6, 1, 5, 'Y', 'Y');
GO
