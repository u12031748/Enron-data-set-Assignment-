SELECT [From], COUNT([From]) As Total
INTO [Emails].[dbo].Total_Sent
FROM [Emails].[dbo].[From_tbl]
GROUP BY [From]