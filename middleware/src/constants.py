# constants.py
"""Constants for SLQ statements"""

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
    SELECT Dim.VistASite.DistrictNumber,
           Inpat.PatientTransfer.PatientMovementIEN,
           SPatient.Spatient.PatientSSN,           
           LEFT(SPatient.SPatient.PatientLastName, 4),
           'I' AS InOutPatientIndicator,
           REPLACE(CONVERT(VARCHAR(10), Inpat.PatientTransfer.PatientTransferDateTime, 120), '-', ''),
           '' AS PrimaryCareTeam,
           Spatient.Spatient.Gender,
           REPLACE(CONVERT(VARCHAR(10), Spatient.Spatient.BirthDateTime, 120), '-', ''),
           '' AS Religion,
           'R' AS EmploymentStatus,
           Inpat.PatientTransfer.Sta3n,
           Dim.VistASite.Facility,
           Inpat.PatientTransfer.InpatientSID,
           Inpat.PatientTransfer.OrdinalNumber,
           Inpat.PatientTransfer.PatientSID,
           SPatient.Spatient.PatientName
    FROM Inpat.PatientTransfer
    INNER JOIN Dim.VistASite ON Inpat.PatientTransfer.Sta3n = Dim.VistASite.Sta3n
    INNER JOIN SPatient.SPatient ON Inpat.PatientTransfer.PatientSID = SPatient.Spatient.PatientSID
    WHERE Inpat.PatientTransfer.Sta3n = '508' and Inpat.PatientTransfer.PatientTransferDateTime > '2025-01-01'
    ORDER BY Inpat.PatientTransfer.PatientTransferDateTime;
"""

ADM_QUERY_02 = """
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