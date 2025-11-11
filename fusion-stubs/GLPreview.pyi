from GLView import GLView

class GLPreview:

    #---Properties---#
    View: GLView
    """
    Represents the display GLView for this Preview

    Use the GLView object this gives you to control the display view.

    Read Only
    """


    #---Registry---#
    REGI_ClassType: int

    REGB_ControlView: bool

    REGB_CreateFramePreview: bool

    REGB_CreateStaticPreview: bool

    REGB_Hide: bool

    REGS_ID: str

    REGS_Name: str

    REGB_Preview_CanNetRender: bool

    REGB_Preview_CanCopyAnim: bool

    REGB_Preview_CanRecord: bool

    REGB_Preview_UsesFilenames: bool

    REGB_Preview_CanSaveImage: bool

    REGB_Preview_CanSaveAnim: bool

    REGB_Preview_CanPlayAnim: bool

    REGB_Preview_CanCopyImage: bool

    REGB_Preview_CanDisplayImage: bool

    REGB_Preview_CanCreateAnim: bool

    REGI_Priority: int

    REGB_SupportsDoD: bool

    REGS_UIName: str

    REGB_Unpredictable: bool

    REGI_Version: int

    REGS_VersionString: str

