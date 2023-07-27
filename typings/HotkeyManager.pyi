class _HotkeyManager:

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
	def GetKeyNames(self):
		...
	def header_text(self):
		...
	def GetKeys(self):
		...
	def GetSuffixNames(self):
		...
	def GetModifierNames(self):
		...

HotkeyManager = _HotkeyManager