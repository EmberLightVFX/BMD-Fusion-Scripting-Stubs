class _UIManager:

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_VersionString: str

	REGS_ID: str

	REGB_ControlView: bool

	REGI_Priority: int


	#---Methods---#
	def AddNotify(self) -> None:
		...
	def QueueEvent(self) -> None:
		...
	def GetEvent(self) -> None:
		...
	def FindWindow(self) -> None:
		...
	def FindWindows(self) -> None:
		...
	def RemoveNotify(self) -> None:
		...
	def header_text(self):
		...

UIManager = _UIManager