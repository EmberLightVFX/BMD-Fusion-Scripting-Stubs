from Composition import Composition_


class FloatLUTMacroFrame_:

	#---Properties---#
	Composition: Composition_
	"""
	Represents this frame window's Composition

	The Composition variable represents the Composition object that thisframe window is displaying.

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


FloatLUTMacroFrame = FloatLUTMacroFrame_