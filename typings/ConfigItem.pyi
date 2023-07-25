from typing import Any

class _ConfigItem:

	#---Properties---#
	Owner: Any
	"""
	Read/Write
	"""
	ID: Any
	"""
	Read/Write
	"""
	Source: Any
	"""
	Read Only
	"""
	UID: Any
	"""
	Read/Write
	"""
	Info: Any
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
	def Set(self):
		...
	def Get(self):
		...
	def header_text(self):
		...

ConfigItem = _ConfigItem