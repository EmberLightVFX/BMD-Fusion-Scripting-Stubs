class _UIDialog:

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGS_VersionString: str

	REGI_ClassType: int

	REGI_Priority: int

	REGB_ControlView: bool

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGB_Unpredictable: bool


	#---Methods---#
	def Exec(self) -> None:
		...
	def RecalcLayout(self) -> None:
		...
	def header_text(self):
		...
	def Done(self) -> None:
		...
	def IsRunning(self) -> None:
		...

UIDialog = _UIDialog