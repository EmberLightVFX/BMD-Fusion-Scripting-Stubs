class _RenderNode:

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
	def Abort(self):
		...
	def IsDisconnecting(self):
		...
	def IsIdle(self):
		...
	def GetJob(self):
		...
	def IsProcessing(self):
		...
	def header_text(self):
		...

RenderNode = _RenderNode