# constants.py

# Constants for SQL statements
SELECT_ALL_Dim_Sta3n = "SELECT * FROM Dim_Sta3n;"
SELECT_COLUMNS_Sta3n = "SELECT Sta3n, Sta3nName, TimeZone, City FROM Dim_Sta3n;"

SELECT_ALL_Spatient_Spatient = "SELECT * FROM Spatient_Spatient;"
SELECT_COLUMNS_Spatient_Spatient = "SELECT PatientSID, PatientIEN, Sta3n, PatientName FROM Spatient_Spatient;"

SELECT_INNER_JOIN_Spatient_Sta3n = "SELECT Spatient_Spatient.*, Dim_Sta3n.Sta3nName as Station FROM Spatient_Spatient INNER JOIN Dim_Sta3n ON SPatient_Spatient.Sta3n = Dim_Sta3n.Sta3n;"
