# constants_sql_adm.py
"""Constants for SLQ statements"""

ADM_QUERY_00 = """
    --
    -- This query is based on the CDW Inpat.PatientTransfer table
    -- Make sure you have selected CDWWork as the active database
    -- Before running, replace the three ? placeholder values in the WHERE clause
    -- For example: 508, '2025-01-01', and '2025-01-03'
    --

    SELECT  d.DivisionIEN,
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

            '1' AS HealthInsurance,
            s2.VAStateCode,
            pa.County,   -- should this be a numeric coded value?
            pa.Zip4,
            p.EligibilityVACode,
            p.VeteranFlag,
            'N' AS Vietnam,
            pd.AgentOrangeExposureCode,
            pd.IonizingRadiationCode,
            pd.POWStatusCode,
            pos.PeriodOfServiceCode,
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
            'TreatSpec' AS TreatingSpecialty,
            s.StaffIEN,
            '12345678' AS MovementFileNum,
            '' AS PlaceholderDRG,
            '' AS Placeholder30,

            -- Get the time component of the PT DateTime field
            REPLACE(CONVERT(VARCHAR(8), pt.PatientTransferDateTime, 108), ':', '') AS PatXferTime,

            '' AS PcProvider,
            '' AS Race,
            'PriWardProv' AS PrimaryWardProvider,
            '' AS MPI,
            '' AS Placeholder36,
            '' AS Placeholder37,
            '' AS Placeholder38,
            '' AS Placeholder39,
            '10' AS AdmissionEligibility,
            'U' AS MSTStatus,
            pd.SHADFlag,
            '' AS Placeholder43,
            '' AS Placeholder44,

            -- Using p.Sta3n for now (determine if enrollment file needed)
            p.Sta3n AS EnrollmentLocation,

            '' AS Placeholder46,
            '' AS Placeholder47,
            '' AS Placeholder48,
            '' AS Placeholder49,
            'D' AS Dom,
            '?' AS EnrollmentCategory,
            '?' AS EnrollmentStatus,
            'N' AS EncounterSHAD,
            'N' AS PurpleHeart,
            'N' AS ObservationPt,
            pd.AgentOrangeLocation,
            pd.POWLocation,
            '' AS Placeholder62,
            '' AS Placeholder63,
            
            -- skipping down a bit...
            '' AS Placeholder70,
            pd.SWAsiaCode,
            pd.AgentOrangeExposureCode,  -- is this a duplicate?
            '' AS Placeholder82,
            s.NPI,
            '' AS Placeholder84,
            s.NPI,
            c.CountryCode,
            p.EligibilityStatus,

            pd.CampLejeuneFlag,

            -- skipping down a bit...
            '' AS PlaceholderCerner,
            p.PatientICN,
            p.SelfIdentifiedGender

    FROM Inpat.PatientTransfer AS pt

    INNER JOIN SPatient.SPatient AS p ON pt.PatientSID = p.PatientSID
    INNER JOIN SPatient.SPatientAddress AS pa ON pt.PatientSID = pa.PatientSID
    INNER JOIN Dim.State AS s2 ON s2.StateSID = pa.StateSID
    INNER JOIN Dim.Country AS c ON pa.CountrySID = c.CountrySID    
    INNER JOIN Spatient.SpatientDisability AS pd ON pt.PatientSID = pd.PatientSID
    INNER JOIN Dim.WardLocation AS wl ON pt.GainingWardLocationSID = wl.WardLocationSID
    INNER JOIN Dim.Division AS d ON wl.DivisionSID = d.DivisionSID
    INNER JOIN Dim.PeriodOfService AS pos ON p.PeriodOfServiceSID = pos.PeriodOfServiceSID
    INNER JOIN SStaff.SStaff AS s ON pt.AttendingPhysicianStaffSID = s.StaffSID
    INNER JOIN Dim.VistASite ON pt.Sta3n = Dim.VistASite.Sta3n

    WHERE
        -- Get latest Patient Address record per Ordinal Number via subquery
        pa.OrdinalNumber = (
            SELECT MAX(pa2.OrdinalNumber)
            FROM SPatient.SPatientAddress AS pa2
            WHERE pa2.PatientSID = pt.PatientSID 
        )
        and pt.Sta3n = ?
        and pt.PatientTransferDateTime >= ?
        and pt.PatientTransferDateTime < ?
        
    ORDER BY pt.PatientTransferDateTime;
"""

ADM_QUERY_01 = """
    --
    -- Get Patient Cohort and write selected data set to a temporary table
    -- Before running, replace the ? placeholder values in the WHERE clause
    -- For example: 508, '2025-01-01', and '2025-01-03'
    --
    SELECT
        pt.PatientSID,
        pt.PatientTransferDateTime,
        pt.GainingWardLocationSID,
        pt.Sta3n,
        pt.AttendingPhysicianStaffSID,
        pt.InpatientSID
    INTO ##AdmPatientCohort
    FROM Inpat.PatientTransfer AS pt
    WHERE pt.Sta3n = ?
        AND pt.PatientTransferDateTime >= ?
        AND pt.PatientTransferDateTime < ?;
"""

ADM_QUERY_02 = """
    --
    -- Check results from prior query
    --
    SELECT *
    FROM ##AdmPatientCohort;
"""

ADM_QUERY_03 = """
    --
    -- Join ##AdmPatientCohort with additional tables to get all ADM data elements
    -- Store result into an additional temporary table
    -- TO-DO: remove transformations from this transaction (do this later)
    --
    SELECT
        d.DivisionIEN,
        p.PatientIEN,
        p.PatientSSN,       
        p.PatientLastName,
        'I' AS InOutPatient,
        apc.PatientTransferDateTime,
        '' AS PrimaryCareTeam,
        p.Gender,
        p.BirthDateTime,
        '' AS Religion,
        pa.EmploymentStatus,
        '1' AS HealthInsurance,
        s2.VAStateCode,
        pa.County,   -- should this be a numeric coded value?
        pa.Zip4,
        p.EligibilityVACode,
        p.VeteranFlag,
        'N' AS Vietnam,
        pd.AgentOrangeExposureCode,
        pd.IonizingRadiationCode,
        pd.POWStatusCode,
        pos.PeriodOfServiceCode,
        '' AS MeansTest,
        p.MaritalStatus,
        wl.WardLocationIEN,
        'TreatSpec' AS TreatingSpecialty,
        s.StaffIEN,
        '12345678' AS MovementFileNum,
        '' AS PlaceholderDRG,
        '' AS Placeholder30,

        -- Extracting Time Component (move this logic to later query)
        -- REPLACE(CONVERT(VARCHAR(8), apc.PatientTransferDateTime, 108), ':', '') AS PatXferTime,

        '' AS PcProvider,
        '' AS Race,
        'PriWardProv' AS PrimaryWardProvider,
        '' AS MPI,
        '' AS Placeholder36,
        '' AS Placeholder37,
        '' AS Placeholder38,
        '' AS Placeholder39,
        '10' AS AdmissionEligibility,
        'U' AS MSTStatus,
        pd.SHADFlag,
        '' AS Placeholder43,
        '' AS Placeholder44,
        p.Sta3n AS EnrollmentLocation,  -- Using p.Sta3n for now (enrollment file needed?)
        '' AS Placeholder46,
        '' AS Placeholder47,
        '' AS Placeholder48,
        '' AS Placeholder49,
        'D' AS Dom,
        '?' AS EnrollmentCategory,
        '?' AS EnrollmentStatus,
        'N' AS EncounterSHAD,
        'N' AS PurpleHeart,
        'N' AS ObservationPt,
        pd.AgentOrangeLocation,

        pd.POWLocation,
        '' AS Placeholder62,
        '' AS Placeholder63,
            
        -- skipping down a bit...
        '' AS Placeholder70,
        pd.SWAsiaCode,

        -- duplicate below, so commenting out
        -- pd.AgentOrangeExposureCode,

        '' AS Placeholder82,
        s.NPI,
        '' AS Placeholder84,

        -- duplicate below, so commenting out
        -- s.NPI,

        c.CountryCode,
        p.EligibilityStatus,
        pd.CampLejeuneFlag,

        -- skipping down a bit...
        '' AS PlaceholderCerner,
        p.PatientICN,
        p.SelfIdentifiedGender AS SIGI
        
    INTO ##AdmPatientExtract

    FROM ##AdmPatientCohort AS apc

    INNER JOIN SPatient.SPatient AS p ON apc.PatientSID = p.PatientSID
    INNER JOIN SPatient.SPatientAddress AS pa ON apc.PatientSID = pa.PatientSID
    INNER JOIN Dim.State AS s2 ON s2.StateSID = pa.StateSID
    INNER JOIN Dim.Country AS c ON pa.CountrySID = c.CountrySID    
    INNER JOIN Spatient.SpatientDisability AS pd ON apc.PatientSID = pd.PatientSID
    INNER JOIN Dim.WardLocation AS wl ON apc.GainingWardLocationSID = wl.WardLocationSID
    INNER JOIN Dim.Division AS d ON wl.DivisionSID = d.DivisionSID
    INNER JOIN Dim.PeriodOfService AS pos ON p.PeriodOfServiceSID = pos.PeriodOfServiceSID
    INNER JOIN SStaff.SStaff AS s ON apc.AttendingPhysicianStaffSID = s.StaffSID
    INNER JOIN Dim.VistASite ON apc.Sta3n = Dim.VistASite.Sta3n

    WHERE
        -- Get latest Patient Address record per Ordinal Number via subquery
        pa.OrdinalNumber = (
            SELECT MAX(pa2.OrdinalNumber)
            FROM SPatient.SPatientAddress AS pa2
            WHERE pa2.PatientSID = apc.PatientSID 
        );
"""

ADM_QUERY_04 = """
    --
    -- Check results from prior query (unsorted)
    --
    SELECT *
    FROM ##AdmPatientExtract;
"""

ADM_QUERY_05 = """
    --
    -- Create final extract format (transform and sort)
    -- TO-DO: move all transformation and sorting logic (from query 3) here
    --
    SELECT
        DivisionIEN,
        PatientIEN,
        PatientSSN,       
        LEFT(PatientLastName, 4) AS LName4,
        InOutPatient,
        REPLACE(CONVERT(VARCHAR(10), PatientTransferDateTime, 120), '-', '') AS PatXferDate,
        PrimaryCareTeam,
        Gender,
        REPLACE(CONVERT(VARCHAR(10), BirthDateTime, 120), '-', '') AS PatientBirthDate,
        Religion,

        -- Employment Status Mapping
        CASE
            WHEN EmploymentStatus = 'EMPLOYED FULL TIME' THEN '1'
            WHEN EmploymentStatus = 'EMPLOYED PART TIME' THEN '2'
            WHEN EmploymentStatus = 'NOT EMPLOYED' THEN '3'
            WHEN EmploymentStatus = 'SELF EMPLOYED' THEN '4'
            WHEN EmploymentStatus = 'RETIRED' THEN '5'
            WHEN EmploymentStatus = 'ACTIVE MILITARY DUTY' THEN '6'
            ELSE '9'
        END AS AddressEmpStatus,

        HealthInsurance,
        VAStateCode,
        County,   -- should this be a numeric coded value?
        Zip4,
        EligibilityVACode,
        VeteranFlag,
        Vietnam,
        AgentOrangeExposureCode,
        IonizingRadiationCode,
        POWStatusCode,
        PeriodOfServiceCode,
        MeansTest,

        -- Marital Status Mapping
        CASE
            WHEN MaritalStatus = 'DIVORCED' THEN '1'
            WHEN MaritalStatus = 'MARRIED' THEN '2'
            WHEN MaritalStatus = 'WIDOWED' THEN '4'
            WHEN MaritalStatus = 'SEPARATED' THEN '5'
            WHEN MaritalStatus = 'NEVER MARRIED' THEN '6'
            WHEN MaritalStatus = 'UNKNOWN' THEN '7'
            ELSE ''
        END AS MaritalStatus,

        WardLocationIEN,
        TreatingSpecialty,
        StaffIEN,
        MovementFileNum,
        PlaceholderDRG,
        Placeholder30,

        -- Extracting Time Component
        REPLACE(CONVERT(VARCHAR(8), PatientTransferDateTime, 108), ':', '') AS PatXferTime,

        PcProvider,
        Race,
        PrimaryWardProvider,
        MPI,
        Placeholder36,
        Placeholder37,
        Placeholder38,
        Placeholder39,
        AdmissionEligibility,
        MSTStatus,
        SHADFlag,
        Placeholder43,
        Placeholder44,
        EnrollmentLocation,  -- Using p.Sta3n for now (enrollment file needed?)
        Placeholder46,
        Placeholder47,
        Placeholder48,
        Placeholder49,
        Dom,
        EnrollmentCategory,
        EnrollmentStatus,
        EncounterSHAD,
        PurpleHeart,
        ObservationPt,
        AgentOrangeLocation,
        POWLocation,
        Placeholder62,
        Placeholder63,
            
        -- skipping down a bit...
        Placeholder70,
        SWAsiaCode,

        -- duplicate below, so commenting out
        -- pd.AgentOrangeExposureCode,

        Placeholder82,
        NPI,
        Placeholder84,

        -- duplicate below, so commenting out
        -- s.NPI,

        CountryCode,
        EligibilityStatus,
        CampLejeuneFlag,

        -- skipping down a bit...
        PlaceholderCerner,
        PatientICN,
        SIGI
        
    FROM ##AdmPatientExtract
    ORDER BY PatXferDate;
"""
