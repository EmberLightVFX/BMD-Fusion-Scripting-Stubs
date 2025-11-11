from typing import Any

class UIActionStrip:

    #---Properties---#
    ActionFlags: Any

    ZonesPerSide: Any


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
    def AddButton(self) -> None:
        ...

    def AddEdit(self) -> None:
        ...

    def AddPopup(self) -> None:
        ...

    def AddSlider(self) -> None:
        ...

    def BeginZone(self) -> None:
        ...

    def EndZone(self) -> None:
        ...

    def FindZone(self) -> None:
        ...

    def GetActionFlags(self) -> None:
        ...

    def GetNextID(self) -> None:
        ...

    def GetZonesPerSide(self) -> None:
        ...

    def Remove(self) -> None:
        ...

    def SetActionFlags(self) -> None:
        ...

    def SetTarget(self) -> None:
        ...

    def SetZonesPerSide(self) -> None:
        ...

    def Update(self) -> None:
        ...

