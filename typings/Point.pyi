from typing import Literal

class _Point:

	#---Properties---#
	X: float
	"""
	Read/Write
	"""
	Z: float
	"""
	Read/Write
	"""
	Y: float
	"""
	Read/Write
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
	def __mul(self, num: float) -> _Point:
		...
	def info_text(self):
		...
	def Point(self, x: float, y: float, z: float) -> _Point:
		"""
		Point constructor
		"""
		...
	def __eq(self, pt: _Point) -> bool:
		...
	def __unm(self) -> _Point:
		...
	def header_text(self):
		...
	def __div(self, num: float) -> _Point:
		...
	def __add(self, pt: _Point) -> _Point:
		...
	def __sub(self, pt: _Point) -> _Point:
		...

Point = _Point