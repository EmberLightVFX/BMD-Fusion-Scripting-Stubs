from float16 float16float32 f import _float16 float16float32 f


class _float16:

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
	def _tofloat16h(self, v: float) -> int:
		...
	def info_text(self):
		...
	def float16(self) -> _float16 float16float32 f:
		"""
		float16 constructor
		"""
		...
	def header_text(self):
		...

float16 = _float16