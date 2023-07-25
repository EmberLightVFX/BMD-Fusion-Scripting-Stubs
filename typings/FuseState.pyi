from TagList import _TagList


class _FuseState:

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
	def info_text(self):
		...
	def _FuRegisterClass(self, id: str, classtype: int, tags: _TagList, filename: str, tpb: str, tpw: int, tph: int, bc: str, bclen: int) -> None:
		...
	def header_text(self):
		...

FuseState = _FuseState