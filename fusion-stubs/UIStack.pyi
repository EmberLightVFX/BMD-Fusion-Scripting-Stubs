from typing import Any

class UIStack:

    #---Properties---#
    CurrentIndex: Any


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
    def GetCurrentIndex(self) -> None:
        ...

    def SetCurrentIndex(self) -> None:
        ...

