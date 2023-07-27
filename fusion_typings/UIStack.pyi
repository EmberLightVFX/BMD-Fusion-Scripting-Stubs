from typing import Any

class UIStack_:

	#---Properties---#
	CurrentIndex: Any
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
	def header_text(self) -> None:
		...
	def GetCurrentIndex(self) -> None:
		...
	def SetCurrentIndex(self) -> None:
		...

UIStack = UIStack_