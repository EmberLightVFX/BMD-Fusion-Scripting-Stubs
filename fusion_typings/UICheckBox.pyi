from typing import Any

class UICheckBox_:

	#---Properties---#
	AutoRepeatInterval: Any
	"""
	Read/Write
	"""
	AutoRepeatDelay: Any
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
	AutoRepeat: Any
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
	Checked: Any
	"""
	Read/Write
	"""
	Text: Any
	"""
	Read/Write
	"""
	Tristate: Any
	"""
	Read/Write
	"""

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def SetText(self) -> None:
		...
	def Click(self) -> None:
		...
	def GetCheckState(self) -> None:
		...
	def SetTristate(self) -> None:
		...
	def GetTristate(self) -> None:
		...
	def GetText(self) -> None:
		...
	def SetAutoExclusive(self) -> None:
		...
	def GetAutoExclusive(self) -> None:
		...
	def SetAutoRepeatInterval(self) -> None:
		...
	def GetAutoRepeatInterval(self) -> None:
		...
	def Toggle(self) -> None:
		...
	def SetAutoRepeatDelay(self) -> None:
		...
	def GetAutoRepeatDelay(self) -> None:
		...
	def header_text(self):
		...
	def SetAutoRepeat(self) -> None:
		...
	def GetAutoRepeat(self) -> None:
		...
	def AnimateClick(self) -> None:
		...
	def SetDown(self) -> None:
		...
	def GetDown(self) -> None:
		...
	def SetCheckState(self) -> None:
		...
	def SetCheckable(self) -> None:
		...
	def GetCheckable(self) -> None:
		...
	def SetChecked(self) -> None:
		...
	def GetChecked(self) -> None:
		...

UICheckBox = UICheckBox_