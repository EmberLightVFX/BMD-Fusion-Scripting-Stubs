class HotkeyManager_:

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
	def GetKeyNames(self) -> None:
		...
	def header_text(self) -> None:
		...
	def GetKeys(self) -> None:
		...
	def GetSuffixNames(self) -> None:
		...
	def GetModifierNames(self) -> None:
		...

HotkeyManager = HotkeyManager_