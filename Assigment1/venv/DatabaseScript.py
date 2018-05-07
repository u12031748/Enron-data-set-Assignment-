import pyodbc
import re
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-FGO9KMF;"
                      "Database=Emails;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Tbl_Emails')
myGlobal = 0
file = open('C:\\Users\\Khumalo\\Desktop\\Enron emails\\testfile.txt', 'r')
for line in file:
    if re.match("(.*)Message-ID:(.*)", line):
        myGlobal = 1
        s = line.replace("Message-ID:", "")

    if re.match("(.*)Date:(.*)", line):
        myGlobal = 2
        s = line.replace("Date:", "")

    if re.match("(.*)From:(.*)", line):
        myGlobal = 3
        s = line.replace("From:", "")

    if re.match("(.*)To:(.*)", line):
        myGlobal = 4
        s = line.replace("To:", "")

    if re.match("(.*)Subject:(.*)", line):
        myGlobal = 5
        s = line.replace("Subject:", "")

    if re.match("(.*)Mime-Version:(.*)", line):
        myGlobal = 6
        s = line.replace("Mime-Version:", "")

    if re.match("(.*)Content-Type:(.*)", line):
        myGlobal = 7
        s = line.replace("Content-Type:", "")

    if re.match("(.*)Content-Transfer-Encoding:(.*)", line):
        myGlobal = 8
        s = line.replace("Content-Transfer-Encoding:", "")

    if re.match("(.*)X-From:(.*)", line):
        myGlobal = 9
        s = line.replace("X-From:", "")

    if re.match("(.*)X-To:(.*)", line):
        myGlobal = 10
        s = line.replace("X-To:", "")

    if re.match("(.*)X-cc:(.*)", line):
        myGlobal = 11
        s = line.replace("X-cc:", "")
    if re.match("(.*)X-bcc:(.*)", line):
        myGlobal = 12
        s = line.replace("X-bcc:", "")

    if re.match("(.*)X-Folder::(.*)", line):
        myGlobal = 13
        s = line.replace("X-Folder:", "")

    if re.match("(.*)X-Origin:(.*)", line):
        myGlobal = 14
        s = line.replace("X-Origin:", "")

    if re.match("(.*)(X|x)-FileName:(.*)", line):
        myGlobal = 15
        s = line.replace("X-FileName:", "")


    if myGlobal == 1:
        cursor.execute("INSERT INTO Emails " "([Message-ID]) " "VALUES ("+s+")");
        connection.commit();
        id = cursor.fetchone()[0]
    if myGlobal == 2:
        #cursor.execute("INSERT INTO Emails " "([Message-ID]) " "VALUES ("+s+")");
        cursor.execute("UPDATE Emails SET Date: = ? WHERE [Message-ID] = ?", newcockpitdrillvalue, oldprimarykeyvalue)

        connection.commit();
    if myGlobal == 3:
        cursor.execute("INSERT INTO Emails " "([Message-ID]) " "VALUES ("+s+")");
        connection.commit();
    if myGlobal == 4:
        print(s)
    if myGlobal == 5:
        print(s)
    if myGlobal == 6:
        print(s)
    if myGlobal == 7:
        print(s)
    if myGlobal == 8:
        print(s)
    if myGlobal == 9:
        print(s)
    if myGlobal == 10:
        print(s)
    if myGlobal == 11:
        print(s)
    if myGlobal == 12:
        print(s)
    if myGlobal == 13:
        print(s)
    if myGlobal == 14:
        print(s)
    if myGlobal == 15:
        print(s)

#cursor.execute('SELECT * FROM Tbl_Emails')

#for row in cursor:
#    print('row = %r' % (row,))

