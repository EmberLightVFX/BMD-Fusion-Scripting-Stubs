from LayoutObj LayoutObjTagList tags import _LayoutObj LayoutObjTagList tags


class _LayoutObj:

	#---Properties---#
	m_PosY: int
	"""
	Read/Write
	"""
	m_SizeY: int
	"""
	Read/Write
	"""
	m_SizeX: int
	"""
	Read/Write
	"""
	m_PosX: int
	"""
	Read/Write
	"""

	#---Methods---#
	def LayoutObj(self) -> _LayoutObj LayoutObjTagList tags:
		"""
		LayoutObj constructor
		"""
		...
	def info_text(self):
		...
	def header_text(self):
		...

LayoutObj = _LayoutObj