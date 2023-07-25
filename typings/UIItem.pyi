from typing import Any

class _UIItem:

	#---Properties---#
	ID: Any
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
	def Set(self) -> None:
		...
	def Get(self) -> None:
		...
	def header_text(self):
		...

UIItem = _UIItem