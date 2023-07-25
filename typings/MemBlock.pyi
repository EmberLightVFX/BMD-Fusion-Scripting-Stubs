from MemBlock MemBlock import _MemBlock MemBlock


class _MemBlock:

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
	def Save(self, filename: str) -> bool:
		...
	def info_text(self):
		...
	def MemBlock(self) -> _MemBlock MemBlock:
		"""
		MemBlock constructor
		"""
		...
	def header_text(self):
		...

MemBlock = _MemBlock