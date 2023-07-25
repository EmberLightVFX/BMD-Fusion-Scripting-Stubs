from typing import Any

from TimeRegion import _TimeRegion
from TimeExtent import _TimeExtent
from TimeStamp import _TimeStamp


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
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_VersionString: str

	REGS_ID: str

	REGB_ControlView: bool

	REGI_Priority: int


	#---Methods---#
	def _IntersectRgn(self, rgn: _TimeRegion) -> None:
		...
	def _UnionExt(self, ext: _TimeExtent) -> None:
		...
	def _UnionRgn(self, rgn: _TimeRegion) -> None:
		...
	def IsEmpty(self) -> bool:
		...
	def _newString(self, str: str) -> _TimeRegion:
		...
	def _newTR(self, tr: _TimeRegion) -> _TimeRegion:
		...
	def FromTable(self, frames: dict[Any, Any]) -> None:
		"""
		Reads a table of {start, end} pairs
		"""
		...
	def ToTable(self) -> dict[Any, Any]:
		"""
		Returns a table of {start, end} pairs
		"""
		...
	def FromFrameString(self, frames: str) -> None:
		"""
		Reads a string description
		"""
		...
	def ToFrameString(self) -> str:
		"""
		Returns a string description
		"""
		...
	def FromString(self, str: str) -> None:
		...
	def _newDef(self) -> _TimeRegion:
		...
	def IsWithin(self, t: _TimeStamp) -> bool:
		...
	def header_text(self):
		...
	def _newNums(self, s: float, e: float, l: float) -> _TimeRegion:
		...
	def ToString(self) -> str:
		...
	def _IntersectExt(self, ext: _TimeExtent) -> None:
		...
	def info_text(self):
		...

TimeRegion = _TimeRegion