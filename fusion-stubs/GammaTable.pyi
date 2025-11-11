class GammaTable:

    #---Properties---#
    TypeName: str
    """
    Read Only
    """

    TypeNamePtr: str
    """
    Read Only
    """


    #---Methods---#
    def InitNoTable(self, _gain: float, _gamma: float) -> None:
        ...

    def InitTable(self, _gain: float, _gamma: float) -> None:
        ...

    def InitTableFlt(self, _gain: float, _gamma: float) -> None:
        ...

    def Lookup(self, x: int) -> int:
        ...

    def LookupFlt(self, x: float) -> float:
        ...

    def __new(self) -> GammaTable:
        """
        GammaTable constructor

        Returns:
            GammaTable
        """
        ...

