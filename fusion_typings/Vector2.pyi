from Matrix3 import Matrix3_
from Matrix4 import Matrix4_


class Vector2_:

	#---Properties---#
	TypeName: str
	"""
	Read Only
	"""
	TypeNamePtr: str
	"""
	Read Only
	"""

	#---Methods---#
	def _newVec2(self, vec: Vector2_) -> Vector2_:
		...
	def info_text(self):
		...
	def _mulMat3(self, mat: Matrix3_) -> Vector2_:
		...
	def _mulMat4(self, mat: Matrix4_) -> Vector2_:
		...
	def __unm(self) -> Vector2_:
		...
	def _newNums(self, x: float, y: float) -> Vector2_:
		...
	def _mulNum(self, num: float) -> Vector2_:
		...
	def Length(self) -> float:
		...
	def IsNull(self) -> bool:
		...
	def Normalize(self) -> None:
		...
	def Distance(self, vec: Vector2_) -> float:
		...
	def __div(self, num: float) -> Vector2_:
		...
	def header_text(self):
		...
	def __eq(self, vec: Vector2_) -> bool:
		...
	def __add(self, vec: Vector2_) -> Vector2_:
		...
	def __sub(self, vec: Vector2_) -> Vector2_:
		...

Vector2 = Vector2_