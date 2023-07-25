from typing import Any

class _UIButton:

	#---Properties---#
	Icon: Any
	"""
	Write Only
	"""
	Flat: Any
	"""
	Read/Write
	"""
	AutoRepeatInterval: Any
	"""
	Read/Write
	"""
	AutoDefault: Any
	"""
	Read/Write
	"""
	Text: Any
	"""
	Read/Write
	"""
	AutoRepeatDelay: Any
	"""
	Read/Write
	"""
	AutoExclusive: Any
	"""
	Read/Write
	"""
	Down: Any
	"""
	Read/Write
	"""
	AutoRepeat: Any
	"""
	Read/Write
	"""
	Default: Any
	"""
	Read/Write
	"""
	Checkable: Any
	"""
	Read/Write
	"""
	Checked: Any
	"""
	Read/Write
	"""
	IconSize: Any
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
	def SetFlat(self) -> None:
		...
	def GetFlat(self) -> None:
		...
	def Toggle(self) -> None:
		...
	def SetAutoDefault(self) -> None:
		...
	def GetAutoDefault(self) -> None:
		...
	def SetIcon(self) -> None:
		...
	def SetDefault(self) -> None:
		...
	def GetDefault(self) -> None:
		...
	def Click(self) -> None:
		...
	def AnimateClick(self) -> None:
		...
	def SetIconSize(self) -> None:
		...
	def GetIconSize(self) -> None:
		...
	def header_text(self):
		...
	def GetText(self) -> None:
		...

UIButton = _UIButton