from MtlGraph3D MtlGraph3DFusionDoc doc import _MtlGraph3D MtlGraph3DFusionDoc doc
from Request req import _Request req
from MtlData3D import _MtlData3D


class _MtlGraph3D:

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGS_VersionString: str

	REGS_UIName: str

	REGI_ClassType: int

	REGI_Priority: int

	REGB_ControlView: bool

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGB_Unpredictable: bool


	#---Methods---#
	def MtlGraph3D(self) -> tuple[_MtlGraph3D MtlGraph3DFusionDoc doc, _Request req]:
		"""
		MtlGraph3D constructor
		"""
		...
	def info_text(self):
		...
	def SetRoot(self, root: _MtlData3D) -> None:
		...
	def header_text(self):
		...

MtlGraph3D = _MtlGraph3D