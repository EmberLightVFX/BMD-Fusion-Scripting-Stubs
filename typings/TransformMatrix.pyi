from TagList import _TagList
from Image import _Image
from Parameter import _Parameter
from TransformMatrix TransformMatrixParameter img import _TransformMatrix TransformMatrixParameter img
from Request req import _Request req
from Input inp import _Input inp
from int32 slot import _int32 slot
from TimeStamp time import _TimeStamp time


class _TransformMatrix:

	#---Properties---#
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
	OriginalIXScale: float
	"""
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
	OriginalIYScale: float
	"""
	Read Only
	"""
	OriginalWidth: int
	"""
	Unproxied image width, in pixels

	Read Only
	"""
	YOffset: int
	"""
	Image X Offset

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
	def ImageConcatenate(self, tags: _TagList) -> None:
		...
	def ApplyTransform(self, tags: _TagList) -> _Image:
		...
	def MergeConcatenate(self, fg: _Parameter, tags: _TagList) -> None:
		...
	def TransformMatrix(self) -> tuple[_TransformMatrix TransformMatrixParameter img, _Request req, _Input inp, _int32 slot, _TimeStamp time]:
		"""
		TransformMatrix constructor
		"""
		...
	def info_text(self):
		...
	def header_text(self):
		...

TransformMatrix = _TransformMatrix