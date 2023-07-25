from Request import _Request
from Parameter import _Parameter


class _Output:

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
	def _SetParam(self, req: _Request, param: _Parameter) -> None:
		...
	def info_text(self):
		...
	def _SetNum(self, req: _Request, num: float) -> None:
		...
	def header_text(self):
		...

Output = _Output