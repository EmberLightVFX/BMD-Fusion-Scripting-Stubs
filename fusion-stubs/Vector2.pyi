from Matrix3 import Matrix3
from Matrix4 import Matrix4


class Vector2:

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
	def Distance(self, vec: Vector2) -> float:
		...

	def IsNull(self) -> bool:
		...

	def Length(self) -> float:
		...

	def Normalize(self) -> None:
		...

	def __add(self, vec: Vector2) -> Vector2:
		...

	def __div(self, num: float) -> Vector2:
		...

	def __eq(self, vec: Vector2) -> bool:
		...

	def __sub(self, vec: Vector2) -> Vector2:
		...

	def __unm(self) -> Vector2:
		...

	def _mulMat3(self, mat: Matrix3) -> Vector2:
		...

	def _mulMat4(self, mat: Matrix4) -> Vector2:
		...

	def _mulNum(self, num: float) -> Vector2:
		...

	def _newNums(self, x: float, y: float) -> Vector2:
		...

	def _newVec2(self, vec: Vector2) -> Vector2:
		...

