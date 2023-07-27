from typing import Any

from TimeExtent import TimeExtent_
from _non_existing import TimeStamp_


class TimeRegion_:

	#---Properties---#
	Start: int
	"""
	Read Only
	"""
	End: int
	"""
	Read Only
	"""

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def _UnionRgn(self, rgn: TimeRegion_) -> None:
		...
	def _newString(self, str: str) -> TimeRegion_:
		...
	def _newTR(self, tr: TimeRegion_) -> TimeRegion_:
		...
	def IsEmpty(self) -> bool:
		...
	def header_text(self) -> None:
		...
	def _newDef(self) -> TimeRegion_:
		...
	def info_text(self) -> None:
		...
	def _newNums(self, s: float, e: float, l: float) -> TimeRegion_:
		...
	def FromString(self, str: str) -> None:
		...
	def IsWithin(self, t: TimeStamp_) -> bool:
		...
	def ToFrameString(self) -> str:
		"""
		Returns a string description
		"""
		...
	def ToString(self) -> str:
		...
	def ToTable(self) -> dict[Any, Any]:
		"""
		Returns a table of {start, end} pairs
		"""
		...
	def _IntersectExt(self, ext: TimeExtent_) -> None:
		...
	def FromTable(self, frames: dict[Any, Any]) -> None:
		"""
		Reads a table of {start, end} pairs
		"""
		...
	def _IntersectRgn(self, rgn: TimeRegion_) -> None:
		...
	def FromFrameString(self, frames: str) -> None:
		"""
		Reads a string description
		"""
		...
	def _UnionExt(self, ext: TimeExtent_) -> None:
		...

TimeRegion = TimeRegion_