WITH XMLNAMESPACES('http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/StoreSurvey' AS ns)
SELECT
	name,
	AnnualRevenue = demographics.value('(/ns:StoreSurvey/ns:AnnualRevenue)[1]', 'DECIMAL(10,2)'),
	SquareFeet = demographics.value('(/ns:StoreSurvey/ns:SquareFeet)[1]', 'INT'),
	NumberEmployees = demographics.value('(/ns:StoreSurvey/ns:NumberEmployees)[1]', 'INT')
FROM [AdventureWorks2022].[Sales].[Store];

