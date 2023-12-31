from typing import Any

class ActionMode_:

	#---Properties---#
	StartPosX: Any
	EnterPosY: Any
	EnterPosX: Any
	StartPosY: Any

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
	def header_text(self) -> None:
		...
	def Set(self) -> None:
		...
	def Get(self) -> None:
		...

ActionMode = ActionMode_