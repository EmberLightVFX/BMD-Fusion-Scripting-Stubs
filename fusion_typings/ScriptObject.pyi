from TagList import TagList_


class ScriptObject_:

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
	def _SetAttrs(self, tags: TagList_) -> bool:
		...

ScriptObject = ScriptObject_