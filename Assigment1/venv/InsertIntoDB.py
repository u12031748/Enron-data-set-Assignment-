import pyodbc
import re
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-PL894JS\SQLEXPRESS;"
                      "Database=Emails;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
#cursor.execute('SELECT * FROM Tbl_Emails')
myGlobal = 0
MessageID =""
Date =""
From =""
To =""
Subject =""
Cc =""
MimeVersion =""
ContentType =""
ContentTransferEncoding =""
Bcc =""
XFrom =""
XTo =""
Xcc =""
Xbcc =""
XFolder =""
XOrigin =""
XFileName= ""
file = open('C:\\Users\\Khumalo\\Desktop\\Enron emails\\testfile.txt', 'r')

for line in file:
    if re.match("(.*)Message-ID:(.*)", line):
        myGlobal = 1
        MessageID = line.replace("Message-ID:", "")

    if re.match("(.*)Date:(.*)", line):
        myGlobal = 2
        Date = line.replace("Date:", "")

    if re.match("From:(.*)", line):
        myGlobal = 3
        From = line.replace("From:", "")

    if re.match("To:(.*)", line):
        myGlobal = 4
        To = line.replace("To:", "")

    if re.match("(.*)Subject:(.*)", line):
        myGlobal = 5
        Subject = line.replace("Subject:", "")

    if re.match("(.*)Mime-Version:(.*)", line):
        myGlobal = 6
        MimeVersion = line.replace("Mime-Version:", "")

    if re.match("(.*)Content-Type:(.*)", line):
        myGlobal = 7
        ContentType = line.replace("Content-Type:", "")

    if re.match("(.*)Content-Transfer-Encoding:(.*)", line):
        myGlobal = 8
        ContentTransferEncoding = line.replace("Content-Transfer-Encoding:", "")

    if re.match("(.*)X-From:(.*)", line):
        myGlobal = 9
        XFrom = line.replace("X-From:", "")

    if re.match("(.*)X-To:(.*)", line):
        myGlobal = 10
        XTo = line.replace("X-To:", "")

    if re.match("(.*)X-cc:(.*)", line):
        myGlobal = 11
        Xcc = line.replace("X-cc:", "")
    if re.match("(.*)X-bcc:(.*)", line):
        myGlobal = 12
        Xbcc = line.replace("X-bcc:", "")

    if re.match("(.*)X-Folder:(.*)", line):
        myGlobal = 13
        XFolder = line.replace("X-Folder:", "")

    if re.match("(.*)X-Origin:(.*)", line):
        myGlobal = 14
        XOrigin = line.replace("X-Origin:", "")

    if re.match("(.*)Cc:(.*)", line):
        myGlobal = 16
        Cc = line.replace("Cc:", "")

    if re.match("(.*)X-FileName:(.*)", line):
        myGlobal = 15
        XFileName = line.replace("X-FileName:", "")
        cursor.execute("INSERT INTO Tbl_Emails([Message-ID],Date,[From],[To],Subject,Cc,[Mime-Version],[Content-Type],[Content-Transfer-Encoding],Bcc,"
                      "[X-From],[X-To],[X-cc],[X-bcc],[X-Folder],[X-Origin],[X-FileName]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                       "",MessageID,Date,From,To,Subject,Cc,MimeVersion,ContentType,ContentTransferEncoding,Bcc,XFrom,XTo,Xcc,Xbcc,XFolder,XOrigin,XFileName);
        cursor.commit();


#cursor.execute('SELECT * FROM Tbl_Emails')

#for row in cursor:
#    print('row = %r' % (row,))

