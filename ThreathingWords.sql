/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [ID]
      ,[Message-ID]
      ,[Date]
      ,[From]
      ,[To]
      ,[Subject]
      ,[Cc]
      ,[Mime-Version]
      ,[Content-Type]
      ,[Content-Transfer-Encoding]
      ,[Bcc]
      ,[X-From]
      ,[X-To]
      ,[X-cc]
      ,[X-bcc]
      ,[X-Folder]
      ,[X-Origin]
      ,[X-FileName]
  FROM [Emails].[dbo].[Tbl_Emails]
  where [Subject] Like '%suck%' or
  [Subject] like '%Fuck%' or
  [Subject] like '%bitch%' or
  [Subject] like '%jail%' 
 

