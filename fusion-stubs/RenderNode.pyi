class RenderNode:

	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def Abort(self) -> None:
		...

	def GetJob(self) -> None:
		...

	def IsDisconnecting(self) -> None:
		...

	def IsIdle(self) -> None:
		...

	def IsProcessing(self) -> None:
		...

