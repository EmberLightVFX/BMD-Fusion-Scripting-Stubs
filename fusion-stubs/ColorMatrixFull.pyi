from ColorMatrix import ColorMatrix


class ColorMatrixFull:

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

	def Inverse(self) -> ColorMatrixFull:
		...

	def IsIdentity(self) -> bool:
		...

	def Offset(self, r: float, g: float, b: float, a: float) -> None:
		...

	def RGBtoYUV(self) -> None:
		...

	def RotA(self, angle: float) -> None:
		...

	def RotB(self, angle: float) -> None:
		...

	def RotG(self, angle: float) -> None:
		...

	def RotR(self, angle: float) -> None:
		...

	def Scale(self, r: float, g: float, b: float, a: float) -> None:
		...

	def YUVtoRGB(self) -> None:
		...

	def __add(self, cm: ColorMatrixFull) -> ColorMatrixFull:
		...

	def __eq(self, cm: ColorMatrixFull) -> bool:
		...

	def _mulCMF(self, cm: ColorMatrixFull) -> ColorMatrixFull:
		...

	def _mulNum(self, num: float) -> ColorMatrixFull:
		...

	def _newCM(self, cm: ColorMatrix) -> ColorMatrixFull:
		...

	def _newCMF(self, cm: ColorMatrixFull) -> ColorMatrixFull:
		...

	def _newDef(self) -> ColorMatrixFull:
		...

