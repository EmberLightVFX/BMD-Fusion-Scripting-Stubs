from Point import _Point
from Point Pointfloat64 x import _Point Pointfloat64 x
from float64 y import _float64 y
from float64 z import _float64 z


class _Point:

	#---Properties---#
	X: float
	"""
	Read/Write
	"""
	Y: float
	"""
	Read/Write
	"""
	Z: float
	"""
	Read/Write
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
	def __unm(self) -> _Point:
		...
	def __eq(self, pt: _Point) -> bool:
		...
	def info_text(self):
		...
	def Point(self) -> tuple[_Point Pointfloat64 x, _float64 y, _float64 z]:
		"""
		Point constructor
		"""
		...
	def header_text(self):
		...
	def __add(self, pt: _Point) -> _Point:
		...
	def __sub(self, pt: _Point) -> _Point:
		...
	def __mul(self, num: float) -> _Point:
		...
	def __div(self, num: float) -> _Point:
		...

Point = _Point