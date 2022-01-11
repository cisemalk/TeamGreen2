import pyodbc
import random
import string

server = 'teamgreenserver.database.windows.net'
database = 'teamgreendatabase'
username = 'Teamgreensql'
password = 'DkKSDEGmdo29.21'
driver = '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=tcp:' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
    with conn.cursor() as cursor:
        cursor.execute('''DROP TABLE IF EXISTS tblEmployee
        CREATE TABLE tblEmployee(
        	[EmpName] nvarchar(20),
        	[EmpSurname] nvarchar(20),
        	[EmpAddress] nvarchar(20),
        	EmpPhone int
        )
        
        ''')
        i = 0
        while i <= 50:
            cursor.execute("""INSERT INTO tblEmployee(EmpName, EmpSurname, EmpAddress, EmpPhone) VALUES ('a','b', 'c',41)
            """)
            i += 1
