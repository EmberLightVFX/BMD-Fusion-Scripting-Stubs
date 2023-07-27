from Output import _Output
from Request import _Request
from Parameter import _Parameter


class _Input:

	#---Properties---#
	ICClass: str
	"""
	Read Only
	"""
	PCClass: str
	"""
	Read Only
	"""
	Source: _Output
	"""
	Read Only
	"""

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def header_text(self):
		...
	def info_text(self):
		...
	def IsAnimated(self) -> bool:
		...
	def GetValue(self, req: _Request, slot: int) -> _Parameter:
		...

Input = _Input