# SQLCMD Cheatsheet
The `sqlcmd` utility is a command-line tool that allows users to interact with SQL Server databases using Transact-SQL (T-SQL). Below is a list of common commands and tasks that can be run from the command line using `sqlcmd`:

---

### 1. Connect to a Database
Use the `-S`, `-U`, and `-P` options to connect to a SQL Server instance.

```bash
sqlcmd -S <ServerName> -U <Username> -P <Password>
```

Example:  
```bash
sqlcmd -S localhost -U sa -P MySecurePassword
```

---

### 2. Select/Use a Database
Run T-SQL commands to select or use a specific database:

```bash
USE <DatabaseName>;
GO
```

Command Line Example:
```bash
sqlcmd -S localhost -U sa -P MySecurePassword -Q "USE MyDatabase; SELECT @@VERSION;"
```

---

### 3. Execute a SQL Script File
Run a `.sql` script file from the command line using the `-i` option.

```bash
sqlcmd -S <ServerName> -U <Username> -P <Password> -i <ScriptFile.sql>
```

Example:  
```bash
sqlcmd -S localhost -U sa -P MySecurePassword -i myscript.sql
```

---

### 4. Query the Database
Execute a T-SQL query using the `-Q` option.

```bash
sqlcmd -S <ServerName> -U <Username> -P <Password> -Q "<T-SQL Query>"
```

Example:  
```bash
sqlcmd -S localhost -U sa -P MySecurePassword -Q "SELECT name FROM sys.databases;"
```

---

### 5. Check Database Status
Get a list of all databases and their status:

```sql
SELECT name, state_desc FROM sys.databases;
```

Command Line Example:
```bash
sqlcmd -S localhost -U sa -P MySecurePassword -Q "SELECT name, state_desc FROM sys.databases;"
```

---

### **6. List Tables in a Database**
Get the list of tables in the current database:

```sql
SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';
```

Command Line Example:
```bash
sqlcmd -S localhost -U sa -P MySecurePassword -Q "SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';"
```

---

### **7. List Schemas in a Database**
Get the list of schemas:

```sql
SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA;
```

Command Line Example:
```bash
sqlcmd -S localhost -U sa -P MySecurePassword -Q "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA;"
```

---

### **8. Get SQL Server Version**
Retrieve the version of the SQL Server instance:

```sql
SELECT @@VERSION;
```

Command Line Example:
```bash
sqlcmd -S localhost -U sa -P MySecurePassword -Q "SELECT @@VERSION;"
```

---

### **9. Check Active Connections**
View active connections to the server:

```sql
SELECT DB_NAME(dbid) AS DatabaseName, COUNT(dbid) AS NumberOfConnections FROM sys.sysprocesses GROUP BY dbid;
```

Command Line Example:
```bash
sqlcmd -S localhost -U sa -P MySecurePassword -Q "SELECT DB_NAME(dbid) AS DatabaseName, COUNT(dbid) AS NumberOfConnections FROM sys.sysprocesses GROUP BY dbid;"
```

---

### **10. Backup a Database**
Run a T-SQL command to back up a database:

```sql
BACKUP DATABASE <DatabaseName> TO DISK = '<FilePath>';
```

Command Line Example:
```bash
sqlcmd -S localhost -U sa -P MySecurePassword -Q "BACKUP DATABASE MyDatabase TO DISK = 'C:\\backups\\MyDatabase.bak';"
```

---

### **11. Exit After a Command**
Add the `-b` option to exit immediately after an error.

Example:
```bash
sqlcmd -S localhost -U sa -P MySecurePassword -b -Q "SELECT 1/0;" # Will terminate on error
```

---

### **12. Display Server Configuration**
View SQL Server configurations:

```sql
EXEC sp_configure;
```

Command Line Example:
```bash
sqlcmd -S localhost -U sa -P MySecurePassword -Q "EXEC sp_configure;"
```

---

### **13. Help with `sqlcmd`**
For a full list of `sqlcmd` options:

```bash
sqlcmd -?
```

---

This list covers many common commands to manage and query SQL Server databases using `sqlcmd`. Let me know if you need examples for other tasks!
