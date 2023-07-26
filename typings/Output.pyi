from typing import Literal

from Request import _Request
from Parameter import _Parameter


class _Output:

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
	def _SetParam(self, req: _Request, param: _Parameter) -> None:
		...
	def _SetNum(self, req: _Request, num: float) -> None:
		...

Output = _Output