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


FloatLUTMacroFrame = _FloatLUTMacroFrame