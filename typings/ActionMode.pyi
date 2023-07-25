from typing import Any

class _ActionMode:

	#---Properties---#
	EnterPosX: Any
	StartPosY: Any
	StartPosX: Any
	EnterPosY: Any

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

ActionMode = _ActionMode