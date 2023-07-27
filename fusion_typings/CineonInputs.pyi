from Request import Request_
from Image import Image_
from TagList import TagList_


class CineonInputs_:

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
	def _ProcessOf(self, req: Request_, img: Image_, out: Image_, clippingmode: str, depth: int, dir: int, tags: TagList_) -> Image_:
		...

CineonInputs = CineonInputs_