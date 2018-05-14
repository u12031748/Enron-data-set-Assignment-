
SELECT SUM(COUNT) [Mon]
into TblRecievedMon
FROM (
SELECT 
	ID
	,Date
	,COUNT = (LEN(Date) - LEN(REPLACE(Date, 'Mon', '')))/LEN('Mon')
FROM Tbl_Emails Where [X-Folder] Like '%inbox%'
)
as TblRecievedMon

SELECT SUM(COUNT) [Tue]
into TblRecievedTue
FROM (
SELECT 
	ID
	,Date
	,COUNT = (LEN(Date) - LEN(REPLACE(Date, 'Tue', '')))/LEN('Tue')
FROM Tbl_Emails Where [X-Folder] Like '%inbox%'
)
as TblRecievedTue

SELECT SUM(COUNT) [Wed]
into TblRecievedWed
FROM (
SELECT 
	ID
	,Date
	,COUNT = (LEN(Date) - LEN(REPLACE(Date, 'Wed', '')))/LEN('Wed')
FROM Tbl_Emails Where [X-Folder] Like '%inbox%'
)
as TblRecievedWed

SELECT SUM(COUNT) [Thu]
into TblRecievedThu
FROM (
SELECT 
	ID
	,Date
	,COUNT = (LEN(Date) - LEN(REPLACE(Date, 'Thu', '')))/LEN('Thu')
FROM Tbl_Emails Where [X-Folder] Like '%inbox%'
)
as TblRecievedThu

SELECT SUM(COUNT) [Fri]
into TblRecievedFri
FROM (
SELECT 
	ID
	,Date
	,COUNT = (LEN(Date) - LEN(REPLACE(Date, 'Fri', '')))/LEN('Fri')
FROM Tbl_Emails Where [X-Folder] Like '%inbox%'
)
as TblRecievedFri

SELECT SUM(COUNT) [Sat]
into TblRecievedSat
FROM (
SELECT 
	ID
	,Date
	,COUNT = (LEN(Date) - LEN(REPLACE(Date, 'Sat', '')))/LEN('Sat')
FROM Tbl_Emails Where [X-Folder] Like '%inbox%'
)
as TblRecievedSat

SELECT SUM(COUNT) [Sun]
into TblRecievedSun
FROM (
SELECT 
	ID
	,Date
	,COUNT = (LEN(Date) - LEN(REPLACE(Date, 'Sun', '')))/LEN('Sun')
FROM Tbl_Emails Where [X-Folder] Like '%inbox%'
)
as TblRecieved
