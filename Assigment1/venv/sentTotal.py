import pyodbc
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-TJ11VHB;"
                      "Database=Emails;"
                      "Trusted_Connection=yes;")

#get from database
cursor = cnxn.cursor()
cursor.execute('SELECT [From] FROM Total_Sent')

x = []
for i in cursor.fetchall():
    x.append(i[0])

cursor = cnxn.cursor()
cursor.execute('SELECT Total FROM Total_Sent')

y = []
for i in cursor.fetchall():
    y.append(i[0])


y, x  = (list(t) for t in zip(*sorted(zip(y, x), reverse=True)))
print(x[:10])
print(y[:10])

#output chart
# naming the x-axis
plt.xlabel('Email address')
# naming the y-axis
plt.ylabel('Number of Emails')
# plot title
plt.title('Top 10 total emails sent by each user')
#plt.plot(xaxis[:10], yaxis[:10], figsize=(20,4))
plt.bar(x[:10], y[:10], tick_label = x[:10], width = 0.5, color = ['red', 'green'])
#plt.figure(figsize=(10, 5))
plt.show()