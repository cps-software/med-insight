-- Query to get structure for a SQL Server View
--
-- Returns:
-- Column Name | Type | Computed | Length | Prec | Scale | Nullable | Trim Blanks | 2 more fields 
--
-- For db create script, I trimmed to:
-- Column Name | Type | Length | Nullable | Trim Blanks | 2 more fields 

exec sp_help 'Spatient.Spatient';