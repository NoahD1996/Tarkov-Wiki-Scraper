USE [TBC_DB]
GO

/****** Object:  Table [dbo].[Bullets]    Script Date: 5/12/2022 7:46:19 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Bullets]') AND type in (N'U'))
DROP TABLE [dbo].[Bullets]
GO

/****** Object:  Table [dbo].[Bullets]    Script Date: 5/12/2022 7:46:19 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Bullets](
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
	[BulletName] [varchar](40) NULL,
	[Damage] [bigint] NULL,
	[Penetration] [bigint] NULL,
	[ArmorDamage] [float] NULL,
	[Recoil] [bigint] NULL,
	[Accuracy] [bigint] NULL,
	[FragmentationChance] [float] NULL,
	[ProjectileSpeed] [bigint] NULL,
	[LightBleedingChance] [float] NULL,
	[HeavyBleedingChance] [float] NULL,
	[RicochetChance] [float] NULL,
PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


