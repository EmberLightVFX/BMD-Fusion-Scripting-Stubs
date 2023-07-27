from Output import Output_
from Request import Request_
from Parameter import Parameter_


class Input_:

	#---Properties---#
	ICClass: str
	"""
	Read Only
	"""
	PCClass: str
	"""
	Read Only
	"""
	Source: Output_
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
	def GetValue(self, req: Request_, slot: int) -> Parameter_:
		...

Input = Input_