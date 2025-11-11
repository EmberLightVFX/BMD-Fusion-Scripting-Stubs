from Parameter import Parameter
from Request import Request

class Output:

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
    def _SetNum(self, req: Request, num: float) -> None:
        ...

    def _SetParam(self, req: Request, param: Parameter) -> None:
        ...

