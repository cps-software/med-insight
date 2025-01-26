# constants.py

# Constants for SQL statements
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

SELECT_ALL_Spatient_Spatient = "SELECT * FROM Spatient_Spatient;"
SELECT_COLUMNS_Spatient_Spatient = "SELECT PatientSID, PatientIEN, Sta3n, PatientName FROM Spatient_Spatient;"

SELECT_INNER_JOIN_Spatient_Sta3n = """
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