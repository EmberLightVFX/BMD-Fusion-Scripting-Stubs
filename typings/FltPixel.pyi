from FltPixel import _FltPixel


class _FltPixel:

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
	def _newDef(self) -> _FltPixel:
		...
	def info_text(self):
		...
	def Clear(self) -> None:
		...
	def header_text(self):
		...

FltPixel = _FltPixel