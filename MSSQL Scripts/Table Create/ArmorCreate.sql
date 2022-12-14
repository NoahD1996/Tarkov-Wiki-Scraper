USE [TBC_DB]
GO

/****** Object:  Table [dbo].[Armor]    Script Date: 5/12/2022 7:46:04 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Armor]') AND type in (N'U'))
DROP TABLE [dbo].[Armor]
GO

/****** Object:  Table [dbo].[Armor]    Script Date: 5/12/2022 7:46:04 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Armor](
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
	[ArmorName] [varchar](70) NULL,
	[MaxDurability] [bigint] NULL,
	[Level] [bigint] NULL,
	[Material] [varchar](40) NULL,
	[Destructibility] [float] NULL,
	[Zones] [varchar](50) NULL,
	[MovementSpeed] [float] NULL,
	[TurnSpeed] [float] NULL,
	[Ergonomics] [bigint] NULL,
	[Weight] [float] NULL,
PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


