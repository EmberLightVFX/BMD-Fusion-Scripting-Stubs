class Noise3:

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
	def __new(self) -> Noise3:
		"""
		Noise3 constructor

		Returns:
			Noise3
		"""
		...

	def _noise(self, x: float, y: float, z: float) -> float:
		...

	def noise(self, x: float, y: float, z: float, octaves: float) -> float:
		...

