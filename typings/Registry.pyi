from typing import Any

from Registry import _Registry
from object import _object


class _Registry:

	#---Properties---#
	m_ClassFlags: int
	"""
	Read/Write
	"""
	m_ClassType: int
	"""
	Read/Write
	"""
	Parent: _Registry
	"""
	Parent of this Registry node

	Read Only
	"""
	m_EnvID: int
	"""
	Read/Write
	"""
	m_RegFlags: int
	"""
	Read/Write
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
	m_ID: str
	"""
	Read Only
	"""
	m_Parent: _Registry
	"""
	Read Only
	"""
	Name: str
	"""
	Friendly name of this Registry node

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
	def GetParent(self) -> _Registry:
		...
	def info_text(self):
		...
	def New(self, object_saved_settings: dict[Any, Any] = dict[Any, Any]()) -> _object:
		"""
		Returns a new instance of this class type
		"""
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

Registry = _Registry