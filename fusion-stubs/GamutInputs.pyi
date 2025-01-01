from Image import Image
from TagList import TagList
from Request import Request


class GamutInputs:

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
	def _ProcessOf(self, req: Request, img: Image, out: Image, depth: int, clippingmode: str, tags: TagList) -> Image:
		...

