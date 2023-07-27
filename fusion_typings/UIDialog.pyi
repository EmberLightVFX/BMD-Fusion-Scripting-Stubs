class UIDialog_:

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def RecalcLayout(self) -> None:
		...
	def header_text(self):
		...
	def Done(self) -> None:
		...
	def IsRunning(self) -> None:
		...
	def Exec(self) -> None:
		...

UIDialog = UIDialog_