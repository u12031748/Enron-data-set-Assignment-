import email
import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-TJ11VHB;"
                      "Database=Emails;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()

f = open('C:\\Users\\i\\Google Drive\\Honours\\COS720\\Assignment\\maildir\\allen-p\\inbox\\1')
msg = email.message_from_file(f)
f.close()

parser = email.parser.HeaderParser()
headers = parser.parsestr(msg.as_string())

hlist = []

for h in headers.items():
 #   print (h[0])
    hlist.append(h[1])


#print(len(hlist))
#print(hlist)

cursor.execute("INSERT INTO Tbl_Emails (ID, Message-ID, Date, From, To, Subject, Mime-Version, Content-Type, Content-Transfer-Encoding, X-From, X-To, X-cc, X-bcc, X-Folder, X-Origin, X-FileName )VALUES ("+1+", "+hlist[0]+", "+hlist[1]+", "+hlist[2]+", "+hlist[3]+", "+hlist[4]+", "+hlist[5]+", "+hlist[6]+", "+hlist[7]+", "+hlist[8]+", "+hlist[9]+", "+hlist[10]+", "+hlist[11]+", "+hlist[12]+", "+hlist[13]+", "+hlist[14])+" )

for row in cursor:
    print('row = %r' % (row,))