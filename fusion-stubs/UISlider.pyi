from typing import Any

class UISlider:

    #---Properties---#
    InvertedAppearance: Any

    InvertedControls: Any

    Maximum: Any

    Minimum: Any

    Orientation: Any

    PageStep: Any

    SingleStep: Any

    SliderDown: Any

    SliderPosition: Any

    TickInterval: Any

    TickPosition: Any

    Tracking: Any

    Value: Any


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
    def GetInvertedAppearance(self) -> None:
        ...

    def GetInvertedControls(self) -> None:
        ...

    def GetMaximum(self) -> None:
        ...

    def GetMinimum(self) -> None:
        ...

    def GetOrientation(self) -> None:
        ...

    def GetPageStep(self) -> None:
        ...

    def GetSingleStep(self) -> None:
        ...

    def GetSliderDown(self) -> None:
        ...

    def GetSliderPosition(self) -> None:
        ...

    def GetTickInterval(self) -> None:
        ...

    def GetTickPosition(self) -> None:
        ...

    def GetTracking(self) -> None:
        ...

    def GetValue(self) -> None:
        ...

    def SetInvertedAppearance(self) -> None:
        ...

    def SetInvertedControls(self) -> None:
        ...

    def SetMaximum(self) -> None:
        ...

    def SetMinimum(self) -> None:
        ...

    def SetOrientation(self) -> None:
        ...

    def SetPageStep(self) -> None:
        ...

    def SetRange(self) -> None:
        ...

    def SetSingleStep(self) -> None:
        ...

    def SetSliderDown(self) -> None:
        ...

    def SetSliderPosition(self) -> None:
        ...

    def SetTickInterval(self) -> None:
        ...

    def SetTickPosition(self) -> None:
        ...

    def SetTracking(self) -> None:
        ...

    def SetValue(self) -> None:
        ...

    def TriggerAction(self) -> None:
        ...

