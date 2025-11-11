from Vector2 import Vector2

class TextStyleFont:

    #---Properties---#
    DoKerning: bool

    DoLigatures: int

    Features: None
    """
    Write Only
    """

    ManualKerning: Vector2

    ManualPositioning: Vector2

    Monospaced: float

    Name: str

    Orientation: int

    Size: float

    SplitLigatures: bool

    Strikeout: bool

    Style: str

    StylisticSet: int

    TypeName: str
    """
    Read Only
    """

    TypeNamePtr: str
    """
    Read Only
    """

    Underline: bool

    UnderlinePosition: int

    Valid: bool


    #---Methods---#
    def MetricsCompatibleWith(self, font: TextStyleFont) -> bool:
        ...

    def SetFeatures(self, features: str) -> None:
        ...

    def __new(self, name: str, style: str, size: float) -> TextStyleFont:
        """
        TextStyleFont constructor

        Args:
            name (str)
            style (str)
            size (float)

        Returns:
            TextStyleFont
        """
        ...

