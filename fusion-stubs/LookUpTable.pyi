from LUT import LUT
from Object import Object
from TagList import TagList

class LookUpTable:

    #---Registry---#
    REGI_ClassType: int

    REGB_ControlView: bool

    REGB_Hide: bool

    REGS_ID: str

    REGS_Name: str

    REGI_Priority: int

    REGB_SupportsDoD: bool

    REGB_Unpredictable: bool

    REGB_Utility_Toggle: bool

    REGI_Version: int

    REGS_VersionString: str


    #---Methods---#
    def Attach(self, obj: Object) -> None:
        ...

    def Detach(self) -> None:
        ...

    def GetTable(self, tags: TagList) -> LUT:
        ...

    def GetValue(self, inval: float) -> float:
        ...

    def IsOneToOne(self) -> bool:
        ...

    def SetOneToOne(self, set: bool) -> None:
        ...

    def _newCopy(self, lut: LookUpTable) -> LookUpTable:
        ...

    def _newDef(self) -> LookUpTable:
        ...

    def _newLUT(self, lut: LUT, id: str) -> LookUpTable:
        ...

