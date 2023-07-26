class _EffectView:

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
	def header_text(self):
		...
	def Search(self):
		"""
		Filters item list
		"""
		...
	def ShowSearch(self):
		"""
		Toggles search panel
		"""
		...

EffectView = _EffectView