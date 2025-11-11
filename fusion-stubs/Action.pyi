from typing import Any

class Action:

    #---Properties---#
    Checked: Any

    Disabled: Any

    FullName: Any

    Name: Any

    ShortName: Any

    StatusTip: Any

    StripName: Any

    ToolTip: Any

    Visible: Any


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
    def SetName(self) -> None:
        ...

    def SetOwner(self) -> None:
        ...

    def Update(self) -> None:
        ...

