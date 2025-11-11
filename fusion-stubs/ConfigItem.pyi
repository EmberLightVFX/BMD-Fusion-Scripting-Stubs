from typing import Any

class ConfigItem:

    #---Properties---#
    ID: Any

    Info: Any

    Owner: Any

    Source: Any

    UID: Any


    #---Registry---#
    REGI_ClassType: int

    REGB_ControlView: bool

    REGB_Hide: bool

    REGS_ID: str

    REGS_Name: str

    REGI_Priority: int

    REGB_SupportsDoD: bool

    REGB_Unpredictable: bool

    REGI_Version: int

    REGS_VersionString: str


    #---Methods---#
    def Get(self) -> None:
        ...

    def Set(self) -> None:
        ...

