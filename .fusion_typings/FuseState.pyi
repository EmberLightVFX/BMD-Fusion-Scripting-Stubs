from TagList import TagList_


class FuseState_:

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
	def _FuRegisterClass(self, id: str, classtype: int, tags: TagList_, filename: str, tpb: str, tpw: int, tph: int, bc: str, bclen: int) -> None:
		...

FuseState = FuseState_