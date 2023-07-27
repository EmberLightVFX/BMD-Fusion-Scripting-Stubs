class MemBlock_:

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
	def MemBlock(self) -> MemBlock_:
		"""
		MemBlock constructor
		"""
		...
	def Save(self, filename: str) -> bool:
		...

MemBlock = MemBlock_