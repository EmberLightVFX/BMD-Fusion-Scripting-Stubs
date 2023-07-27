from FusionDoc import FusionDoc_
from Request import Request_
from _non_existing import MtlData3D_


class MtlGraph3D_:

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
	def MtlGraph3D(self, doc: FusionDoc_, req: Request_) -> MtlGraph3D_:
		"""
		MtlGraph3D constructor
		"""
		...
	def SetRoot(self, root: MtlData3D_) -> None:
		...

MtlGraph3D = MtlGraph3D_