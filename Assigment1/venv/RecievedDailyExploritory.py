import pyodbc
import re
import matplotlib.pyplot as plt
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-PL894JS\SQLEXPRESS;"
                      "Database=Emails;"
                      "Trusted_Connection=yes;")

cursor = cnxn.cursor()
#Mon
mon = cursor.execute('SELECT Mon FROM TblRecievedMon')
rowMon = mon.fetchone()
rowAsList = [x for x in rowMon]
for i in rowAsList:
  Monday = i
#Tues
Tue = cursor.execute('SELECT Tue FROM TblRecievedTue')
rowTue = mon.fetchone()
TueRowAsList = [x for x in rowTue]
for i in TueRowAsList:
  Tuesday = i


#Wed
Wed = cursor.execute('SELECT Wed FROM TblRecievedWed')
rowWed = Wed.fetchone()
WedRowAsList = [x for x in rowWed]
for i in WedRowAsList:
  Wednesday = i

#Thu
Thu = cursor.execute('SELECT Thu FROM TblRecievedThu')
rowThu = Thu.fetchone()
ThuRowAsList = [x for x in rowThu]
for i in ThuRowAsList:
  Thursday = i

#Fri
Fri = cursor.execute('SELECT Fri FROM TblRecievedFri')
rowFri = mon.fetchone()
FriRowAsList = [x for x in rowFri]
for i in FriRowAsList:
  Friday = i
#Sat
Sat = cursor.execute('SELECT Sat FROM TblRecievedSat')
rowSat = mon.fetchone()
SatRowAsList = [x for x in rowSat]
for i in SatRowAsList:
  Satarday = i
#Sun
Sun = cursor.execute('SELECT Sun FROM TblRecievedSun')
rowSun = mon.fetchone()
SunRowAsList = [x for x in rowSun]
for i in SunRowAsList:
  Sunday = i

print(Monday, Tuesday, Wednesday,Thursday,Friday,Satarday,Sunday)

#plt.plot(["Mon","Tues","Wed","Thu","Fri","Sat","Sun"],[Monday, Tuesday, Wednesday,Thursday,Friday,Satarday,Sunday])
#plt.ylabel('Number of Emails recieved daily')
#plt.xlabel('days of the week')
#plt.show()

labels = 'Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'
sizes = [Sunday,Monday, Tuesday, Wednesday,Thursday,Friday,Satarday]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','blue','silver','green']
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()