from Matrix4 import _Matrix4
from Vector2 import _Vector2


class _Shape:

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
	def TransformOfShape(self, mat: _Matrix4) -> _Shape:
		...
	def _AddRectangle(self, v1: _Vector2, v2: _Vector2, round: float, prec: int) -> None:
		...
	def _BezierTo(self, v1: _Vector2, v2: _Vector2, v3: _Vector2, close: bool) -> None:
		...
	def IsEmpty(self) -> bool:
		...
	def _ConicTo(self, v1: _Vector2, v2: _Vector2, close: bool) -> None:
		...
	def _FitSourceTo(self, v1: _Vector2, v2: _Vector2, v3: _Vector2, v4: _Vector2, keepaspect: bool) -> None:
		...
	def Shape(self) -> _Shape:
		"""
		Shape constructor
		"""
		...
	def _FitTo(self, v1: _Vector2, v2: _Vector2, keepaspect: bool) -> None:
		...
	def info_text(self):
		...
	def _FlatBezierTo(self, v1: _Vector2, v2: _Vector2, v3: _Vector2, prec: int, close: bool) -> None:
		...
	def ExpandOfShape(self, thick: float, prec: int, fprec: int, mod: bool) -> _Shape:
		...
	def _FlatConicTo(self, v1: _Vector2, v2: _Vector2, prec: int, close: bool) -> None:
		...
	def _LineTo(self, v1: _Vector2) -> None:
		...
	def Close(self) -> None:
		...
	def _MoveTo(self, v1: _Vector2) -> None:
		...
	def FlattenOfShape(self, prec: int) -> _Shape:
		...
	def GetCount(self) -> int:
		...
	def Clear(self) -> None:
		...
	def Copy(self) -> _Shape:
		...
	def IsFlat(self) -> bool:
		...
	def header_text(self):
		...

Shape = _Shape