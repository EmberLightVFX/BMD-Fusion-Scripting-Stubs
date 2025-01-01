from Composition import Composition


class FloatLUTMacroFrame:

	#---Properties---#
	Composition: Composition
	"""
	Represents this frame window's Composition

	The Composition variable represents the Composition object that thisframe window is displaying.

	Read Only
	"""


	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGI_Version: int

	REGS_VersionString: str

