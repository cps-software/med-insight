/*
 * create_view_inpat_patienttransfer.sql
 *
 * This script was originally generated via Microsoft SQL Server Studio tool.
 * Original SQL Server Object: View [Inpat].[PatientTransfer]
 *
 * The script has been modified to be compatible with MySQL/MariaDB syntax.
 * The script creates a table, as opposed to a view.
 *
 */

-- set the active database
USE cdwwork;

-- create table
CREATE VIEW [Inpat].[PatientTransfer]
AS  -- View: Inpat.PatientTransfer_v019, Table: Inpat.PatientTransfer_v086
Select 
  a.PatientTransferSID as PatientTransferSID
  , a.PatientMovementIEN as PatientMovementIEN
  , a.Sta3n as Sta3n
  , a.InpatientSID as InpatientSID
  , a.OrdinalNumber as OrdinalNumber
  , a.PatientSID as PatientSID
  , a.PatientTransferDateTime as PatientTransferDateTime
  , a.PatientTransferVistaErrorDate as PatientTransferVistaErrorDate
  , a.PatientTransferDateTimeTransformSID as PatientTransferDateTimeTransformSID
  , a.PatientTransferDateSID as PatientTransferDateSID
  , a.MASMovementTypeSID as MASMovementTypeSID
  , a.FacilityMovementTypeSID as FacilityMovementTypeSID
  , a.TransferInstitutionSID as TransferInstitutionSID
  , a.WardLocationSID as GainingWardLocationSID
  , a.RoomBedSID as RoomBedSID
  , a.PrimaryPhysicianStaffSID as PrimaryPhysicianStaffSID
  , a.ASIHInpatientSID as ASIHInpatientSID
  , a.AttendingPhysicianStaffSID as AttendingPhysicianStaffSID
  , a.ASIHSequence as ASIHSequence
  , a.EnteredByStaffSID as EnteredByStaffSID
  , a.EnteredOnDateTime as EnteredOnDateTime
  , a.LastEditedByStaffSID as LastEditedByStaffSID
  , a.LastEditedOnDateTime as LastEditedOnDateTime
  , a.MPCRChangeFlag as MPCRChangeFlag
  , a.AdmitDateTime as AdmitDateTime
  , a.AdmitVistaErrorDate as AdmitVistaErrorDate
  , a.AdmitDateTimeTransformSID as AdmitDateTimeTransformSID
  , a.DischargeDateTime as DischargeDateTime
  , a.DischargeVistaErrorDate as DischargeVistaErrorDate
  , a.DischargeDateTimeTransformSID as DischargeDateTimeTransformSID
  , a.LosingSpecialtySID as LosingSpecialtySID
  , a.LosingWardLocationSID as LosingWardLocationSID
  , a.LosingWardCDR as LosingWardCDR
  , a.LeaveDays as LeaveDays
  , a.PassDays as PassDays
  , a.DischargeMovementFlag as DischargeMovementFlag
  , a.TransmitFlag as TransmitFlag
From CDW14.Inpat.PatientTransfer_v086 AS a
Where 1=1

-- Automatic filtering:
AND a.OpCode <> 'X' -- Always filter out OpCode = X 
AND a.OpCode <> 'D' -- Filter for Work and PDWNext views

-- Set the WorkView version
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Physical table: PatientTransfer_v086' , @level0type=N'SCHEMA',@level0name=N'Inpat', @level1type=N'VIEW',@level1name=N'PatientTransfer'
GO

EXEC sys.sp_addextendedproperty @name=N'TableVersion', @value=86 , @level0type=N'SCHEMA',@level0name=N'Inpat', @level1type=N'VIEW',@level1name=N'PatientTransfer'
GO

EXEC sys.sp_addextendedproperty @name=N'ViewVersion', @value=19 , @level0type=N'SCHEMA',@level0name=N'Inpat', @level1type=N'VIEW',@level1name=N'PatientTransfer'
GO


