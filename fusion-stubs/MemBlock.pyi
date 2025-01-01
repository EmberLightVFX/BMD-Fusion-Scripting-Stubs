class MemBlock:

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
	def Save(self, filename: str) -> bool:
		...

	def __new(self) -> MemBlock:
		"""
		MemBlock constructor

		Returns:
			MemBlock
		"""
		...

