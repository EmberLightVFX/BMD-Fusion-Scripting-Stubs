class _IntPixel:

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
	def _newDef(self) -> _IntPixel:
		...
	def Clear(self) -> None:
		...

IntPixel = _IntPixel