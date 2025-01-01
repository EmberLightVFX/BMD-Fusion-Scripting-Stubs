from Request import Request
from FusionDoc import FusionDoc
from _non_existing import MtlData3D


class MtlGraph3D:

	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGB_Utility_Toggle: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def SetRoot(self, root: MtlData3D) -> None:
		...

	def __new(self, doc: FusionDoc, req: Request) -> MtlGraph3D:
		"""
		MtlGraph3D constructor

		Args:
			doc (FusionDoc)
			req (Request)

		Returns:
			MtlGraph3D
		"""
		...

