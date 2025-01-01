from FusionDoc import FusionDoc
from Image import Image


class Clip:

	#---Properties---#
	Filename: str
	"""
	Read Only
	"""

	IsMultiFrame: bool
	"""
	Read Only
	"""


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
	def Close(self) -> None:
		...

	def GetFrame(self, frame: int) -> Image:
		...

	def Open(self) -> bool:
		...

	def PutFrame(self, frame: int, img: Image) -> bool:
		...

	def __new(self, name: str, save: bool, doc: FusionDoc) -> Clip:
		"""
		Clip constructor

		Args:
			name (str)
			save (bool)
			doc (FusionDoc)

		Returns:
			Clip
		"""
		...

