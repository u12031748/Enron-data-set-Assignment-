import pyodbc
import re
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-FGO9KMF;"
                      "Database=Emails;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Tbl_Emails')

file = open('C:\\Users\\Khumalo\\Desktop\\Enron emails\\testfile.txt', 'r')
for line in file:
    if re.match("(.*)Message-ID:(.*)", line):
        s = line.replace("Message-ID:", "")
        print(s)
    if re.match("(.*)Date:(.*)", line):
        s = line.replace("Message-ID:", "")
        print(s)
    if re.match("(.*)From:(.*)", line):
        s = line.replace("From:", "")
        print(s)
    if re.match("(.*)To:(.*)", line):
        s = line.replace("To:", "")
        print(s)
    if re.match("(.*)Message-ID:(.*)", line):
        s = line.replace("Message-ID:", "")
        print(s)
    if re.match("(.*)Message-ID:(.*)", line):
        s = line.replace("Message-ID:", "")
        print(s)
    if re.match("(.*)(X|x)-FileName:(.*)", line):
            print("\n")
            print("\n")
            break
#cursor.execute('SELECT * FROM Tbl_Emails')

#for row in cursor:
#    print('row = %r' % (row,))

