class IOClass:

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
    def Close(self) -> None:
        ...

    def Flush(self) -> None:
        ...

    def GetFilePos(self) -> None:
        ...

    def GetFileSize(self) -> None:
        ...

    def Read(self) -> None:
        ...

    def ReadLine(self) -> None:
        ...

    def Seek(self) -> None:
        ...

    def Write(self) -> None:
        ...

    def WriteLine(self) -> None:
        ...

