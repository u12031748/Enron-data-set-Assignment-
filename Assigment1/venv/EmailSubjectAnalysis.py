
import pyodbc
import re
import matplotlib.pyplot as plt
import numpy as np

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-PL894JS\SQLEXPRESS;"
                      "Database=Emails;"
                      "Trusted_Connection=yes;")

cursor = cnxn.cursor()
#cursor.execute('SELECT * FROM TblSubjectAnalysisMoney')
Emails = cursor.execute('SELECT [From] FROM TblSubjectAnalysisMoney')

From = []
x = 0
for i in cursor.fetchall():
    From.append(i[0])

UniqueEmails = set(From)
SortedUniqueListX = list(UniqueEmails)

SortedUniqueListX, yaxis = np.unique(From, return_counts=True)

yaxis, SortedUniqueListX  = (list(t) for t in zip(*sorted(zip(yaxis, SortedUniqueListX), reverse=True)))
print(SortedUniqueListX[:20])
print(yaxis[:20])

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1,0.1, 0.1, 0.1,0.1,0.1,0.1,0.1,0.1,0.1)  # explode 1st slice

# Plot
plt.pie(yaxis[:10], explode=explode, labels=SortedUniqueListX[:10], colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
#print(len(SortedUniqueList))

