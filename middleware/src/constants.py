# constants.py
"""Constants for SLQ statements"""

import os                          # import entire module

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
GRAY = "\033[90m"
RESET = "\033[0m"

SELECT_ALL_Dim_Sta3n = """
    SELECT *
    FROM [CDWWork].[Dim].[Sta3n];
"""

SELECT_COLUMNS_Sta3n = """
    SELECT Sta3n,
           LEFT(Sta3nName, 50) AS Sta3nName,
           LEFT(TimeZone, 25) AS TimeZone,
           TRIM(LEFT(City, 30)) AS City
    FROM [CDWWork].[Dim].[Sta3n];
"""

SELECT_ALL_Spatient_Spatient = """
    SELECT * FROM Spatient_Spatient;
"""

SELECT_COLUMNS_Spatient_Spatient = "SELECT PatientSID, PatientIEN, Sta3n, PatientName FROM Spatient_Spatient;"

ADM_SEQUENCE_NUMBER = '552ADM'
ADM_YEAR_MONTH = '202501'
EXTRACT_NUMBER = '0072025'

ADM_QUERY_01 = """
    SELECT Dim.Division.DivisionIEN AS Division,
           Spatient.SPatient.PatientIEN,
           SPatient.Spatient.PatientSSN,       
           LEFT(SPatient.SPatient.PatientLastName, 4) AS LName4,
           'I' AS InOutPatientIndicator,
           REPLACE(CONVERT(VARCHAR(10), Inpat.PatientTransfer.PatientTransferDateTime, 120), '-', ''),
           '' AS PrimaryCareTeam,
           Spatient.Spatient.Gender,
           REPLACE(CONVERT(VARCHAR(10), Spatient.Spatient.BirthDateTime, 120), '-', ''),
           '' AS Religion,
           SPatient.SpatientInsurance.EmploymentStatus,
           '1' AS HealthInsurance,
           '39' AS StateCode,
           '100' AS CountyCode,
           '12345' AS ZipCode,
           Inpat.PatientTransfer.Sta3n,
           Dim.VistASite.Facility,
           Inpat.PatientTransfer.InpatientSID,
           Inpat.PatientTransfer.OrdinalNumber,
           Inpat.PatientTransfer.PatientSID,
           SPatient.Spatient.PatientName
    FROM Inpat.PatientTransfer
    INNER JOIN SPatient.SPatient ON Inpat.PatientTransfer.PatientSID = SPatient.Spatient.PatientSID
    INNER JOIN SPatient.SPatientInsurance ON Inpat.PatientTransfer.PatientSID = SPatient.SpatientInsurance.PatientSID
    INNER JOIN Dim.WardLocation ON Inpat.PatientTransfer.GainingWardLocationSID = Dim.WardLocation.WardLocationSID
    INNER JOIN Dim.Division ON Dim.WardLocation.DivisionSID = Dim.Division.DivisionSID
    INNER JOIN Dim.VistASite ON Inpat.PatientTransfer.Sta3n = Dim.VistASite.Sta3n
    WHERE Inpat.PatientTransfer.Sta3n = ?
        and Inpat.PatientTransfer.PatientTransferDateTime >= ?
        and Inpat.PatientTransfer.PatientTransferDateTime <= ?
    ORDER BY Inpat.PatientTransfer.PatientTransferDateTime;
"""

ADM_QUERY_02 = """
    SELECT Dim.Division.DivisionIEN,
           Spatient.Spatient.PatientSID,
           Spatient.SPatient.PatientIEN,
           LEFT(SPatient.SPatient.PatientLastName, 4) AS LName4,           
           Spatient.Spatient.Sta3n
    FROM Inpat.PatientTransfer

    INNER JOIN Spatient.Spatient ON Inpat.PatientTransfer.PatientSID = Spatient.Spatient.PatientSID
    INNER JOIN Dim.WardLocation ON Inpat.PatientTransfer.GainingWardLocationSID = Dim.WardLocation.WardLocationSID
    INNER JOIN Dim.Division ON Dim.WardLocation.DivisionSID = Dim.Division.DivisionSID

    WHERE Inpat.PatientTransfer.Sta3n = ?
        and Inpat.PatientTransfer.PatientTransferDateTime >= ?
        and Inpat.PatientTransfer.PatientTransferDateTime <= ?
    ORDER BY Inpat.PatientTransfer.PatientTransferDateTime;
"""

ADM_QUERY_03 = """
    SELECT SPatient.SPatient.PatientSID,
           SPatient.SPatient.PatientIEN,
           SPatient.SPatient.PatientName,
           CONVERT(VARCHAR(10), SPatient.SPatient.PatientEnteredDateTime, 120) AS PatientEnteredDateTime,
           SPatient.SPatient.Sta3n,
           Dim.Sta3n.Sta3nName
    FROM [CDWWork].[SPatient].[SPatient]
    INNER JOIN [CDWWork].[Dim].[Sta3n]
    ON SPatient.SPatient.Sta3n = Dim.Sta3n.Sta3n
    WHERE PatientEnteredDateTime > '2025-01-20'
    ORDER BY PatientSID;
"""