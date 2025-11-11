from Matrix4 import Matrix4
from Vector2 import Vector2

class Shape:

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
    def Clear(self) -> None:
        ...

    def Close(self) -> None:
        ...

    def Copy(self) -> Shape:
        ...

    def ExpandOfShape(self, thick: float, prec: int, fprec: int, mod: bool) -> Shape:
        ...

    def FlattenOfShape(self, prec: int) -> Shape:
        ...

    def GetCount(self) -> int:
        ...

    def IsEmpty(self) -> bool:
        ...

    def IsFlat(self) -> bool:
        ...

    def TransformOfShape(self, mat: Matrix4) -> Shape:
        ...

    def _AddRectangle(self, v1: Vector2, v2: Vector2, round: float, prec: int) -> None:
        ...

    def _BezierTo(self, v1: Vector2, v2: Vector2, v3: Vector2, close: bool) -> None:
        ...

    def _ConicTo(self, v1: Vector2, v2: Vector2, close: bool) -> None:
        ...

    def _FitSourceTo(self, v1: Vector2, v2: Vector2, v3: Vector2, v4: Vector2, keepaspect: bool) -> None:
        ...

    def _FitTo(self, v1: Vector2, v2: Vector2, keepaspect: bool) -> None:
        ...

    def _FlatBezierTo(self, v1: Vector2, v2: Vector2, v3: Vector2, prec: int, close: bool) -> None:
        ...

    def _FlatConicTo(self, v1: Vector2, v2: Vector2, prec: int, close: bool) -> None:
        ...

    def _LineTo(self, v1: Vector2) -> None:
        ...

    def _MoveTo(self, v1: Vector2) -> None:
        ...

    def __new(self) -> Shape:
        """
        Shape constructor

        Returns:
            Shape
        """
        ...

