class FloatViewFrame_:

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
	def header_text(self) -> None:
		...
	def ActivatePrevFrame(self) -> None:
		"""
		Activates the previous frame window
		"""
		...
	def ActivateNextFrame(self) -> None:
		"""
		Activates the next frame window
		"""
		...
	def ActivateFrame(self) -> None:
		"""
		Activates this frame window
		"""
		...

FloatViewFrame = FloatViewFrame_