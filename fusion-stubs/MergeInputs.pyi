from Image import Image
from Request import Request
from TagList import TagList
from TransformMatrix import TransformMatrix

class MergeInputs:

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
    def MergeOf(self, req: Request, img: Image, tags: TagList) -> Image:
        ...

    def _Merge_Image(self, req: Request, img: Image, tags: TagList) -> bool:
        ...

    def _Merge_TransformMatrix(self, req: Request, tm: TransformMatrix, tags: TagList) -> bool:
        ...

