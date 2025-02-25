# constants_sql_rad.py
"""Constants for SLQ statements"""

RAD_QUERY_01 = """
    --
    -- This version of the query is based on the CDW RadiologyNuclearMedicineReport table
    -- Make sure you have selected CDWWork as the active database
    -- There are several JOINS to other tables, mostly based on PatientSID
    -- Before running, replace the three ? placeholder values in the WHERE clause
    -- For example: '508', '2025-01-01', and '2025-01-03'
    --

    SELECT
        -- d.DivisionIEN AS Division,
        '1' AS DivIEN,
        p.PatientIEN,
        p.PatientSSN,       
        -- LEFT(SPatient.SPatient.PatientLastName, 4) AS LName4,
        'I' AS InOutPatient,
        -- REPLACE(CONVERT(VARCHAR(10), pt.PatientTransferDateTime, 120), '-', '') AS ProcedureDate,
        '55555' AS CPTCode,
        '99999' AS ProcedureCode,
        '11111' AS ImagingLocation,
        rnmr.RadiologyNuclearMedicineReportSID,
        rnmr.Sta3n,
        rnmr.ExamDateTime

    FROM SStaff.RadiologyNuclearMedicineReport AS rnmr

    INNER JOIN SPatient.SPatient AS p ON rnmr.PatientSID = p.PatientSID
    
    WHERE rnmr.Sta3n = ?
        and rnmr.ExamDateTime >= ?
        and rnmr.ExamDateTime <= ?

    ORDER BY rnmr.ExamDateTime;
"""