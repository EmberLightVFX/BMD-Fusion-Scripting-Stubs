from Image import Image_
from FusionDoc import FusionDoc_


class Clip_:

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
	def PutFrame(self, frame: int, img: Image_) -> bool:
		...
	def GetFrame(self, frame: int) -> Image_:
		...
	def header_text(self):
		...
	def Clip(self, name: str, save: bool, doc: FusionDoc_) -> Clip_:
		"""
		Clip constructor
		"""
		...
	def Open(self) -> bool:
		...
	def Close(self) -> None:
		...

Clip = Clip_