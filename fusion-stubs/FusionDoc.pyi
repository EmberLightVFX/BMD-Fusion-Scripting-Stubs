from _non_existing import TimeStamp

class FusionDoc:

    #---Properties---#
    AudioFilename: str
    """
    Read Only
    """

    AudioOffset: TimeStamp
    """
    Read Only
    """

    AverageFrameTime: float
    """
    Read Only
    """

    CurrentTime: TimeStamp
    """
    Read Only
    """

    ElapsedTime: float
    """
    Read Only
    """

    Filename: str
    """
    Read Only
    """

    GlobalEnd: TimeStamp
    """
    Read Only
    """

    GlobalStart: TimeStamp
    """
    Read Only
    """

    HiQ: bool
    """
    Read Only
    """

    LastFrameRendered: TimeStamp
    """
    Read Only
    """

    LastFrameTime: float
    """
    Read Only
    """

    Locked: bool
    """
    Read Only
    """

    Modified: bool
    """
    Read Only
    """

    Name: str
    """
    Read Only
    """

    Proxy: bool
    """
    Read Only
    """

    ProxyScale: int
    """
    Read Only
    """

    RenderEnd: TimeStamp
    """
    Read Only
    """

    RenderFlags: int
    """
    Read Only
    """

    RenderStart: TimeStamp
    """
    Read Only
    """

    RenderStep: int
    """
    Read Only
    """

    Rendering: bool
    """
    Read Only
    """

    TimeRemaining: float
    """
    Read Only
    """


    #---Methods---#
    def EndUndo(self, keep: bool) -> None:
        ...

    def StartUndo(self, name: str) -> None:
        ...

