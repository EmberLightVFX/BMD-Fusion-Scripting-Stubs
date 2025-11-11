from FusionDoc import FusionDoc
from Image import Image
from OCLManager import OCLManager
from OCLMemory import OCLMemory

class OCLProgram:

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
    def Build(self, wait: bool, opts: str) -> bool:
        ...

    def CopyToBuffer(self, img: Image, mem: OCLMemory, offset: int, wait: bool) -> int:
        ...

    def CreateKernel(self, name: str) -> int:
        ...

    def Lock(self) -> None:
        ...

    def Release(self) -> None:
        ...

    def ReleaseMemory(self, mem: OCLMemory) -> bool:
        ...

    def RunKernel(self, index: int, block: bool) -> bool:
        ...

    def SetSize(self, xsize: int, ysize: int) -> None:
        ...

    def SetWorkgroupSize(self, xsize: int, ysize: int) -> None:
        ...

    def WaitForBuild(self, timeout: int) -> bool:
        ...

    def __new(self, mgr: OCLManager, doc: FusionDoc, src: str, len: int) -> OCLProgram:
        """
        OCLProgram constructor

        Args:
            mgr (OCLManager)
            doc (FusionDoc)
            src (str)
            len (int)

        Returns:
            OCLProgram
        """
        ...

