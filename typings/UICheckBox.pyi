from typing import Any

class _UICheckBox:

	#---Properties---#
	AutoRepeatInterval: Any
	"""
	Read/Write
	"""
	Text: Any
	"""
	Read/Write
	"""
	Checkable: Any
	"""
	Read/Write
	"""
	AutoExclusive: Any
	"""
	Read/Write
	"""
	Tristate: Any
	"""
	Read/Write
	"""
	CheckState: Any
	"""
	Read/Write
	"""
	Down: Any
	"""
	Read/Write
	"""
	AutoRepeatDelay: Any
	"""
	Read/Write
	"""
	Checked: Any
	"""
	Read/Write
	"""
	AutoRepeat: Any
	"""
	Read/Write
	"""

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGS_VersionString: str

	REGI_ClassType: int

	REGI_Priority: int

	REGB_ControlView: bool

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGB_Unpredictable: bool


	#---Methods---#
	def SetAutoExclusive(self) -> None:
		...
	def GetAutoExclusive(self) -> None:
		...
	def SetAutoRepeatInterval(self) -> None:
		...
	def GetAutoRepeatInterval(self) -> None:
		...
	def SetAutoRepeatDelay(self) -> None:
		...
	def GetAutoRepeatDelay(self) -> None:
		...
	def SetText(self) -> None:
		...
	def SetAutoRepeat(self) -> None:
		...
	def GetAutoRepeat(self) -> None:
		...
	def SetDown(self) -> None:
		...
	def GetDown(self) -> None:
		...
	def SetCheckable(self) -> None:
		...
	def GetCheckable(self) -> None:
		...
	def SetChecked(self) -> None:
		...
	def GetChecked(self) -> None:
		...
	def Toggle(self) -> None:
		...
	def SetCheckState(self) -> None:
		...
	def GetCheckState(self) -> None:
		...
	def Click(self) -> None:
		...
	def AnimateClick(self) -> None:
		...
	def GetTristate(self) -> None:
		...
	def SetTristate(self) -> None:
		...
	def header_text(self):
		...
	def GetText(self) -> None:
		...

UICheckBox = _UICheckBox