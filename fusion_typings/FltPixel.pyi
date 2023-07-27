class FltPixel_:

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
	def header_text(self) -> None:
		...
	def info_text(self) -> None:
		...
	def _newDef(self) -> FltPixel_:
		...
	def Clear(self) -> None:
		...

FltPixel = FltPixel_