from ColorMatrixFull import ColorMatrixFull

class ColorMatrix:

    #---Properties---#
    TypeName: str
    """
    Read Only
    """

    TypeNamePtr: str
    """
    Read Only
    """

    def_BWeight: float
    """
    Read Only
    """

    def_GWeight: float
    """
    Read Only
    """

    def_RWeight: float
    """
    Read Only
    """


    #---Methods---#
    def Adjoint(self) -> None:
        ...

    def Blend(self, cm: ColorMatrix, blend: float) -> None:
        ...

    def Determinant(self) -> float:
        ...

    def GrayScale(self, rweight: float, gweight: float, bweight: float) -> None:
        ...

    def Hue(self, hue: float, rweight: float, gweight: float, bweight: float) -> None:
        ...

    def Identity(self) -> None:
        ...

    def Inverse(self) -> ColorMatrixFull:
        ...

    def IsIdentity(self) -> bool:
        ...

    def Offset(self, r: float, g: float, b: float) -> None:
        ...

    def RGBtoYUV(self) -> None:
        ...

    def Rotate(self, r: float, g: float, b: float, angle: float) -> None:
        ...

    def RotateWeighted(self, r: float, g: float, b: float, angle: float, rweight: float, gweight: float, bweight: float) -> None:
        ...

    def Saturate(self, sat: float, rweight: float, gweight: float, bweight: float) -> None:
        ...

    def Shear(self, g: float, r: float) -> None:
        ...

    def Tint(self, angle: float, length: float, rweight: float, gweight: float, bweight: float) -> None:
        ...

    def Tint_HighLuma(self, angle: float, len: float) -> None:
        ...

    def Tint_HighLumaBetter(self, angle: float, len: float) -> None:
        ...

    def Tint_LowLuma(self, angle: float, len: float) -> None:
        ...

    def Tint_LowLumaBetter(self, angle: float, len: float) -> None:
        ...

    def YUVtoRGB(self) -> None:
        ...

    def _RotB1(self, angle: float) -> None:
        ...

    def _RotB2(self, s: float, c: float) -> None:
        ...

    def _RotG1(self, angle: float) -> None:
        ...

    def _RotG2(self, s: float, c: float) -> None:
        ...

    def _RotR1(self, angle: float) -> None:
        ...

    def _RotR2(self, s: float, c: float) -> None:
        ...

    def _Scale3(self, r: float, g: float, b: float) -> None:
        ...

    def _Scale4(self, r: float, g: float, b: float, scale: float) -> None:
        ...

    def __add(self, cm: ColorMatrix) -> ColorMatrix:
        ...

    def __eq(self, cm: ColorMatrix) -> bool:
        ...

    def _mulCM(self, cm: ColorMatrix) -> ColorMatrix:
        ...

    def _mulNum(self, num: float) -> ColorMatrix:
        ...

    def _newCM(self, cm: ColorMatrix) -> ColorMatrix:
        ...

    def _newCMF(self, cm: ColorMatrixFull) -> ColorMatrix:
        ...

    def _newDef(self) -> ColorMatrix:
        ...

