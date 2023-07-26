from typing import Literal

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
	REGB_Preview_CanRecord: bool

	REGB_Preview_UsesFilenames: bool

	REGB_Preview_CanNetRender: bool

	REGB_ControlView: bool

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_ID: str

	REGS_VersionString: str

	REGS_UIName: str

	REGS_Name: str

	REGI_Version: int

	REGB_CreateStaticPreview: bool

	REGB_SupportsDoD: bool

	REGB_CreateFramePreview: bool

	REGI_Priority: int

	REGB_Preview_CanDisplayImage: bool

	REGB_Hide: bool

	REGB_Preview_CanCreateAnim: bool

	REGB_Preview_CanPlayAnim: bool

	REGB_Preview_CanSaveImage: bool

	REGB_Preview_CanSaveAnim: bool

	REGB_Preview_CanCopyImage: bool

	REGB_Preview_CanCopyAnim: bool


GLPreview = _GLPreview