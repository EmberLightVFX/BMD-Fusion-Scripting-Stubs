from typing import Any

class ConfigItem_:

	#---Properties---#
	Owner: Any
	"""
	Read/Write
	"""
	UID: Any
	"""
	Read/Write
	"""
	Source: Any
	"""
	Read Only
	"""
	ID: Any
	"""
	Read/Write
	"""
	Info: Any
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
	def header_text(self):
		...
	def Set(self):
		...
	def Get(self):
		...

ConfigItem = ConfigItem_