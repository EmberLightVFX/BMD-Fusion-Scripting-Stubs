from typing import Literal

from TagList import _TagList


class _ScriptObject:

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
	def _SetAttrs(self, tags: _TagList) -> bool:
		...

ScriptObject = _ScriptObject