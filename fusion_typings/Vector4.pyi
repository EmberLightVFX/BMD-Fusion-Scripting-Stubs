from Vector4f import Vector4f_
from Vector3f import Vector3f_
from Matrix4 import Matrix4_


class Vector4_:

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
	def __div(self, v: float) -> Vector4_:
		...
	def __unm(self) -> Vector4_:
		...
	def _newVec4(self, vec: Vector4_) -> Vector4_:
		...
	def _newVec4f(self, vec: Vector4f_) -> Vector4_:
		...
	def _newVec3f(self, vec: Vector3f_) -> Vector4_:
		...
	def header_text(self):
		...
	def _LerpVec4(self, vec: Vector4_, t: Vector4_) -> Vector4_:
		...
	def _LerpNum(self, vec: Vector4_, t: float) -> Vector4_:
		...
	def info_text(self):
		...
	def _newNums(self, x: float, y: float, z: float, w: float) -> Vector4_:
		...
	def _mulMat4(self, mat: Matrix4_) -> Vector4_:
		...
	def Scale(self, x: float, y: float, z: float, w: float) -> Vector4_:
		...
	def Set(self, x: float, y: float, z: float, w: float) -> None:
		...
	def _mulNum(self, v: float) -> Vector4_:
		...
	def Length(self) -> float:
		...
	def __eq(self, vec: Vector4_) -> bool:
		...
	def Normalize(self) -> None:
		...
	def Dot4(self, vec: Vector4_) -> Vector4_:
		...
	def Distance(self, vec: Vector4_) -> float:
		...
	def Dot3(self, vec: Vector4_) -> Vector4_:
		...
	def Cross(self, vec: Vector4_) -> Vector4_:
		...
	def __add(self, vec: Vector4_) -> Vector4_:
		...
	def __sub(self, vec: Vector4_) -> Vector4_:
		...

Vector4 = Vector4_