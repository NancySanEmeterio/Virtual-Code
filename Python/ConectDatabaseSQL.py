import pyodbc
import pandas as pd


conn_str = (r'DRIVER={SQL Server};' r'SERVER=MXMCAS06;' r'DATABASE=sia1mxdb;' 
             r'Trusted_Connection=yes;')

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

storedProc = "exec PythonTest"
cursor.execute(storedProc)

row = cursor.fetchone()
while row:
    print(str(row[0]) + " : " + str(row[1] or '') )
    row = cursor.fetchone()
    
cursor.close()
conn.close()
