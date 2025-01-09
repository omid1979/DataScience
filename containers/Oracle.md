

sqlplus / as sysdba

## Create User :

CREATE USER myuser IDENTIFIED BY mypassword;
GRANT CREATE SESSION, CREATE TABLE, CREATE PROCEDURE TO myuser;
GRANT UNLIMITED TABLESPACE TO myuser;

##  Create Tables and Schema

CONNECT myuser/mypassword
CREATE TABLE mytable (
    id NUMBER PRIMARY KEY,
    name VARCHAR2(50)
);



Creating a Database from Scratch
If you are looking to create a new Oracle database from scratch, you typically use the DBCA tool or manual scripts. Here's a simplified overview of creating a database manually using SQL commands, but this is not typically done using the SYS account alone:

    Create a New Database:
        This involves creating the necessary files and structures, which is usually done during installation or with DBCA.
    Create Control Files:
        Use SQL commands to create control files, but this is typically automated.
    Create Data Files:
        Create data files for each tablespace.
    Create Redo Log Files:
        Create redo log files.
    Mount and Open the Database:
        Use SQL commands to mount and open the database.




-- Connect as SYSDBA
sqlplus / as sysdba

-- Mount the database
ALTER DATABASE MOUNT;

-- Open the database
ALTER DATABASE OPEN;


### show tables
SELECT table_name FROM user_tables;

SELECT table_name FROM all_tables WHERE owner = 'SYS';


