from typing import Literal

class _MemBlock:

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
	def MemBlock(self) -> _MemBlock:
		"""
		MemBlock constructor
		"""
		...
	def Save(self, filename: str) -> bool:
		...

MemBlock = _MemBlock