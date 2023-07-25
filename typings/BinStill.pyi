class _BinStill:

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGS_VersionString: str

	REGI_ClassType: int

	REGS_FileName: str

	REGB_ControlView: bool

	REGS_ID: str

	REGI_Priority: int

	REGB_Unpredictable: bool


	#---Methods---#
	def Defragment(self) -> None:
		"""
		Defragment this clip
		"""
		...
	def header_text(self):
		...

BinStill = _BinStill