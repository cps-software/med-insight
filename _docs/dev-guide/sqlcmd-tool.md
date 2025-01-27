# sqlcmd utility

The sqlcmd utility lets you enter Transact-SQL statements, system procedures, and script files through various modes:

- At the command prompt
- In Query Editor in SQLCMD mode
- In a Windows script file
- In an operating system (cmd.exe) job step of a SQL Server Agent job

### Find out which version you have installed
There are two versions of sqlcmd:

- The go-mssqldb-based sqlcmd, sometimes styled as go-sqlcmd, a standalone tool you can download independently of SQL Server.
- The ODBC-based sqlcmd, available with SQL Server or the Microsoft Command Line Utilities, and part of the mssql-tools package on Linux.

To determine the version you have installed, run the following statement at the command line:

```bash
sqlcmd "--version"
```

If you're using the new version of sqlcmd (Go), the output is similar to the following example:
`Version: 1.3.1`

### Download and install sqlcmd
sqlcmd (Go) can be installed cross-platform, on Microsoft Windows, macOS, and Linux. 

Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

sqlcmd
```bash
brew install sqlcmd
```

### Azure Data Studio
To run SQLCMD statements in Azure Data Studio, select `Enable SQLCMD` from the editor toolbar.

### Usage
Usage:
  sqlcmd [flags]
  sqlcmd [command]

### Examples:
Install/Create, Query, Uninstall SQL Server:
  sqlcmd create mssql --accept-eula --using https://aka.ms/AdventureWorksLT.bak
  sqlcmd open ads
  sqlcmd query "SELECT @@version"
  sqlcmd delete

# View configuration information and connection strings
  sqlcmd config view
  sqlcmd config cs

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  config      Modify sqlconfig files using subcommands like "sqlcmd config use-context mssql"
  create      Install/Create SQL Server, Azure SQL, and Tools
  delete      Uninstall/Delete the current context
  help        Help about any command
  open        Open tools (e.g ADS) for current context
  query       Run a query against the current context
  start       Start current context
  stop        Stop current context

Use "sqlcmd [command] --help" for more information about a command.

## Login from Command Line
```bash
sqlcmd -S localhost:1433 -U sa
```
Then enter password for designated user.

## Instal ODBC Driver
This is needed (I believe) for the SQL Server module, pyodbc to work.

### Install the Microsoft ODBC driver for SQL Server (macOS)
To install Microsoft ODBC driver 18 for SQL Server on macOS, run the following commands:

```bash
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
HOMEBREW_ACCEPT_EULA=Y brew install msodbcsql18 mssql-tools18
```