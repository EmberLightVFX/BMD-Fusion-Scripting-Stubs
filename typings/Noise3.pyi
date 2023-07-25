from Noise3 Noise3 import _Noise3 Noise3


class _Noise3:

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
	def noise(self, x: float, y: float, z: float, octaves: float) -> float:
		...
	def Noise3(self) -> _Noise3 Noise3:
		"""
		Noise3 constructor
		"""
		...
	def _noise(self, x: float, y: float, z: float) -> float:
		...
	def header_text(self):
		...

Noise3 = _Noise3