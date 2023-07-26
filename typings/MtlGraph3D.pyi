from typing import Literal

from FusionDoc import _FusionDoc
from Request import _Request
from _non_existing import _MtlData3D


class _MtlGraph3D:

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGB_ControlView: bool

	REGB_Utility_Toggle: bool

	REGS_Name: str

	REGB_Unpredictable: bool

	REGS_UIName: str


	#---Methods---#
	def header_text(self):
		...
	def info_text(self):
		...
	def MtlGraph3D(self, doc: _FusionDoc, req: _Request) -> _MtlGraph3D:
		"""
		MtlGraph3D constructor
		"""
		...
	def SetRoot(self, root: _MtlData3D) -> None:
		...

MtlGraph3D = _MtlGraph3D