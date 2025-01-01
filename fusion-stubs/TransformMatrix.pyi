from Request import Request
from ImgRectI import ImgRectI
from Image import Image
from Parameter import Parameter
from TagList import TagList
from Input import Input
from _non_existing import TimeStamp


class TransformMatrix:

	#---Properties---#
	Depth: int
	"""
	Image depth indicator (not in bits)

	Depth will be one of the following values:
	
	1 - alpha only  8 bit integer
	2 - alpha only 16 bit integer
	3 - alpha only 16 bit float
	4 - alpha only 32 bit float
	5 - RGBA        8 bit integer
	6 - RGBA       16 bit integer
	7 - RGBA       16 bit float
	8 - RGBA       32 bit float

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

	ProxyScale: int
	"""
	Image proxy scale multiplier

	ProxyScale may be any positive integer, where 1 indicates no proxy.

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

	DataWindow: ImgRectI
	"""
	Read Only
	"""

	ImageWindow: ImgRectI
	"""
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
	def ApplyTransform(self, tags: TagList) -> Image:
		...

	def ImageConcatenate(self, tags: TagList) -> None:
		...

	def MergeConcatenate(self, fg: Parameter, tags: TagList) -> None:
		...

	def __new(self, img: Parameter, req: Request, inp: Input, slot: int, time: TimeStamp) -> TransformMatrix:
		"""
		TransformMatrix constructor

		Args:
			img (Parameter)
			req (Request)
			inp (Input)
			slot (int)
			time (TimeStamp)

		Returns:
			TransformMatrix
		"""
		...

