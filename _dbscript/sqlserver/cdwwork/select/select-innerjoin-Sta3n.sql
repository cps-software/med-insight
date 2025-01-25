-- Select with inner join

SELECT SPatient.SPatient.PatientSID,
       SPatient.SPatient.PatientIEN,
       SPatient.SPatient.PatientName,
       SPatient.SPatient.PatientEnteredDateTime,
       SPatient.SPatient.Sta3n,
       Dim.Sta3n.Sta3nName
FROM CDWWork.SPatient.SPatient 
INNER JOIN CDWWork.Dim.Sta3n 
ON SPatient.SPatient.Sta3n = Dim.Sta3n.Sta3n 
WHERE PatientEnteredDateTime > '2025-01-20'
ORDER BY PatientSID;