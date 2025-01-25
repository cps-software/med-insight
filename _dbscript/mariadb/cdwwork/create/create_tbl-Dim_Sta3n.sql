/*
|--------------------------------------------------------------------------------
| create_tbl-Dim_Sta3n.sql
|--------------------------------------------------------------------------------
| Creating MariaDB table to simulate CDW SQL Server view:
|   [CDWWork].[Dim].[Stan]
|
*/

-- set the active database
USE CDWWork;

-- create table
CREATE TABLE Dim_Sta3n
(
Sta3n               smallint NOT  NULL,
Sta3nName           varchar(50)   NULL,
VISNPreFY15         smallint      NULL,
VISNFY16            smallint      NULL,
VISNFY17            smallint      NULL,
Active              char(1)       NULL,
NextSta3n           int           NULL,
TimeZone            varchar(100)  NULL,
SiteCode            varchar(100)  NULL,
RegionFY15          smallint      NULL,
DistrictNameFY16    varchar(100)  NULL,
DistrictNumberFY16  varchar(100)  NULL,
DistrictNameFY17    varchar(100)  NULL,
DistrictNumberFY17  varchar(100)  NULL,
City                varchar(100)  NULL,
StateSID            int           NULL,
    INDEX
    (
      Sta3n
    ),
    INDEX
    (
      Sta3nName
    )
);