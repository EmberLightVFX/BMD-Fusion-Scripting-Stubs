from typing import Any

class _Action:

	#---Properties---#
	StripName: Any
	"""
	Read/Write
	"""
	ToolTip: Any
	"""
	Read/Write
	"""
	Disabled: Any
	"""
	Read/Write
	"""
	Visible: Any
	"""
	Read/Write
	"""
	FullName: Any
	"""
	Read/Write
	"""
	Checked: Any
	"""
	Read/Write
	"""
	StatusTip: Any
	"""
	Read/Write
	"""
	Name: Any
	"""
	Read/Write
	"""
	ShortName: Any
	"""
	Read/Write
	"""

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGS_VersionString: str

	REGI_ClassType: int

	REGI_Priority: int

	REGB_ControlView: bool

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGB_Unpredictable: bool


	#---Methods---#
	def Update(self):
		...
	def SetName(self):
		...
	def SetOwner(self):
		...
	def header_text(self):
		...

Action = _Action