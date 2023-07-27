from Request import _Request
from Image import _Image
from TagList import _TagList


class _GamutInputs:

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
	def _ProcessOf(self, req: _Request, img: _Image, out: _Image, depth: int, clippingmode: str, tags: _TagList) -> _Image:
		...

GamutInputs = _GamutInputs