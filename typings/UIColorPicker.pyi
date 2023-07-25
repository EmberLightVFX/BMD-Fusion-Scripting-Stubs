from typing import Any

class _UIColorPicker:

	#---Properties---#
	DoAlpha: Any
	"""
	Read/Write
	"""
	Color: Any
	"""
	Read/Write
	"""
	Tracking: Any
	"""
	Read/Write
	"""
	Text: Any
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
	def SetTracking(self) -> None:
		...
	def GetTracking(self) -> None:
		...
	def SetColor(self) -> None:
		...
	def SetText(self) -> None:
		...
	def GetColor(self) -> None:
		...
	def GetText(self) -> None:
		...
	def header_text(self):
		...
	def SetDoAlpha(self) -> None:
		...
	def GetDoAlpha(self) -> None:
		...

UIColorPicker = _UIColorPicker