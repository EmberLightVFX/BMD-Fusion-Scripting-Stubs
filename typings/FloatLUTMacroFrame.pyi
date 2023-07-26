from Composition import _Composition


class _FloatLUTMacroFrame:

	#---Properties---#
	Composition: _Composition
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


FloatLUTMacroFrame = _FloatLUTMacroFrame