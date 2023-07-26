from Image import _Image
from FusionDoc import _FusionDoc


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
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def info_text(self):
		...
	def PutFrame(self, frame: int, img: _Image) -> bool:
		...
	def GetFrame(self, frame: int) -> _Image:
		...
	def header_text(self):
		...
	def Clip(self, name: str, save: bool, doc: _FusionDoc) -> _Clip:
		"""
		Clip constructor
		"""
		...
	def Open(self) -> bool:
		...
	def Close(self) -> None:
		...

Clip = _Clip