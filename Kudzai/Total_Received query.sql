SELECT [To], COUNT([To]) As Total
INTO [Emails].[dbo].Total_Received
FROM [Emails].[dbo].[From_tbl]
GROUP BY [To]