from typing import Literal

class _StyledText:

	#---Properties---#
	Value: str
	"""
	Read Only
	"""

	#---Attributes---#
	REGS_FileName: str

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
	def header_text(self):
		...
	def info_text(self):
		...
	def StyledText(self, val: str) -> _StyledText:
		"""
		StyledText constructor
		"""
		...

StyledText = _StyledText