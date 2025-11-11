from typing import Any

class UIButton:

    #---Properties---#
    AutoDefault: Any

    AutoExclusive: Any

    AutoRepeat: Any

    AutoRepeatDelay: Any

    AutoRepeatInterval: Any

    Checkable: Any

    Checked: Any

    Default: Any

    Down: Any

    Flat: Any

    Icon: Any
    """
    Write Only
    """

    IconSize: Any

    Text: Any


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
    def AnimateClick(self) -> None:
        ...

    def Click(self) -> None:
        ...

    def GetAutoDefault(self) -> None:
        ...

    def GetAutoExclusive(self) -> None:
        ...

    def GetAutoRepeat(self) -> None:
        ...

    def GetAutoRepeatDelay(self) -> None:
        ...

    def GetAutoRepeatInterval(self) -> None:
        ...

    def GetCheckable(self) -> None:
        ...

    def GetChecked(self) -> None:
        ...

    def GetDefault(self) -> None:
        ...

    def GetDown(self) -> None:
        ...

    def GetFlat(self) -> None:
        ...

    def GetIconSize(self) -> None:
        ...

    def GetText(self) -> None:
        ...

    def SetAutoDefault(self) -> None:
        ...

    def SetAutoExclusive(self) -> None:
        ...

    def SetAutoRepeat(self) -> None:
        ...

    def SetAutoRepeatDelay(self) -> None:
        ...

    def SetAutoRepeatInterval(self) -> None:
        ...

    def SetCheckable(self) -> None:
        ...

    def SetChecked(self) -> None:
        ...

    def SetDefault(self) -> None:
        ...

    def SetDown(self) -> None:
        ...

    def SetFlat(self) -> None:
        ...

    def SetIcon(self) -> None:
        ...

    def SetIconSize(self) -> None:
        ...

    def SetText(self) -> None:
        ...

    def Toggle(self) -> None:
        ...

