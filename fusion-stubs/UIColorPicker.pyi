from typing import Any

class UIColorPicker:

	#---Properties---#
	Color: Any

	DoAlpha: Any

	Text: Any

	Tracking: Any


	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGB_Utility_Toggle: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def GetColor(self) -> None:
		...

	def GetDoAlpha(self) -> None:
		...

	def GetText(self) -> None:
		...

	def GetTracking(self) -> None:
		...

	def SetColor(self) -> None:
		...

	def SetDoAlpha(self) -> None:
		...

	def SetText(self) -> None:
		...

	def SetTracking(self) -> None:
		...

