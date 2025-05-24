# T-SQL Cheatsheet
Once you start the `sqlcmd` interactive prompt (by running `sqlcmd` without the `-Q` or `-i` options), many commands can be executed directly from the prompt, as long as they are valid T-SQL commands or use `sqlcmd`-specific syntax. Here's how it works:

---

### Commands from the `sqlcmd` Interactive Prompt

1. **Select/Use a Database**  
   You can use the `USE` command to change the current database:
   ```sql
   USE <DatabaseName>;
   GO
   ```

2. **Query the Database**  
   Any valid T-SQL query can be run interactively:
   ```sql
   SELECT name FROM sys.databases;
   GO
   ```

3. **Check Database Status**  
   Run a query to check the status of databases:
   ```sql
   SELECT name, state_desc FROM sys.databases;
   GO
   ```

4. **List Tables in a Database**  
   Retrieve table names interactively:
   ```sql
   SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';
   GO
   ```

5. **List Schemas in a Database**  
   List schemas with a query:
   ```sql
   SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA;
   GO
   ```

6. **Get SQL Server Version**  
   Check the version of the SQL Server:
   ```sql
   SELECT @@VERSION;
   GO
   ```

7. **Check Active Connections**  
   Query for active connections:
   ```sql
   SELECT DB_NAME(dbid) AS DatabaseName, COUNT(dbid) AS NumberOfConnections FROM sys.sysprocesses GROUP BY dbid;
   GO
   ```

8. **Backup a Database**  
   You can run backup commands:
   ```sql
   BACKUP DATABASE <DatabaseName> TO DISK = '<FilePath>';
   GO
   ```

9. **Display Server Configuration**  
   Execute `sp_configure`:
   ```sql
   EXEC sp_configure;
   GO
   ```

---

### **Commands That Require a Preconfigured Script or Cannot Be Run in the Interactive Prompt**

The following require you to use command-line options (`-Q` or `-i`) when launching `sqlcmd` and cannot be initiated directly in the interactive prompt:

1. **Run a SQL Script File**  
   You cannot pass a script file (`-i`) directly from the prompt. Instead, you run:
   ```bash
   sqlcmd -S <ServerName> -U <Username> -P <Password> -i <ScriptFile.sql>
   ```

2. **Exit on Errors (`-b`)**  
   The `-b` option to terminate on errors is a startup option and cannot be toggled from the interactive prompt.

3. **Connect to a Database (`-S`, `-U`, `-P`)**  
   Connecting to a different server or changing authentication details must be done when launching `sqlcmd`.

---

### **Special `sqlcmd` Interactive Commands**

Inside the `sqlcmd` interactive prompt, there are also **sqlcmd-specific commands** that you can use:

1. **Switch Database Context**
   ```sql
   :use <DatabaseName>
   ```

2. **List Current Database**
   ```sql
   :listvar
   ```

3. **Exit the Interactive Session**
   ```sql
   :exit
   ```

4. **Run a Script File**
   You can run a script file directly from the prompt using:
   ```sql
   :r <FilePath>
   ```

5. **Set a Variable**
   Set a variable that can be used in T-SQL:
   ```sql
   :setvar MyVariable MyValue
   ```

6. **Print Variable Values**
   ```sql
   PRINT '$(MyVariable)';
   GO
   ```

---

### **Example Interactive Session**
```bash
sqlcmd -S localhost -U sa -P MySecurePassword
```

```plaintext
1> USE MyDatabase;
2> GO
1> SELECT name FROM sys.databases;
2> GO
1> BACKUP DATABASE MyDatabase TO DISK = 'C:\backup\MyDatabase.bak';
2> GO
1> :exit
```

---

In summary:

- Most **T-SQL commands** listed above can be executed interactively.
- Tasks like running a script (`-i`), exiting on errors (`-b`), or setting connection parameters (`-S`, `-U`, `-P`) must be configured when starting `sqlcmd`.