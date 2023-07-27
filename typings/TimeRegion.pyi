from typing import Any

from TimeExtent import _TimeExtent
from _non_existing import _TimeStamp


class _TimeRegion:

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
	def _UnionRgn(self, rgn: _TimeRegion) -> None:
		...
	def _newString(self, str: str) -> _TimeRegion:
		...
	def _newTR(self, tr: _TimeRegion) -> _TimeRegion:
		...
	def IsEmpty(self) -> bool:
		...
	def header_text(self):
		...
	def _newDef(self) -> _TimeRegion:
		...
	def info_text(self):
		...
	def _newNums(self, s: float, e: float, l: float) -> _TimeRegion:
		...
	def FromString(self, str: str) -> None:
		...
	def IsWithin(self, t: _TimeStamp) -> bool:
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
	def _IntersectExt(self, ext: _TimeExtent) -> None:
		...
	def FromTable(self, frames: dict[Any, Any]) -> None:
		"""
		Reads a table of {start, end} pairs
		"""
		...
	def _IntersectRgn(self, rgn: _TimeRegion) -> None:
		...
	def FromFrameString(self, frames: str) -> None:
		"""
		Reads a string description
		"""
		...
	def _UnionExt(self, ext: _TimeExtent) -> None:
		...

TimeRegion = _TimeRegion