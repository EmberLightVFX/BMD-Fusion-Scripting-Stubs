class FillStyle:

    #---Properties---#
    AdaptToPerspective: bool

    CleanIntersections: bool

    ExpandType: str

    JoinType: str

    LineType: str

    MiterLimit: float

    OutsideOnly: bool

    Overlap: str

    RelativeThickness: float

    Thickness: float

    Type: str

    TypeName: str
    """
    Read Only
    """

    TypeNamePtr: str
    """
    Read Only
    """


    #---Methods---#
    def ActualThickness(self) -> float:
        ...

    def IsTraceCompatibleWith(self, style: FillStyle) -> bool:
        ...

    def __new(self) -> FillStyle:
        """
        FillStyle constructor

        Returns:
            FillStyle
        """
        ...

