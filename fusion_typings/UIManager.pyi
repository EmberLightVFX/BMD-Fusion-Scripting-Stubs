class UIManager_:

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def FindWindow(self) -> None:
		...
	def FindWindows(self) -> None:
		...
	def QueueEvent(self) -> None:
		...
	def header_text(self) -> None:
		...
	def RemoveNotify(self) -> None:
		...
	def GetEvent(self) -> None:
		...
	def AddNotify(self) -> None:
		...

UIManager = UIManager_