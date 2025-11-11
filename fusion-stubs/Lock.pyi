class Lock:

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
    def ObtainLock(self) -> None:
        ...

    def ReleaseLock(self) -> None:
        ...

