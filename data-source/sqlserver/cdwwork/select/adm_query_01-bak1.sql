SELECT  d.DivisionIEN AS Division,
        p.PatientIEN,
        p.PatientSSN,       
        LEFT(p.PatientLastName, 4) AS LName4,
        'I' AS InOutPatient,
        REPLACE(CONVERT(VARCHAR(10), pt.PatientTransferDateTime, 120), '-', '') AS PatXferDate,
        '' AS PrimaryCareTeam,
        p.Gender,
        REPLACE(CONVERT(VARCHAR(10), p.BirthDateTime, 120), '-', '') AS PatientBirthDate,
        '' AS Religion,
        -- Get and map Employment Status from Patient Address table
        CASE
            WHEN pa.EmploymentStatus = 'EMPLOYED FULL TIME' THEN '1'
            WHEN pa.EmploymentStatus = 'EMPLOYED PART TIME' THEN '2'
            WHEN pa.EmploymentStatus = 'NOT EMPLOYED' THEN '3'
            WHEN pa.EmploymentStatus = 'SELF EMPLOYED' THEN '4'
            WHEN pa.EmploymentStatus = 'RETIRED' THEN '5'
            WHEN pa.EmploymentStatus = 'ACTIVE MILITARY DUTY' THEN '6'
            ELSE '9'
        END AS AddressEmpStatus,
        -- Compare with Employment Status from Patient Insurance table
        -- This isn't working like I want it to, so commenting out
        --CASE
        --    WHEN pi.EmploymentStatus = 'FULL TIME' THEN '1'
        --    WHEN pi.EmploymentStatus = 'PART TIME' THEN '2'
        --    WHEN pi.EmploymentStatus = 'NOT EMPLOYED' THEN '3'
        --    WHEN pi.EmploymentStatus = 'SELF EMPLOYED' THEN '4'
        --    WHEN pi.EmploymentStatus = 'RETIRED' THEN '5'
        --    WHEN pi.EmploymentStatus = 'ACTIVE MILITARY' THEN '6'
        --    ELSE '9'
        --END AS InsuranceEmpStatus,
        '1' AS HealthInsurance,
        '39' AS StateCode,
        '100' AS CountyCode,
        pa.Zip4,
        pt.Sta3n,
        '10' AS EligCode,
        p.VeteranFlag,
        'N' AS Vietnam,
        'N' AS AgentOrange,
        '1' AS Radiation,
        'N' AS POW,
        p.PeriodOfService,
        '' AS MeansTest,
        -- Get and map Patient Marital Status
        CASE
            WHEN p.MaritalStatus = 'DIVORCED' THEN '1'
            WHEN p.MaritalStatus = 'MARRIED' THEN '2'
            WHEN p.MaritalStatus = 'WIDOWED' THEN '4'
            WHEN p.MaritalStatus = 'SEPARATED' THEN '5'
            WHEN p.MaritalStatus = 'NEVER MARRIED' THEN '6'               
            WHEN p.MaritalStatus = 'UNKNOWN' THEN '7'
            ELSE ''
        END AS MaritalStatus,
        wl.WardLocationIEN,
        'TrSpec' AS TreatingSpecialty,
        s.StaffIEN,
        '12345678' AS MovementFileNum,
        '' AS DRG,
        '' AS Placeholder30,
        '150001' AS Time,
        '' AS PcProvider,
        '' AS Race,
        'PriWardProv' AS PrimaryWardProvider,
        '' AS MPI,
        '' AS Placeholder36,
        '' AS Placeholder37,
        '' AS Placeholder38,
        '' AS Placeholder39,
        'N' AS EncounterSHAD,
        'N' AS PurpleHeart,
        'N' AS ObservationPt,
        'RET' AS PtCategory,
        pt.InpatientSID,
        pt.OrdinalNumber,
        pt.PatientSID,
        p.PatientName
FROM Inpat.PatientTransfer AS pt
INNER JOIN SPatient.SPatient AS p ON pt.PatientSID = p.PatientSID
INNER JOIN SPatient.SPatientAddress AS pa ON pt.PatientSID = pa.PatientSID
--INNER JOIN SPatient.SPatientInsurance AS pi ON pt.PatientSID = pi.PatientSID
INNER JOIN Dim.WardLocation AS wl ON pt.GainingWardLocationSID = wl.WardLocationSID
INNER JOIN Dim.Division AS d ON wl.DivisionSID = d.DivisionSID
INNER JOIN SStaff.SStaff AS s ON pt.AttendingPhysicianStaffSID = s.StaffSID
INNER JOIN Dim.VistASite ON pt.Sta3n = Dim.VistASite.Sta3n
WHERE
    -- Get latest Patient Address record per Ordinal Number via subquery
    pa.OrdinalNumber = (
        SELECT MAX(pa2.OrdinalNumber)
        FROM SPatient.SPatientAddress AS pa2
        WHERE pa2.PatientSID = pt.PatientSID 
    )
    --and
    -- Get latest Patient Insurance record per Ordinal Number via subquery
    -- This isn't working like I want it to, so commenting out
    --pi.PolicyEffectiveDate = (
    --    SELECT MAX(pi.PolicyEffectiveDate)
    --    FROM SPatient.SPatientInsurance AS pi2
    --    WHERE pi2.PatientSID = pt.PatientSID 
    --)
    and pt.Sta3n = ?
    and pt.PatientTransferDateTime >= ?
    and pt.PatientTransferDateTime <= ?
    
ORDER BY pt.PatientTransferDateTime;
