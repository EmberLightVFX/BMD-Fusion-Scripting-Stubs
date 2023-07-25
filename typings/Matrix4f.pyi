from Matrix4f import _Matrix4f


class _Matrix4f:

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
	def info_text(self):
		...
	def _newMat4(self, mat: _Matrix4f) -> _Matrix4f:
		...
	def _newNums(self, a11: float, a12: float, a13: float, a14: float, a21: float, a22: float, a23: float, a24: float, a31: float, a32: float, a33: float, a34: float, a41: float, a42: float, a43: float, a44: float) -> _Matrix4f:
		...
	def _newDef(self) -> _Matrix4f:
		...
	def header_text(self):
		...

Matrix4f = _Matrix4f