class _ReelView:

	#---Attributes---#
	REGS_FileName: str

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
	def ExitPlayer(self):
		...
	def header_text(self):
		...
	def ZoomOut(self):
		...
	def ZoomIn(self):
		...
	def DeleteSelected(self):
		...

ReelView = _ReelView