class _ActionManager:

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
	def GetEvents(self):
		...
	def GetTargets(self):
		...
	def GetActions(self):
		...
	def QueueAction(self):
		...
	def header_text(self):
		...
	def DoAction(self):
		...

ActionManager = _ActionManager