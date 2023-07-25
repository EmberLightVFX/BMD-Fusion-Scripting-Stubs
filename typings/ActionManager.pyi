class _ActionManager:

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
	def QueueAction(self):
		...
	def GetTargets(self):
		...
	def GetEvents(self):
		...
	def DoAction(self):
		...
	def GetActions(self):
		...
	def header_text(self):
		...

ActionManager = _ActionManager