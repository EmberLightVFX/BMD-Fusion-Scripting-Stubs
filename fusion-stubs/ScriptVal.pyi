from _non_existing import ScriptValType

class ScriptVal:

    #---Properties---#
    TypeName: str
    """
    Read Only
    """

    TypeNamePtr: str
    """
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

    REGB_Utility_Toggle: bool

    REGI_Version: int

    REGS_VersionString: str


    #---Methods---#
    def Type(self) -> ScriptValType:
        ...

    def _newDef(self) -> ScriptVal:
        ...

    def _newScriptVal(self, sv: ScriptVal) -> ScriptVal:
        ...

