from TagList import TagList_


class LayoutObj_:

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
	def LayoutObj(self, tags: TagList_) -> LayoutObj_:
		"""
		LayoutObj constructor
		"""
		...

LayoutObj = LayoutObj_