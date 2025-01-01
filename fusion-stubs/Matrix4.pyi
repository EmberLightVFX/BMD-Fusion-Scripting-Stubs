from Vector3f import Vector3f
from Vector4 import Vector4


class Matrix4:

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
	def Adjoint(self) -> None:
		...

	def Determinant(self) -> float:
		...

	def Identity(self) -> None:
		...

	def Inverse(self) -> Matrix4:
		...

	def InverseTranspose(self) -> Matrix4:
		...

	def LookAt(self, eye: Vector4, at: Vector4, up: Vector4) -> None:
		...

	def MapQuad(self, tlX: float, tlY: float, trX: float, trY: float, blX: float, blY: float, brX: float, brY: float) -> bool:
		...

	def Move(self, x: float, y: float, z: float) -> None:
		...

	def Perspective(self, fovy: float, aspect: float, znear: float, zfar: float) -> None:
		...

	def Project(self, persp: float) -> None:
		...

	def ProjectWindow(self, width: float, height: float, znear: float, zfar: float) -> None:
		...

	def RotAxis(self, xaxis: float, yaxis: float, zaxis: float, rad: float) -> None:
		...

	def RotX(self, a: float) -> None:
		...

	def RotY(self, a: float) -> None:
		...

	def RotZ(self, a: float) -> None:
		...

	def Rotate(self, x: float, y: float, z: float, order: str) -> None:
		...

	def Scale(self, x: float, y: float, z: float) -> None:
		...

	def SetIdentity(self) -> None:
		...

	def SetOne(self) -> None:
		...

	def SetZero(self) -> None:
		...

	def Shear(self, x: float, y: float, z: float) -> None:
		...

	def TransformNormal(self, norm: Vector3f) -> Vector3f:
		...

	def TransformPoint(self, out: Vector4, inp: Vector4) -> None:
		...

	def Transpose(self) -> Matrix4:
		...

	def _Ortho3(self, width: float, height: float, depth: float) -> None:
		...

	def _Ortho6(self, xmin: float, xmax: float, ymin: float, ymax: float, zmin: float, zmax: float) -> None:
		...

	def __mul(self, mat: Matrix4) -> Matrix4:
		...

	def _newDef(self) -> Matrix4:
		...

	def _newMat4(self, mat: Matrix4) -> Matrix4:
		...

	def _newNums(self, a11: float, a12: float, a13: float, a14: float, a21: float, a22: float, a23: float, a24: float, a31: float, a32: float, a33: float, a34: float, a41: float, a42: float, a43: float, a44: float) -> Matrix4:
		...

