/*
|--------------------------------------------------------------------------------
| Inpat.PatientTransfer.sql
|--------------------------------------------------------------------------------
| Insert test data
| PatientTransferSID => 8001 series
|
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
(8001, 'IEN00001', 508, 11001101, NULL, 1001, '2025-01-01 10:10:05', 'vista_error_date', 330033001, 101, 101, 101, -1, 2001, 3010001, -1, 990000001, 1001, 0, 60000001, '2025-01-01 09:00:00', 70000001, '2025-01-01 09:30:00', 'N', '2025-01-01 08:00:00', 'error_date', 99099001, NULL, 'error_date', 990099001, NULL, 201, 5, 3, 5, NULL, NULL),

(8002, 'IEN00002', 508, 11001101, NULL, 1002, '2025-01-02 11:11:06', 'vista_error_date', 330033002, 102, 102, 102, -1, 2001, 3010002, -1, 990000001, 1001, 1, 60000002, '2025-01-02 09:00:00', 70000002, '2025-01-02 09:30:00', 'N', '2025-01-02 08:00:00', 'error_date', 99099002, '2025-01-02 20:00:00', 'error_date', 990099002, NULL, 202, 4, 2, 5, 'N', 'N'),

(8003, 'IEN00003', 508, 11001101, NULL, 1003, '2025-01-02 13:22:04', NULL, NULL, 20250102, 1200000078, 1200000065, -1, 2001, 1200062221, -1, -1, 1002, 0, 1621550001, '2025-01-02 13:22:05', 1621550001, '2025-01-02 13:22:25', 'N', '2025-01-01 08:01:30', NULL, NULL, NULL, NULL, NULL, 1200000184, 1200000145, 1211, 0, 0, NULL, NULL),

(8004, 'IEN00004', 508, 11001101, NULL, 1004, '2025-01-01 12:25:05', 'vista_error_date', 330033004, 104, 104, 104, -1, 2001, 3010004, -1, 990000001, 1002, 0, 60000004, '2025-01-01 09:00:00', 70000004, '2025-01-01 09:30:00', 'N', '2025-01-01 08:00:00', 'error_date', 99099004, NULL, 'error_date', 990099004, NULL, 203, 6, 1, 5, 'Y', 'Y'),

(8005, 'IEN00005', 508, 11001101, NULL, 1005, '2025-01-03 12:35:30', 'vista_error_date', 330033004, 105, 105, 105, -1, 2001, 3010004, -1, 990000001, 1002, 0, 60000004, '2025-01-01 09:00:00', 70000004, '2025-01-01 09:30:00', 'N', '2025-01-01 08:00:00', 'error_date', 99099004, NULL, 'error_date', 990099004, NULL, 203, 6, 1, 5, 'Y', 'Y'),

(8006, 'IEN00006', 516, 11001101, NULL, 1006, '2025-01-01 08:35:27', 'vista_error_date', 330033004, 106, 106, 106, -1, 2006, 3010004, -1, 990000001, 1001, 0, 60000001, '2025-01-01 09:10:10', 70000001, '2025-01-01 13:30:25', 'N', '2025-01-01 08:31:00', 'error_date', 99099004, NULL, 'error_date', 990099001, NULL, 201, 5, 1, 5, 'Y', 'Y'),

(8007, 'IEN00007', 516, 11001101, NULL, 1007, '2025-01-01 09:25:25', 'vista_error_date', 330033001, 106, 106, 106, -1, 2006, 3010001, -1, 990000001, 1001, 0, 60000001, '2025-01-01 09:11:12', 70000001, '2025-01-01 15:01:01', 'N', '2025-01-01 16:31:32', 'error_date', 99099004, NULL, 'error_date', 990099001, NULL, 201, 5, 1, 5, 'Y', 'Y');

GO
