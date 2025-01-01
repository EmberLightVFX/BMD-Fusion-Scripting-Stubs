class float16:

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
	def __new(self, f: float) -> float16:
		"""
		float16 constructor

		Args:
			f (float)

		Returns:
			float16
		"""
		...

	def _tofloat16h(self, v: float) -> int:
		...

