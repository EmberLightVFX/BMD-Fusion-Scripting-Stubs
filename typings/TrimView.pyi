class _TrimView:

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
	def Exit(self):
		...
	def header_text(self):
		...

TrimView = _TrimView