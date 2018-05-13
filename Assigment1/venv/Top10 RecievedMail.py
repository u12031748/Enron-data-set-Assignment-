import pyodbc
import re
import matplotlib.pyplot as plt
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-PL894JS\SQLEXPRESS;"
                      "Database=Emails;"
                      "Trusted_Connection=yes;")

cursor = cnxn.cursor()
cursor.execute('SELECT [To] FROM Total_Received')

x = []
for i in cursor.fetchall():
    x.append(i[0])


cursor = cnxn.cursor()
cursor.execute('SELECT Total FROM Total_Received')

y = []
for i in cursor.fetchall():
    y.append(i[0])


y, x  = (list(t) for t in zip(*sorted(zip(y, x), reverse=True)))
print(x[:20])
print(y[:20])

Names = []
for i in  x[:20]:
    Names.append(i.split('@')[0])

print(Names)
#output chart
# naming the x-axis
plt.xlabel('Email address owner')
# naming the y-axis
plt.ylabel('Number of Emails')
# plot title
plt.title('Top 20 total emails recieved by the top 10 user')
#plt.plot(xaxis[:10], yaxis[:10], figsize=(20,4))
plt.figure(figsize=(20, 5))
plt.bar(Names[:10], y[:10], tick_label = Names[:10],align='edge', width=0.3, color = ['lightblue', 'lightgreen'])

plt.show()