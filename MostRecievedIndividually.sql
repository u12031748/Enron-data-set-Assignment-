SELECT [To], COUNT([To]) As Total
INTO [Emails].[dbo].Total_Received
FROM [Emails].[dbo].Tbl_Emails
GROUP BY [To]