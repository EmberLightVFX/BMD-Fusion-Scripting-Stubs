class _FloatViewFrame:

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
	def header_text(self):
		...

FloatViewFrame = _FloatViewFrame