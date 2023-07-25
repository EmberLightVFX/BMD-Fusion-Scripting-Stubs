from TimeExtent import _TimeExtent
from TimeStamp import _TimeStamp


class _TimeExtent:

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
	def _newExt(self, ext: _TimeExtent) -> _TimeExtent:
		...
	def _newNum(self, s: _TimeStamp, e: _TimeStamp, l: _TimeStamp) -> _TimeExtent:
		...
	def info_text(self):
		...
	def _newDef(self) -> _TimeExtent:
		...
	def header_text(self):
		...

TimeExtent = _TimeExtent