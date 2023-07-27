from TagList import _TagList


class _LayoutObj:

	#---Properties---#
	m_SizeX: int
	"""
	Read/Write
	"""
	m_SizeY: int
	"""
	Read/Write
	"""
	m_PosY: int
	"""
	Read/Write
	"""
	m_PosX: int
	"""
	Read/Write
	"""

	#---Methods---#
	def header_text(self):
		...
	def info_text(self):
		...
	def LayoutObj(self, tags: _TagList) -> _LayoutObj:
		"""
		LayoutObj constructor
		"""
		...

LayoutObj = _LayoutObj