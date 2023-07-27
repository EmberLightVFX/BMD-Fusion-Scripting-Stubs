class IntPixel_:

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
	def _newDef(self) -> IntPixel_:
		...
	def Clear(self) -> None:
		...

IntPixel = IntPixel_