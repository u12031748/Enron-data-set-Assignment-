/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (55000) [ID]
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
      ,[X-FileName]   as TblSubjectAnalysisMoney
  into [Emails].[dbo].TblSubjectAnalysisMoney
  FROM [Emails].[dbo].[Tbl_Emails]
  where [Subject] like '%money%'
