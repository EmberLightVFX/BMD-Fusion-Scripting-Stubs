from Parameter import Parameter
from Output import Output
from Request import Request


class Input:

	#---Properties---#
	ICClass: str
	"""
	Read Only
	"""

	PCClass: str
	"""
	Read Only
	"""

	Source: Output
	"""
	Read Only
	"""


	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def GetValue(self, req: Request, slot: int) -> Parameter:
		...

	def IsAnimated(self) -> bool:
		...

