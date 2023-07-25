from Vector2 import _Vector2
from Shape import _Shape
from Shape Shape import _Shape Shape
from Matrix4 import _Matrix4


class _Shape:

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_VersionString: str

	REGS_ID: str

	REGB_ControlView: bool

	REGI_Priority: int


	#---Methods---#
	def _AddRectangle(self, v1: _Vector2, v2: _Vector2, round: float, prec: int) -> None:
		...
	def Close(self) -> None:
		...
	def IsEmpty(self) -> bool:
		...
	def _ConicTo(self, v1: _Vector2, v2: _Vector2, close: bool) -> None:
		...
	def _FitSourceTo(self, v1: _Vector2, v2: _Vector2, v3: _Vector2, v4: _Vector2, keepaspect: bool) -> None:
		...
	def Copy(self) -> _Shape:
		...
	def Shape(self) -> _Shape Shape:
		"""
		Shape constructor
		"""
		...
	def _FitTo(self, v1: _Vector2, v2: _Vector2, keepaspect: bool) -> None:
		...
	def header_text(self):
		...
	def _FlatBezierTo(self, v1: _Vector2, v2: _Vector2, v3: _Vector2, prec: int, close: bool) -> None:
		...
	def ExpandOfShape(self, thick: float, prec: int, fprec: int, mod: bool) -> _Shape:
		...
	def _FlatConicTo(self, v1: _Vector2, v2: _Vector2, prec: int, close: bool) -> None:
		...
	def _LineTo(self, v1: _Vector2) -> None:
		...
	def _MoveTo(self, v1: _Vector2) -> None:
		...
	def FlattenOfShape(self, prec: int) -> _Shape:
		...
	def info_text(self):
		...
	def GetCount(self) -> int:
		...
	def IsFlat(self) -> bool:
		...
	def Clear(self) -> None:
		...
	def TransformOfShape(self, mat: _Matrix4) -> _Shape:
		...
	def _BezierTo(self, v1: _Vector2, v2: _Vector2, v3: _Vector2, close: bool) -> None:
		...

Shape = _Shape