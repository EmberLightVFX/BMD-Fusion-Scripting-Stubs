from Matrix4 import Matrix4_


class Vector3f_:

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
	def __div(self, num: float) -> Vector3f_:
		...
	def __pow(self, vec: Vector3f_) -> Vector3f_:
		...
	def __unm(self) -> Vector3f_:
		...
	def LengthSquared(self) -> float:
		...
	def IsNaN(self) -> bool:
		...
	def IsNormalized(self) -> bool:
		...
	def IsZero(self, num: float) -> bool:
		...
	def Equals(self, vec: Vector3f_) -> bool:
		...
	def header_text(self) -> None:
		...
	def info_text(self) -> None:
		...
	def _mulMat4(self, mat: Matrix4_) -> Vector3f_:
		...
	def _mulNum(self, num: float) -> Vector3f_:
		...
	def Length(self) -> float:
		...
	def __eq(self, vec: Vector3f_) -> bool:
		...
	def Normalize(self) -> None:
		...
	def _newVec3f(self, vec: Vector3f_) -> Vector3f_:
		...
	def _newNums(self, x: float, y: float, z: float) -> Vector3f_:
		...
	def Project(self, vec: Vector3f_) -> None:
		...
	def __add(self, vec: Vector3f_) -> Vector3f_:
		...
	def __sub(self, vec: Vector3f_) -> Vector3f_:
		...

Vector3f = Vector3f_