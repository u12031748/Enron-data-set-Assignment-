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
cursor.execute('SELECT * FROM From_tbl')
results = list(cursor.fetchall())
#sort
results.sort()
#Sprint(results)
#print(len(results))

#turn results to list
#list(sum(results, ()))
r = []
for element in results:
    #print(",".join(element))
    r.append(",".join(element))


r.sort()

x = 0
while x < len(r):
    r[x].strip('\n')
    x += 1

#print(r)
#print(r.__sizeof__())

#get unique emails for x-axis
fromSet = set(r)
xaxis = list(fromSet)
xaxis.sort()
#print(xaxis)
#print(len(xaxis))

#get count of unique emails for y-axis
xaxis, yaxis = np.unique(r, return_counts=True)
#print("Frequency of unique values of the said array:")
#print(np.asarray((xaxis[:10], yaxis[:10])))

#sort by most emails sent
#xaxis = np.array(xaxis)
#yaxis = np.array(yaxis)
#inds = yaxis.argsort()
#sortedPeople = xaxis[inds]

yaxis, xaxis  = (list(t) for t in zip(*sorted(zip(yaxis, xaxis), reverse=True)))
print(xaxis[:10])
print(yaxis[:10])

#y = 0
#while y < len(yaxis):
list(map(int, yaxis))
list(map(str, xaxis))
 #   y += 1

#output chart
# naming the x-axis
plt.xlabel('Email address')
# naming the y-axis
plt.ylabel('Number of Emails')
# plot title
plt.title('Total emails sent by each user')
#plt.plot(xaxis[:10], yaxis[:10], figsize=(20,4))
plt.bar(xaxis[:10], yaxis[:10], tick_label = xaxis[:10], width = 0.5, color = ['red', 'green'])
#plt.figure(figsize=(10, 5))
plt.show()

#persist result to database
#cursor.execute('''CREATE TABLE SentEmailsTotal (ID int, Email varchar(255), Total int, PRIMARY KEY (ID))''')
#cursor.commit()
i = 1
while i < len(xaxis)+1:
    #cursor.execute('INSERT INTO SentEmailsTotal (ID, Email, Total) values ("%d","%s","%d")' % (i, xaxis[i], yaxis[i]))
    #cursor.execute('INSERT INTO SentEmailsTotal (Email, Total) values ('+xaxis[i]+','+yaxis[i]+')')
    cursor.execute('INSERT INTO SentEmailsTotal (Email) values (' + xaxis[i] + ')')
    cursor.commit()
    i += 1


