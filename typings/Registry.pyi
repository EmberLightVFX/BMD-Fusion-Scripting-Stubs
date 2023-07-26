from typing import Literal

class _Registry:

	#---Properties---#
	m_RegFlags: int
	"""
	Read/Write
	"""
	Parent: _Registry
	"""
	Parent of this Registry node

	Read Only
	"""
	Name: str
	"""
	Friendly name of this Registry node

	Read Only
	"""
	m_ClassFlags: int
	"""
	Read/Write
	"""
	m_ClassType: int
	"""
	Read/Write
	"""
	m_EnvID: int
	"""
	Read/Write
	"""
	m_ID: str
	"""
	Read Only
	"""
	ID: str
	"""
	ID of this Registry node

	Read Only
	"""
	m_Name: str
	"""
	Read Only
	"""
	m_Parent: _Registry
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
	def info_text(self):
		...
	def IsRegClassType(self) -> bool:
		"""
		Returns whether a tool is a particular Registry ClassType
		"""
		...
	def IsClassType(self) -> bool:
		"""
		Returns whether a tool's ID or any of its parent's IDs is a particular Registry ID
		"""
		...
	def header_text(self):
		...
	def GetParent(self) -> _Registry:
		...

Registry = _Registry