-- Database must already exist

-- Create table in 
CREATE TABLE [dbo].[Patient] (
    [ID]            INT          IDENTITY (1, 1) NOT NULL,
    [BirthDate]     INT          NOT NULL,
    [FirstName]     VARCHAR (50) NOT NULL,
    [LastName]      VARCHAR (50) NOT NULL,
    [AccountNumber] VARCHAR (50) NOT NULL,
    [Department]    VARCHAR (20) NOT NULL,
    [Room]          INT          NOT NULL,
    CONSTRAINT [PK_Patient] PRIMARY KEY CLUSTERED ([ID] ASC)
);

-- Insert Seed Row
INSERT INTO [MyTestDB].[dbo].[Patient]
        ([BirthDate]
        ,[FirstName]
        ,[LastName]
        ,[AccountNumber]
        ,[Department]
        ,[Room])
VALUES
        ('2000-01-01 07:00:00.000'
        ,'Josh'
        ,'Patient'
        ,'A00000000001'
        ,'ICU'
        ,1)
GO
