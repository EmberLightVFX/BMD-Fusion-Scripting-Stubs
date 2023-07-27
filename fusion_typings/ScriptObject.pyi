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
	def header_text(self):
		...
	def info_text(self):
		...
	def _SetAttrs(self, tags: TagList_) -> bool:
		...

ScriptObject = ScriptObject_