import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-TJ11VHB;"
                      "Database=Emails;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Tbl_Emails')

for row in cursor:
    print('row = %r' % (row,))