class _HotkeyManager:

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
	def GetSuffixNames(self):
		...
	def GetModifierNames(self):
		...
	def GetKeyNames(self):
		...
	def header_text(self):
		...
	def GetKeys(self):
		...

HotkeyManager = _HotkeyManager