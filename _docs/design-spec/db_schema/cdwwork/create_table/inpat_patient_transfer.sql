/*
 * create_tbl_inpat_patient_transfer.sql
 *
 * This script was originally generated via Microsoft SQL Server Studio tool.
 * Original SQL Server Object: View [Inpat].[PatientTransfer]
 * The script has been modified to generate a comparable MySQL/MariaDB table.
 *
 */

-- set the active database
USE cdwwork;

-- create table
CREATE TABLE inpat_patient_transfer
(
  patient_transfer_sid bigint NOT NULL,
  patient_movement_ien varchar(50) NOT NULL,
  sta3n smallint NOT NULL,
  inpatient_sid bigint NULL,
  ordinal_number smallint NULL,
  patient_sid int NULL,
  patient_tansfer_date_time datetime NULL,
  patient_transfer_vista_error_date varchar(50) NULL,
  patient_transfer_date_time_transform_sid bigint NULL,
  patient_transfer_date_sid int NULL,
  mas_movement_type_sid int NULL,
  facility_movement_type_sid int NULL,
  transfer_institution_sid int NULL,
  gaining_ward_location_sid int NULL,
  room_bed_sid int NULL,
  primary_physician_staff_sid int NULL,
  asih_inpatient_sid bigint NULL,
  attending_physician_staff_sid int NULL,
  asih_sequence smallint NULL,
  entered_by_staff_sid int NULL,
  entered_on_date_time datetime NULL,
  last_edited_by_staff_sid int NULL,
  last_edited_on_date_time datetime NULL,
  mpcr_change_flag char(1) NULL,
  admit_date_time datetime NULL,
  admit_vista_error_date varchar(50) NULL,
  admit_date_time_transform_sid bigint NULL,
  discharge_date_time datetime NULL,
  discharge_vista_error_date varchar(50) NULL,
  discharge_date_time_transform_sid bigint NULL,
  losing_specialty_sid int NULL,
  losing_ward_location_sid int NULL,
  losing_ward_cdr smallint NULL,
  leave_days smallint NULL,
  pass_days smallint NULL,
  discharge_movement_flag char(1) NULL,
  transmit_flag char(1) NULL,
    INDEX
    (
      patient_transfer_sid
    ),
    INDEX
    (
      sta3n
    ),
    INDEX
    (
      inpatient_sid
    )
);