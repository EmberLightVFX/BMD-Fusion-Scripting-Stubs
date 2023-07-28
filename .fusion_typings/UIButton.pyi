from typing import Any

class UIButton_:

	#---Properties---#
	AutoRepeatInterval: Any
	"""
	Read/Write
	"""
	Default: Any
	"""
	Read/Write
	"""
	IconSize: Any
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
	Flat: Any
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
	AutoDefault: Any
	"""
	Read/Write
	"""
	Icon: Any
	"""
	Write Only
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
	def SetFlat(self) -> None:
		...
	def GetFlat(self) -> None:
		...
	def SetAutoDefault(self) -> None:
		...
	def GetAutoDefault(self) -> None:
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
	def header_text(self) -> None:
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
	def SetAutoRepeatDelay(self) -> None:
		...
	def GetAutoRepeatDelay(self) -> None:
		...
	def Toggle(self) -> None:
		...
	def SetAutoRepeat(self) -> None:
		...
	def GetAutoRepeat(self) -> None:
		...
	def SetText(self) -> None:
		...
	def SetDown(self) -> None:
		...
	def GetDown(self) -> None:
		...
	def SetIcon(self) -> None:
		...
	def SetCheckable(self) -> None:
		...
	def GetCheckable(self) -> None:
		...
	def SetChecked(self) -> None:
		...
	def GetChecked(self) -> None:
		...

UIButton = UIButton_