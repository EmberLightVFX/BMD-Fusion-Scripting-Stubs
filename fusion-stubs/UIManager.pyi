class UIManager:

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
    def AddNotify(self) -> None:
        ...

    def FindWindow(self) -> None:
        ...

    def FindWindows(self) -> None:
        ...

    def GetEvent(self) -> None:
        ...

    def QueueEvent(self) -> None:
        ...

    def RemoveNotify(self) -> None:
        ...

