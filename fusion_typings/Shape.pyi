from Matrix4 import Matrix4_
from Vector2 import Vector2_


class Shape_:

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
	def TransformOfShape(self, mat: Matrix4_) -> Shape_:
		...
	def _AddRectangle(self, v1: Vector2_, v2: Vector2_, round: float, prec: int) -> None:
		...
	def _BezierTo(self, v1: Vector2_, v2: Vector2_, v3: Vector2_, close: bool) -> None:
		...
	def IsEmpty(self) -> bool:
		...
	def _ConicTo(self, v1: Vector2_, v2: Vector2_, close: bool) -> None:
		...
	def _FitSourceTo(self, v1: Vector2_, v2: Vector2_, v3: Vector2_, v4: Vector2_, keepaspect: bool) -> None:
		...
	def Shape(self) -> Shape_:
		"""
		Shape constructor
		"""
		...
	def _FitTo(self, v1: Vector2_, v2: Vector2_, keepaspect: bool) -> None:
		...
	def info_text(self):
		...
	def _FlatBezierTo(self, v1: Vector2_, v2: Vector2_, v3: Vector2_, prec: int, close: bool) -> None:
		...
	def ExpandOfShape(self, thick: float, prec: int, fprec: int, mod: bool) -> Shape_:
		...
	def _FlatConicTo(self, v1: Vector2_, v2: Vector2_, prec: int, close: bool) -> None:
		...
	def _LineTo(self, v1: Vector2_) -> None:
		...
	def Close(self) -> None:
		...
	def _MoveTo(self, v1: Vector2_) -> None:
		...
	def FlattenOfShape(self, prec: int) -> Shape_:
		...
	def GetCount(self) -> int:
		...
	def Clear(self) -> None:
		...
	def Copy(self) -> Shape_:
		...
	def IsFlat(self) -> bool:
		...
	def header_text(self):
		...

Shape = Shape_