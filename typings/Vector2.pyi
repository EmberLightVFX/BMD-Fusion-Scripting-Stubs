from Vector2 import _Vector2
from Matrix3 import _Matrix3
from Matrix4 import _Matrix4


class _Vector2:

	#---Properties---#
	TypeNamePtr: str
	"""
	Read Only
	"""
	TypeName: str
	"""
	Read Only
	"""

	#---Methods---#
	def _newVec2(self, vec: _Vector2) -> _Vector2:
		...
	def __unm(self) -> _Vector2:
		...
	def _newNums(self, x: float, y: float) -> _Vector2:
		...
	def _mulMat3(self, mat: _Matrix3) -> _Vector2:
		...
	def _mulMat4(self, mat: _Matrix4) -> _Vector2:
		...
	def __eq(self, vec: _Vector2) -> bool:
		...
	def _mulNum(self, num: float) -> _Vector2:
		...
	def header_text(self):
		...
	def info_text(self):
		...
	def IsNull(self) -> bool:
		...
	def Normalize(self) -> None:
		...
	def __add(self, vec: _Vector2) -> _Vector2:
		...
	def __sub(self, vec: _Vector2) -> _Vector2:
		...
	def Length(self) -> float:
		...
	def __div(self, num: float) -> _Vector2:
		...

Vector2 = _Vector2