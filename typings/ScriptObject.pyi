from TagList import _TagList


class _ScriptObject:

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
	def _SetAttrs(self, tags: _TagList) -> bool:
		...
	def info_text(self):
		...
	def header_text(self):
		...

ScriptObject = _ScriptObject