from _non_existing import TimeStamp


class TimeExtent:

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
	def _newDef(self) -> TimeExtent:
		...

	def _newExt(self, ext: TimeExtent) -> TimeExtent:
		...

	def _newNum(self, s: TimeStamp, e: TimeStamp, l: TimeStamp) -> TimeExtent:
		...

