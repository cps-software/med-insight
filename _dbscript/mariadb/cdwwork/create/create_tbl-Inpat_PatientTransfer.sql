/*
|--------------------------------------------------------------------------------
| create_tbl-Inpat_PatientTransfer.sql
|--------------------------------------------------------------------------------
| Creating MariaDB table to simulate CDW SQL Server view:
|   [CDWWork].[Inpat].[PatientTransfer]
|
*/

-- set the active database
USE CDWWork;

-- create table
CREATE TABLE Inpat_PatientTransfer
(
  PatientTransferSID          bigint NOT NULL,
  PatientMovementIEN          varchar(50) NOT NULL,
  Sta3n                       smallint NOT NULL,
  InpatientSID                bigint NULL,
  OrdinalNumber smallint NULL,
  PatientSID int NULL,
  PatientTransferDateTime datetime NULL,
  PatientTransferVistaErrorDate varchar(50) NULL,
  PatientTransferDateTimeTransformSID bigint NULL,
  PatientTransferDateSID int NULL,
  MASMovementTypeSID int NULL,
  FacilityMovementTypeSID int NULL,
  TransferInstitutionSID int NULL,
  GainingWardLocationSID int NULL,
  RoomBedSID int NULL,
  PrimaryPhysicianStaffSID int NULL,
  ASIHInpatientSID bigint NULL,
  AttendingPhysicianStaffSID int NULL,
  ASIHSequence smallint NULL,
  EnteredByStaffSID int NULL,
  EnteredOnDateTime datetime NULL,
  LastEditedByStaffSID int NULL,
  LastEditedOnDateTime datetime NULL,
  MPCRChangeFlag char(1) NULL,
  AdmitDateTime datetime NULL,
  AdmitVistaErrorDate varchar(50) NULL,
  AdmitDateTimeTransformSID bigint NULL,
  DischargeDateTime datetime NULL,
  DischargeVistaErrorDate varchar(50) NULL,
  DischargeDateTimeTransformSID bigint NULL,
  LosingSpecialtySID int NULL,
  LosingWardLocationSID int NULL,
  LosingWardCDR smallint NULL,
  LeaveDays smallint NULL,
  PassDays smallint NULL,
  DischargeMovementFlag char(1) NULL,
  TransmitFlag char(1) NULL,
    INDEX
    (
      PatientTransferSID
    ),
    INDEX
    (
      Sta3n
    ),
    INDEX
    (
      InpatientSID
    )
);