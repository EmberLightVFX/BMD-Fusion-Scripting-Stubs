class FloatViewFrame:

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
	def ActivateFrame(self) -> None:
		"""
		Activates this frame window
		"""
		...

	def ActivateNextFrame(self) -> None:
		"""
		Activates the next frame window
		"""
		...

	def ActivatePrevFrame(self) -> None:
		"""
		Activates the previous frame window
		"""
		...

