from _non_existing import _TimeStamp


class _TimeExtent:

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
	def _newDef(self) -> _TimeExtent:
		...
	def info_text(self):
		...
	def _newNum(self, s: _TimeStamp, e: _TimeStamp, l: _TimeStamp) -> _TimeExtent:
		...
	def header_text(self):
		...
	def _newExt(self, ext: _TimeExtent) -> _TimeExtent:
		...

TimeExtent = _TimeExtent