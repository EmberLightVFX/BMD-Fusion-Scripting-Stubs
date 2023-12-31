class Noise3_:

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
	def info_text(self) -> None:
		...
	def noise(self, x: float, y: float, z: float, octaves: float) -> float:
		...
	def header_text(self) -> None:
		...
	def _noise(self, x: float, y: float, z: float) -> float:
		...
	def Noise3(self) -> Noise3_:
		"""
		Noise3 constructor
		"""
		...

Noise3 = Noise3_