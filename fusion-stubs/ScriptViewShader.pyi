from Input import Input
from TagList import TagList
from ViewShadeNode import ViewShadeNode

class ScriptViewShader:

    #---Properties---#
    Height: int
    """
    Read Only
    """

    RealHeight: int
    """
    Read Only
    """

    RealWidth: int
    """
    Read Only
    """

    Width: int
    """
    Read Only
    """

    m_ViewShadeNode: ViewShadeNode


    #---Registry---#
    REGI_ClassType: int

    REGB_ControlView: bool

    REGS_FileName: str

    REGB_Hide: bool

    REGS_ID: str

    REGS_Name: str

    REGI_Priority: int

    REGB_SupportsDoD: bool

    REGS_UIName: str

    REGB_Unpredictable: bool

    REGI_Version: int

    REGS_VersionString: str


    #---Methods---#
    def AddControlPage(self, name: str, tags: TagList) -> int:
        ...

    def _AddInput(self, name: str, id: str, tags: TagList) -> Input:
        ...

