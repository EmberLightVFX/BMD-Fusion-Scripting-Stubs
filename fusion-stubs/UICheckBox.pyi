from typing import Any

class UICheckBox:

	#---Properties---#
	AutoExclusive: Any

	AutoRepeat: Any

	AutoRepeatDelay: Any

	AutoRepeatInterval: Any

	CheckState: Any

	Checkable: Any

	Checked: Any

	Down: Any

	Text: Any

	Tristate: Any


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
	def AnimateClick(self) -> None:
		...

	def Click(self) -> None:
		...

	def GetAutoExclusive(self) -> None:
		...

	def GetAutoRepeat(self) -> None:
		...

	def GetAutoRepeatDelay(self) -> None:
		...

	def GetAutoRepeatInterval(self) -> None:
		...

	def GetCheckState(self) -> None:
		...

	def GetCheckable(self) -> None:
		...

	def GetChecked(self) -> None:
		...

	def GetDown(self) -> None:
		...

	def GetText(self) -> None:
		...

	def GetTristate(self) -> None:
		...

	def SetAutoExclusive(self) -> None:
		...

	def SetAutoRepeat(self) -> None:
		...

	def SetAutoRepeatDelay(self) -> None:
		...

	def SetAutoRepeatInterval(self) -> None:
		...

	def SetCheckState(self) -> None:
		...

	def SetCheckable(self) -> None:
		...

	def SetChecked(self) -> None:
		...

	def SetDown(self) -> None:
		...

	def SetText(self) -> None:
		...

	def SetTristate(self) -> None:
		...

	def Toggle(self) -> None:
		...

