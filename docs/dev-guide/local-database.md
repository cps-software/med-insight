# Local Database

## MariaDB Setup and Use

### Local Installation
MariaDB is bundled with the XAMPP distribution. Once XAMPP is installed, Application Manager can be used to start, restart, stop, and configure the MariaDB database server. It can also be administered from the command line. I'll add info on this later.  

Note that MariaDB is 100% compatible as MySQL and uses the same commands, functions, interface, etc. So, I may sometimes use the term "MySQL", and at other times, "MariaDB".

The MariaDB executable is located at: `/Applications/XAMPP/bin`

To check the MariaDB version and start an interactive shell:
```bash
/Applications/XAMPP/bin/mariadb -v
```

To quit the inteactive shell:
```bash
\q
```

#### Add MariaDB to $PATH
To add visibility to the MariaDB (and other PHP) executables, update .zshrc to expand the $PATH environment variable:
```text
export PATH=/Applications/XAMPP/bin:$PATH
```

#### Start MariaDB to Administer
Launch MacOS app, manager-osx.  
This starts the MariaDB Application Manager.  
Start the desired servers

#### Set up a New MySQL User Account
When you start Mariadb without specifying a user or not including _sudo_, MariaDB starts up with your local Mac account as the user, e.g., `chuck@localhost`. If you prefix with _sudo_ and enter your local machine password, MariaDB starts up as `root@localhost`.  

Then, as the root user, you can create a new database user account.  
```text
sudo ./mariadb -v
Password: (my mac user sudo password)

MariaDB> create user 'myusername'@'localhost' identified by 'mypassword';
MariaDB> grant all on *.* to 'myusername'@'localhost';
```

#### Use New User Account
```text
./mariadb -h localhost -u myusername -p
Password: mypassword
```

#### Add Password to Root User
```text
./mariadb-admin -u root password {new-password}
```

After resetting the root password, you may need to cycle the MariaDB server.

#### Use New User Account
```text
./mariadb -h localhost -u root -p
Password: {root-password}
```

#### Useful MySQL Commands
MariaDB> SYSTEM -u [username] -p  
MariaDB> status  
MariaDB> show databases;  
MariaDB> use database;  
MariaDB> show tables;  
MariaDB> select [rest of statement];  
MariaDB> select database();  
MariaDB> describe [tablename];  
MariaDB> desc [tablename];  

Note: replace the terminating character "**;**" with "**\G**", to print results vertically, e.g.:
```bash
select * from table\G
```

### Create the AVWHIMS Database
The avwhims database is created via a set of SQL data definition language (DDL) scripts. To create the main database and tables that comprise the database, launch the MariaDB shell using the new user that was created, e.g., csylvester.  

Then, run each of the DDL scripts in order to create the database, tables, and sample data.

At the MariaDB command prompt, execute the following command to run a DDL script. You can use the full path, or a relative path from the diretory that you started MariaDB from.  

For example, if you started from `/Applications/XAMPP/htdocs/avwhims/_dbscript`, you can run:
```text
source ./create/script_file.sql
```

Otherwise, use a full absolute path, e.g.,:
```text
source [/full/path/file.sql]
```

#### Database Creation Scrpts
Run each of the following scripts in this order:

```text
source ./create/create_db_avwhims.sql

source ./create/create_tbl_user_account.sql
source ./insert/insert_row_user_account.sql

source ./create/create_tbl_user_profile.sql
source ./insert/insert_row_user_profile.sql
```

### How to Drop a Database Table
```sql
drop table table_name;
```