from IntPixel import _IntPixel


class _IntPixel:

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
	def _newDef(self) -> _IntPixel:
		...
	def info_text(self):
		...
	def Clear(self) -> None:
		...
	def header_text(self):
		...

IntPixel = _IntPixel