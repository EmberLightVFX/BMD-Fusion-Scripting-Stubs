class HotkeyManager:

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
	def GetKeyNames(self) -> None:
		...

	def GetKeys(self) -> None:
		...

	def GetModifierNames(self) -> None:
		...

	def GetSuffixNames(self) -> None:
		...

