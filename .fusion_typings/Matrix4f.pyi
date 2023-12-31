class Matrix4f_:

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
	def _newDef(self) -> Matrix4f_:
		...
	def info_text(self) -> None:
		...
	def _newMat4(self, mat: Matrix4f_) -> Matrix4f_:
		...
	def _newNums(self, a11: float, a12: float, a13: float, a14: float, a21: float, a22: float, a23: float, a24: float, a31: float, a32: float, a33: float, a34: float, a41: float, a42: float, a43: float, a44: float) -> Matrix4f_:
		...
	def header_text(self) -> None:
		...

Matrix4f = Matrix4f_