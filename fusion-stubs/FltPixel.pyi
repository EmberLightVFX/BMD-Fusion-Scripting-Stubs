class FltPixel:

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
    def Clear(self) -> None:
        ...

    def _newDef(self) -> FltPixel:
        ...

