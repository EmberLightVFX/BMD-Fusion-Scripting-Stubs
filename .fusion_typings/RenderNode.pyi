class RenderNode_:

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
	def Abort(self) -> None:
		...
	def IsDisconnecting(self) -> None:
		...
	def IsIdle(self) -> None:
		...
	def GetJob(self) -> None:
		...
	def header_text(self) -> None:
		...
	def IsProcessing(self) -> None:
		...

RenderNode = RenderNode_