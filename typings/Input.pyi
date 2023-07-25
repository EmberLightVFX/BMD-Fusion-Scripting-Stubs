from Output import _Output
from Request import _Request
from Parameter import _Parameter


class _Input:

	#---Properties---#
	PCClass: str
	"""
	Read Only
	"""
	Source: _Output
	"""
	Read Only
	"""
	ICClass: str
	"""
	Read Only
	"""

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_VersionString: str

	REGS_ID: str

	REGB_ControlView: bool

	REGI_Priority: int


	#---Methods---#
	def IsAnimated(self) -> bool:
		...
	def info_text(self):
		...
	def GetValue(self, req: _Request, slot: int) -> _Parameter:
		...
	def header_text(self):
		...

Input = _Input