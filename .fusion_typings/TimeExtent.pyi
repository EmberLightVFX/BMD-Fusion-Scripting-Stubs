from _non_existing import TimeStamp_


class TimeExtent_:

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
	def _newDef(self) -> TimeExtent_:
		...
	def info_text(self) -> None:
		...
	def _newNum(self, s: TimeStamp_, e: TimeStamp_, l: TimeStamp_) -> TimeExtent_:
		...
	def header_text(self) -> None:
		...
	def _newExt(self, ext: TimeExtent_) -> TimeExtent_:
		...

TimeExtent = TimeExtent_