class float16_:

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
	def header_text(self):
		...
	def info_text(self):
		...
	def _tofloat16h(self, v: float) -> int:
		...
	def float16(self, f: float) -> float16_:
		"""
		float16 constructor
		"""
		...

float16 = float16_