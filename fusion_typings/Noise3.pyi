class _Noise3:

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
	def info_text(self):
		...
	def noise(self, x: float, y: float, z: float, octaves: float) -> float:
		...
	def header_text(self):
		...
	def _noise(self, x: float, y: float, z: float) -> float:
		...
	def Noise3(self) -> _Noise3:
		"""
		Noise3 constructor
		"""
		...

Noise3 = _Noise3