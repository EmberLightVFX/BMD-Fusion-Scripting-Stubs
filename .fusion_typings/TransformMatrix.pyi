from Parameter import Parameter_
from TagList import TagList_
from Request import Request_
from Input import Input_
from Image import Image_
from _non_existing import TimeStamp_


class TransformMatrix_:

	#---Properties---#
	XScale: int
	"""
	Pixel X Aspect

	Read Only
	"""
	YOffset: int
	"""
	Image X Offset

	Read Only
	"""
	YScale: int
	"""
	Pixel Y Aspect

	Read Only
	"""
	Depth: int
	"""
	Image depth indicator (not in bits)

	Depth will be one of the following values:

	1 - alpha only	8 bit integer
	2 - alpha only 16 bit integer
	3 - alpha only 16 bit float
	4 - alpha only 32 bit float
	5 - RGBA				8 bit integer
	6 - RGBA			 16 bit integer
	7 - RGBA			 16 bit float
	8 - RGBA			 32 bit float

	Read Only
	"""
	Field: int
	"""
	Field indicator

	Field will be one of the following values:

	-1 - Full Frames, no fields
	 0 - Odd (NTSC) field
	 1 - Even (PAL/HD) field

	Read Only
	"""
	Height: int
	"""
	Actual image height, in pixels

	Read Only
	"""
	OriginalHeight: int
	"""
	Unproxied image height, in pixels

	Read Only
	"""
	OriginalWidth: int
	"""
	Unproxied image width, in pixels

	Read Only
	"""
	OriginalXScale: int
	"""
	Unproxied pixel X Aspect

	Read Only
	"""
	OriginalYScale: int
	"""
	Unproxied pixel Y Aspect

	Read Only
	"""
	OriginalIXScale: float
	"""
	Read Only
	"""
	OriginalIYScale: float
	"""
	Read Only
	"""
	Width: int
	"""
	Actual image width, in pixels

	Read Only
	"""
	XOffset: int
	"""
	Image X Offset

	Read Only
	"""
	ProxyScale: int
	"""
	Image proxy scale multiplier

	ProxyScale may be any positive integer, where 1 indicates no proxy.

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
	def MergeConcatenate(self, fg: Parameter_, tags: TagList_) -> None:
		...
	def info_text(self) -> None:
		...
	def header_text(self) -> None:
		...
	def TransformMatrix(self, img: Parameter_, req: Request_, inp: Input_, slot: int, time: TimeStamp_) -> TransformMatrix_:
		"""
		TransformMatrix constructor
		"""
		...
	def ImageConcatenate(self, tags: TagList_) -> None:
		...
	def ApplyTransform(self, tags: TagList_) -> Image_:
		...

TransformMatrix = TransformMatrix_