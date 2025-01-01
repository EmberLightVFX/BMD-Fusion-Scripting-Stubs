from TagList import TagList


class FuseState:

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
	def _FuRegisterClass(self, id: str, classtype: int, tags: TagList, filename: str, tpb: str, tpw: int, tph: int, bc: str, bclen: int) -> None:
		...

