class BinView:

	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGS_FileName: str

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def ExitPlayer(self) -> None:
		...

	def Paste(self) -> None:
		...

