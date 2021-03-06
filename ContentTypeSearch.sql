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
      ,[X-FileName]
  FROM [Emails].[dbo].[Tbl_Emails]
  where [Content-Type] like '%video%' or
		[Content-Type] like '%application%' or
		[Content-Type] like '%audio%' or
		[Content-Type] like '%image%' or
		[Content-Type] like '%video%' or
		[Content-Type] like '%text/sgml%' or
		[Content-Type] like '%text/html%' or
		[Content-Type] like '%text/richtext%' or
		[Content-Type] like '%text/plain Invalid%' or
		[Content-Type] like '%text/richtext Header%' or
		[Content-Type] like '%text/css%' or
		[Content-Type] like '%text/richtext%'
    
