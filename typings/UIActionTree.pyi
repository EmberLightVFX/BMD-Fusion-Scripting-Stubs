class _UIActionTree:

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
	def SetTarget(self):
		...
	def AddAction(self):
		...
	def Clear(self):
		...
	def header_text(self):
		...

UIActionTree = _UIActionTree