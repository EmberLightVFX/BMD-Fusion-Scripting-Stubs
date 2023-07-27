from TagList import _TagList


class _FuseState:

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
	def _FuRegisterClass(self, id: str, classtype: int, tags: _TagList, filename: str, tpb: str, tpw: int, tph: int, bc: str, bclen: int) -> None:
		...

FuseState = _FuseState