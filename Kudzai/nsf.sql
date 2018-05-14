SELECT DISTINCT RIGHT([X-FileName], 
             LEN([X-FileName]) - 8) as Uses_NSF,
			 [From]
FROM [Emails].[dbo].[Tbl_Emails]
WHERE [X-FileName] LIKE '%nsf%';
