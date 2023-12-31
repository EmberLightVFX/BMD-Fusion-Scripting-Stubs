from typing import Any

class PlayerView_:

	#---Properties---#
	ViewHeight: Any
	ViewWidth: Any
	OriginY: Any
	OriginX: Any
	ImageHeight: Any
	Zoom: Any
	ImageWidth: Any

	#---Attributes---#
	REGS_FileName: str

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
	def Exit(self) -> None:
		...

PlayerView = PlayerView_