import pyodbc
import re
import matplotlib.pyplot as plt
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-PL894JS\SQLEXPRESS;"
                      "Database=Emails;"
                      "Trusted_Connection=yes;")

cursor = cnxn.cursor()
cursor.execute('SELECT [From] FROM Tbl_Emails')
From = []
x = 0
for i in cursor.fetchall():
    From.append(i[0])
    x = x+1
cursor.execute('SELECT [X-From] FROM Tbl_Emails')
XFrom = []
y = 0
for i in cursor.fetchall():
    XFrom.append(i[0])
    y = y+1
print(x)
print(y)

Names = []
sk = 0
ty = 0
for i in  From:
    try:
        if i.index(".") < i.index("@"):
            Names.append(i.split('.')[0])
            sk = sk+1
        else:
            Names.append(i.split('@')[0])
            sk =sk+1
    except ValueError:
            Names.append(i.split('@')[0])
            sk = sk+1;
indexX = 0
SuspeciousEmail = 0;
goodEmail = 0
for i in From:
    if  Names[indexX] in i:
       goodEmail = goodEmail+1
    else:
        print(i)
        print(Names[indexX])
        SuspeciousEmail = SuspeciousEmail+1

    indexX = indexX+1

print(SuspeciousEmail)
print(goodEmail)