from typing import Any, Literal

from TagList import _TagList


class _LUT:

	#---Properties---#
	m_EndIn: float
	"""
	Read/Write
	"""
	m_EndSlope: float
	"""
	Read/Write
	"""
	m_Maximum: float
	"""
	Read/Write
	"""
	m_MaximumValue: float
	"""
	Read/Write
	"""
	m_StartIn: float
	"""
	Read/Write
	"""
	m_Minimum: float
	"""
	Read/Write
	"""
	m_Type: int
	"""
	Read/Write
	"""
	m_MinimumValue: float
	"""
	Read/Write
	"""
	m_StartSlope: float
	"""
	Read/Write
	"""
	m_NumEntries: int
	"""
	Read/Write
	"""
	m_Table: Any
	"""
	Read/Write
	"""
	m_Offset: int
	"""
	Read/Write
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
	def GetValue(self, inval: float) -> float:
		...
	def info_text(self):
		...
	def _newLUT(self, lut: _LUT) -> _LUT:
		...
	def Table(self):
		...
	def header_text(self):
		...
	def EntrySize(self, ty: int) -> int:
		...
	def _newNums(self, num: int, ty: int) -> _LUT:
		...
	def _newTags(self, tags: _TagList) -> _LUT:
		...

LUT = _LUT