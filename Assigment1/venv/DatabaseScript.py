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
        s = line.replace("Date:", "")
        print(s)
    if re.match("(.*)From:(.*)", line):
        s = line.replace("From:", "")
        print(s)
    if re.match("(.*)To:(.*)", line):
        s = line.replace("To:", "")
        print(s)
    if re.match("(.*)Subject:(.*)", line):
        s = line.replace("Subject:", "")
        print(s)
    if re.match("(.*)Mime-Version:(.*)", line):
        s = line.replace("Mime-Version:", "")
        print(s)
    if re.match("(.*)Content-Type:(.*)", line):
        s = line.replace("Content-Type:", "")
        print(s)
    if re.match("(.*)Content-Transfer-Encoding:(.*)", line):
        s = line.replace("Content-Transfer-Encoding:", "")
        print(s)
    if re.match("(.*)X-From:(.*)", line):
        s = line.replace("X-From:", "")
        print(s)
    if re.match("(.*)X-To::(.*)", line):
        s = line.replace("X-To:", "")
        print(s)
    if re.match("(.*)X-cc:(.*)", line):
        s = line.replace("X-cc:", "")
    if re.match("(.*)X-bcc:(.*)", line):
        s = line.replace("X-bcc:", "")
        print(s)
    if re.match("(.*)X-Folder::(.*)", line):
        s = line.replace("X-Folder:", "")
        print(s)
    if re.match("(.*)X-Origin:(.*)", line):
        s = line.replace("X-Origin:", "")
        print(s)
    if re.match("(.*)(X|x)-FileName:(.*)", line):
        s = line.replace("X-FileName:", "")
        print(s)
        print("\n")

#cursor.execute('SELECT * FROM Tbl_Emails')

#for row in cursor:
#    print('row = %r' % (row,))

