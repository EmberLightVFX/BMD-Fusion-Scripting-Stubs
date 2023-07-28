class ActionManager_:

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
	def GetEvents(self) -> None:
		...
	def GetTargets(self) -> None:
		...
	def GetActions(self) -> None:
		...
	def QueueAction(self) -> None:
		...
	def header_text(self) -> None:
		...
	def DoAction(self) -> None:
		...

ActionManager = ActionManager_