from TextStyleFont import TextStyleFont

class TextStyleFontMetrics:

    #---Properties---#
    CharWidthAverage: float

    CharWidthSpace: float

    DoStrikeout: bool

    DoUnderline: bool

    FontSize: float

    Scale: float

    StrikeoutOffset: float

    StrikeoutThickness: float

    TextAscent: float

    TextDescent: float

    TextExternalLeading: float

    TextInternalLeading: float

    TypeName: str
    """
    Read Only
    """

    TypeNamePtr: str
    """
    Read Only
    """

    UnderlineOffsetH: float

    UnderlineThickness: float


    #---Methods---#
    def CalcCharacterWidth(self, ch: int) -> float:
        ...

    def CharacterKerning(self, first: str, second: str) -> float:
        ...

    def CharacterWidth(self, ch: str) -> float:
        ...

    def GetError(self) -> int:
        ...

    def WordWidth(self, str: str, direction: int) -> float:
        ...

    def __new(self, font: TextStyleFont, direction: int) -> TextStyleFontMetrics:
        """
        TextStyleFontMetrics constructor

        Args:
            font (TextStyleFont)
            direction (int)

        Returns:
            TextStyleFontMetrics
        """
        ...

