from typing import Any

from TagList import _TagList
from LUT import _LUT


class _LUT:

	#---Properties---#
	m_Maximum: float
	"""
	Read/Write
	"""
	m_MaximumValue: float
	"""
	Read/Write
	"""
	m_Type: int
	"""
	Read/Write
	"""
	m_Minimum: float
	"""
	Read/Write
	"""
	m_MinimumValue: float
	"""
	Read/Write
	"""
	m_Table: Any
	"""
	Read/Write
	"""
	m_NumEntries: int
	"""
	Read/Write
	"""
	m_StartSlope: float
	"""
	Read/Write
	"""
	m_Offset: int
	"""
	Read/Write
	"""
	m_StartIn: float
	"""
	Read/Write
	"""
	m_EndIn: float
	"""
	Read/Write
	"""
	m_EndSlope: float
	"""
	Read/Write
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
	def _newTags(self, tags: _TagList) -> _LUT:
		...
	def info_text(self):
		...
	def EntrySize(self, ty: int) -> int:
		...
	def _newLUT(self, lut: _LUT) -> _LUT:
		...
	def _newNums(self, num: int, ty: int) -> _LUT:
		...
	def Table(self):
		...
	def GetValue(self, inval: float) -> float:
		...
	def header_text(self):
		...

LUT = _LUT