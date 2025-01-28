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
(120011001, 'IEN00001', 508, 120120001, NULL, 110011001, '2025-01-01 10:00:00', 'vista_error_date', 330033001, 101, 101, 101, -1, 2010001, 3010001, -1, 990000001, -1, 0, 60000001, '2025-01-01 09:00:00', 70000001, '2025-01-01 09:30:00', 'N', '2025-01-01 08:00:00', 'error_date', 99099001, NULL, 'error_date', 990099001, NULL, 201, 5, 3, 5, NULL, NULL),

(120011002, 'IEN00002', 508, 120120002, NULL, 110011002, '2025-01-02 11:00:00', 'vista_error_date', 330033002, 102, 102, 102, -1, 2010002, 3010002, -1, 990000001, -1, 1, 60000002, '2025-01-02 09:00:00', 70000002, '2025-01-02 09:30:00', 'N', '2025-01-02 08:00:00', 'error_date', 99099002, '2025-01-02 20:00:00', 'error_date', 990099002, NULL, 202, 4, 2, 5, 'N', 'N'),

(120011003, 'IEN00003', 508, 120120003, NULL, 110011003, '2025-01-02 13:22:04', NULL, NULL, 20250102, 1200000078, 1200000065, -1, 1200009001, 1200062221, -1, -1, -1, 0, 1621550001, '2025-01-02 13:22:05', 1621550001, '2025-01-02 13:22:25', 'N', '2025-01-01 08:01:30', NULL, NULL, NULL, NULL, NULL, 1200000184, 1200000145, 1211, 0, 0, NULL, NULL),

(120011004, 'IEN00004', 508, 120120004, NULL, 110011004, '2025-01-01 12:00:00', 'vista_error_date', 330033004, 104, 104, 104, -1, 2010004, 3010004, -1, 990000001, -1, 0, 60000004, '2025-01-01 09:00:00', 70000004, '2025-01-01 09:30:00', 'N', '2025-01-01 08:00:00', 'error_date', 99099004, NULL, 'error_date', 990099004, NULL, 203, 6, 1, 5, 'Y', 'Y'),

(120011005, 'IEN00005', 516, 120120005, NULL, 110011005, '2025-01-01 12:00:00', 'vista_error_date', 330033004, 104, 104, 104, -1, 2010004, 3010004, -1, 990000001, -1, 0, 60000004, '2025-01-01 09:00:00', 70000004, '2025-01-01 09:30:00', 'N', '2025-01-01 08:00:00', 'error_date', 99099004, NULL, 'error_date', 990099004, NULL, 203, 6, 1, 5, 'Y', 'Y');

GO
