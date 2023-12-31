from ColorMatrixFull import ColorMatrixFull_


class ColorMatrix_:

	#---Properties---#
	TypeName: str
	"""
	Read Only
	"""
	def_GWeight: float
	"""
	Read Only
	"""
	def_RWeight: float
	"""
	Read Only
	"""
	TypeNamePtr: str
	"""
	Read Only
	"""
	def_BWeight: float
	"""
	Read Only
	"""

	#---Methods---#
	def Tint_LowLuma(self, angle: float, len: float) -> None:
		...
	def Tint_LowLumaBetter(self, angle: float, len: float) -> None:
		...
	def _RotB1(self, angle: float) -> None:
		...
	def Hue(self, hue: float, rweight: float, gweight: float, bweight: float) -> None:
		...
	def _RotG1(self, angle: float) -> None:
		...
	def header_text(self) -> None:
		...
	def _RotG2(self, s: float, c: float) -> None:
		...
	def Identity(self) -> None:
		...
	def _RotR1(self, angle: float) -> None:
		...
	def _RotR2(self, s: float, c: float) -> None:
		...
	def Determinant(self) -> float:
		...
	def _Scale3(self, r: float, g: float, b: float) -> None:
		...
	def _Scale4(self, r: float, g: float, b: float, scale: float) -> None:
		...
	def _mulCM(self, cm: ColorMatrix_) -> ColorMatrix_:
		...
	def Rotate(self, r: float, g: float, b: float, angle: float) -> None:
		...
	def Inverse(self) -> ColorMatrixFull_:
		...
	def IsIdentity(self) -> bool:
		...
	def Offset(self, r: float, g: float, b: float) -> None:
		...
	def RGBtoYUV(self) -> None:
		...
	def GrayScale(self, rweight: float, gweight: float, bweight: float) -> None:
		...
	def Blend(self, cm: ColorMatrix_, blend: float) -> None:
		...
	def _newDef(self) -> ColorMatrix_:
		...
	def info_text(self) -> None:
		...
	def YUVtoRGB(self) -> None:
		...
	def Adjoint(self) -> None:
		...
	def _mulNum(self, num: float) -> ColorMatrix_:
		...
	def RotateWeighted(self, r: float, g: float, b: float, angle: float, rweight: float, gweight: float, bweight: float) -> None:
		...
	def _newCM(self, cm: ColorMatrix_) -> ColorMatrix_:
		...
	def Saturate(self, sat: float, rweight: float, gweight: float, bweight: float) -> None:
		...
	def __eq(self, cm: ColorMatrix_) -> bool:
		...
	def _RotB2(self, s: float, c: float) -> None:
		...
	def Tint(self, angle: float, length: float, rweight: float, gweight: float, bweight: float) -> None:
		...
	def Shear(self, g: float, r: float) -> None:
		...
	def _newCMF(self, cm: ColorMatrixFull_) -> ColorMatrix_:
		...
	def Tint_HighLuma(self, angle: float, len: float) -> None:
		...
	def __add(self, cm: ColorMatrix_) -> ColorMatrix_:
		...
	def Tint_HighLumaBetter(self, angle: float, len: float) -> None:
		...

ColorMatrix = ColorMatrix_