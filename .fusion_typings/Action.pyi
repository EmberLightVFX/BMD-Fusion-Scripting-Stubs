from typing import Any

class Action_:

	#---Properties---#
	FullName: Any
	"""
	Read/Write
	"""
	Name: Any
	"""
	Read/Write
	"""
	ToolTip: Any
	"""
	Read/Write
	"""
	Checked: Any
	"""
	Read/Write
	"""
	ShortName: Any
	"""
	Read/Write
	"""
	StripName: Any
	"""
	Read/Write
	"""
	Visible: Any
	"""
	Read/Write
	"""
	Disabled: Any
	"""
	Read/Write
	"""
	StatusTip: Any
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

	REGB_Utility_Toggle: bool

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def header_text(self) -> None:
		...
	def SetName(self) -> None:
		...
	def SetOwner(self) -> None:
		...
	def Update(self) -> None:
		...

Action = Action_