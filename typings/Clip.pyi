from Clip Clipstring name import _Clip Clipstring name
from boolean save import _boolean save
from FusionDoc doc import _FusionDoc doc
from Image import _Image


class _Clip:

	#---Properties---#
	Filename: str
	"""
	Read Only
	"""
	IsMultiFrame: bool
	"""
	Read Only
	"""

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGS_VersionString: str

	REGI_ClassType: int

	REGI_Priority: int

	REGB_ControlView: bool

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGB_Unpredictable: bool


	#---Methods---#
	def Clip(self) -> tuple[_Clip Clipstring name, _boolean save, _FusionDoc doc]:
		"""
		Clip constructor
		"""
		...
	def info_text(self):
		...
	def Open(self) -> bool:
		...
	def Close(self) -> None:
		...
	def PutFrame(self, frame: int, img: _Image) -> bool:
		...
	def GetFrame(self, frame: int) -> _Image:
		...
	def header_text(self):
		...

Clip = _Clip