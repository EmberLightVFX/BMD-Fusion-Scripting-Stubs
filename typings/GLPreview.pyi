from GLView import _GLView


class _GLPreview:

	#---Properties---#
	View: _GLView
	"""
	Represents the display GLView for this Preview

			Use the GLView object this gives you to control the display view.

	Read Only
	"""

	#---Attributes---#
	REGB_Preview_CanSaveImage: bool

	REGB_Preview_CanSaveAnim: bool

	REGB_Preview_CanCopyImage: bool

	REGB_Preview_CanCopyAnim: bool

	REGB_Preview_CanRecord: bool

	REGB_Preview_UsesFilenames: bool

	REGB_Preview_CanNetRender: bool

	REGB_ControlView: bool

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_ID: str

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_VersionString: str

	REGS_UIName: str

	REGB_CreateStaticPreview: bool

	REGS_Name: str

	REGB_CreateFramePreview: bool

	REGI_Priority: int

	REGB_Preview_CanDisplayImage: bool

	REGI_Version: int

	REGB_Preview_CanCreateAnim: bool

	REGB_Preview_CanPlayAnim: bool


GLPreview = _GLPreview