from typing import Any

from FltPixel import FltPixel

class Gradient:

    #---Properties---#
    Value: dict[Any, Any]
    """
    The gradient in table form

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
    def AddColor(self, pos: float, pix: FltPixel) -> None:
        ...

    def AddRGBA(self, pos: float, r: float, g: float, b: float, a: float) -> None:
        ...

    def Clear(self) -> None:
        ...

    def ClearTables(self) -> None:
        ...

    def GetColor(self, pos: float) -> FltPixel:
        ...

    def GetColorCount(self) -> int:
        ...

    def QuickEvaluate(self, pos: float, cstr: str) -> FltPixel:
        ...

    def SetPreset(self, pstr: str) -> None:
        ...

    def _newGrad(self, grad: Gradient) -> Gradient:
        ...

    def _newPreset(self, pstr: str) -> Gradient:
        ...

