from Request import _Request
from Image import _Image
from TagList import _TagList


class _CineonInputs:

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
	def _ProcessOf(self, req: _Request, img: _Image, out: _Image, clippingmode: str, depth: int, dir: int, tags: _TagList) -> _Image:
		...
	def info_text(self):
		...
	def header_text(self):
		...

CineonInputs = _CineonInputs