import pyodbc
import re
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objs as go
import plotly.plotly as py
import matplotlib.mlab as mlab

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-PL894JS\SQLEXPRESS;"
                      "Database=Emails;"
                      "Trusted_Connection=yes;")

cursor = cnxn.cursor()
Emails = cursor.execute('SELECT [From] FROM TblSubjectAnalysisInvoices')

From = []
x = 0
for i in cursor.fetchall():
    From.append(i[0])

UniqueEmails = set(From)
SortedUniqueListX = list(UniqueEmails)

SortedUniqueListX, yaxis = np.unique(From, return_counts=True)

yaxis, SortedUniqueListX  = (list(t) for t in zip(*sorted(zip(yaxis, SortedUniqueListX), reverse=False)))
print(SortedUniqueListX[:20])
print(yaxis[:20])

#output chart
# naming the x-axis
plt.xlabel('Email address')
# naming the y-axis
plt.ylabel('Number of Emails')
# plot title
plt.title('Emails with word invoice in subject')
#plt.plot(xaxis[:10], yaxis[:10], figsize=(20,4))
plt.bar(SortedUniqueListX[10:20], yaxis[10:20], tick_label = SortedUniqueListX[10:20], width = 0.5, color = ['lightblue', 'lightgreen'])
plt.xticks(rotation=80)
plt.tight_layout()
#plt.figure(figsize=(10, 5))
plt.show()