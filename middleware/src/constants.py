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
    SELECT div.DivisionIEN AS Division,
           sp.PatientIEN,
           sp.PatientSSN,       
           LEFT(sp.PatientLastName, 4) AS LName4,
           'I' AS InOutPatient,
           REPLACE(CONVERT(VARCHAR(10), pt.PatientTransferDateTime, 120), '-', '') AS PatXferDate,
           '' AS PrimaryCareTeam,
           sp.Gender,
           REPLACE(CONVERT(VARCHAR(10), sp.BirthDateTime, 120), '-', '') AS PatientBirthDate,
           '' AS Religion,
           CASE
               WHEN pa.EmploymentStatus = 'FULL TIME' THEN '1'
               WHEN pa.EmploymentStatus = 'PART TIME' THEN '2'
               WHEN pa.EmploymentStatus = 'RETIRED' THEN '5'
               ELSE '9'
           END AS EmpStatus,
           '1' AS HealthInsurance,
           '39' AS StateCode,
           '100' AS CountyCode,
           '12345' AS ZipCode,
           pt.Sta3n,
           '10' AS EligCode,
           sp.VeteranFlag,
           'N' AS Vietnam,
           'N' AS AgentOrange,
           '1' AS Radiation,
           'N' AS POW,
           '8' AS POSCode,
           '' AS MeansTest,
           '2' AS MaritalStatus,
           vs.Facility,
           '1321' AS Ward,
           '' AS Placeholder1,
           '' AS Placeholder2,
           '' AS Placeholder3,
           '' AS Placeholder4,
           '' AS Placeholder5,
           'N' AS EncounterSHAD,
           'N' AS PurpleHeart,
           'N' AS ObservationPt,
           'RET' AS PtCategory,
           pt.InpatientSID,
           pt.OrdinalNumber,
           pt.PatientSID,
           sp.PatientName
    FROM Inpat.PatientTransfer AS pt
    INNER JOIN SPatient.SPatient AS sp ON pt.PatientSID = sp.PatientSID
    INNER JOIN SPatient.SPatientAddress AS pa ON pt.PatientSID = pa.PatientSID
    INNER JOIN Dim.WardLocation AS wl ON pt.GainingWardLocationSID = wl.WardLocationSID
    INNER JOIN Dim.Division AS div ON wl.DivisionSID = div.DivisionSID
    INNER JOIN Dim.VistASite AS vs ON pt.Sta3n = vs.Sta3n
    WHERE pt.Sta3n = ?
        and pt.PatientTransferDateTime >= ?
        and pt.PatientTransferDateTime <= ?
    ORDER BY pt.PatientTransferDateTime;
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