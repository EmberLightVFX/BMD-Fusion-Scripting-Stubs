from typing import Any

class UIColorPicker_:

	#---Properties---#
	Color: Any
	"""
	Read/Write
	"""
	DoAlpha: Any
	"""
	Read/Write
	"""
	Text: Any
	"""
	Read/Write
	"""
	Tracking: Any
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
	def GetColor(self) -> None:
		...
	def SetText(self) -> None:
		...
	def header_text(self):
		...
	def SetColor(self) -> None:
		...
	def SetDoAlpha(self) -> None:
		...
	def GetDoAlpha(self) -> None:
		...
	def GetText(self) -> None:
		...
	def SetTracking(self) -> None:
		...
	def GetTracking(self) -> None:
		...

UIColorPicker = UIColorPicker_