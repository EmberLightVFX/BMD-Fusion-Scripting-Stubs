from _non_existing import TimeStamp
from ImageDomain import ImageDomain
from Input import Input
from Operator import Operator
from Output import Output
from Parameter import Parameter
from TagList import TagList
from TimeExtent import TimeExtent

class Request:

    #---Properties---#
    BaseTime: float
    """
    Read Only
    """

    SourceImg: Parameter
    """
    Read Only
    """

    SourceImgValid: TimeExtent
    """
    Read Only
    """

    Time: float
    """
    Read Only
    """


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
    def ClearInputData(self, inp: Input, slot: int) -> bool:
        ...

    def ClearInputFlags(self, inp: Input, flags: int, slot: int) -> bool:
        ...

    def ClearReqFlags(self, flags: int) -> None:
        ...

    def FreeAllInputs(self) -> None:
        ...

    def FreeAllOutputs(self) -> None:
        ...

    def GetBaseTime(self) -> float:
        ...

    def GetDoD(self) -> ImageDomain:
        ...

    def GetFlags(self) -> int:
        ...

    def GetInputAttrs(self, inp: Input, slot: int) -> TagList:
        ...

    def GetInputBaseTime(self, inp: Input, slot: int) -> TimeStamp:
        ...

    def GetInputData(self, inp: Input, slot: int) -> Parameter:
        ...

    def GetInputDataValid(self, inp: Input, slot: int) -> TimeExtent:
        ...

    def GetInputDoD(self, inp: Input, slot: int) -> ImageDomain:
        ...

    def GetInputFlags(self, inp: Input, slot: int) -> int:
        ...

    def GetInputLayer(self, inp: Input, slot: int) -> str:
        ...

    def GetInputRoI(self, inp: Input, slot: int) -> ImageDomain:
        ...

    def GetInputTime(self, inp: Input, slot: int) -> TimeStamp:
        ...

    def GetLayer(self) -> str:
        ...

    def GetOp(self) -> Operator:
        ...

    def GetOutputData(self, out: Output) -> Parameter:
        ...

    def GetOutputDataValid(self, out: Output) -> TimeExtent:
        ...

    def GetPending(self) -> int:
        ...

    def GetPri(self) -> int:
        ...

    def GetRoI(self) -> ImageDomain:
        ...

    def GetTime(self) -> float:
        ...

    def IsCompleted(self) -> bool:
        ...

    def IsFailed(self) -> bool:
        ...

    def IsInputCurrent(self, inp: Input, slot: int) -> bool:
        ...

    def IsInputSet(self, inp: Input, slot: int) -> bool:
        ...

    def IsInteractive(self) -> bool:
        ...

    def IsIntermediate(self) -> bool:
        ...

    def IsNoCache(self) -> bool:
        ...

    def IsNoMotionBlur(self) -> bool:
        ...

    def IsNoPreviewResize(self) -> bool:
        ...

    def IsOutputCurrent(self, out: Output) -> bool:
        ...

    def IsOutputSet(self, out: Output) -> bool:
        ...

    def IsPending(self) -> bool:
        ...

    def IsPlayback(self) -> bool:
        ...

    def IsPreCalc(self) -> bool:
        ...

    def IsPreview(self) -> bool:
        ...

    def IsProcessing(self) -> bool:
        ...

    def IsQuick(self) -> bool:
        ...

    def IsQuiet(self) -> bool:
        ...

    def IsRemote(self) -> bool:
        ...

    def IsSecondaryTime(self) -> bool:
        ...

    def IsSerialised(self) -> bool:
        ...

    def IsStampOnly(self) -> bool:
        ...

    def Lock(self) -> None:
        ...

    def LockInputData(self, inp: Input, slot: int) -> None:
        ...

    def LockOutputData(self, out: Output) -> None:
        ...

    def SetAllOutputsCurrent(self, current: bool) -> bool:
        ...

    def SetInputAttrs(self, inp: Input, tags: TagList, slot: int) -> bool:
        ...

    def SetInputBaseTime(self, inp: Input, t: TimeStamp, slot: int) -> bool:
        ...

    def SetInputCurrent(self, inp: Input, current: bool, slot: int) -> bool:
        ...

    def SetInputData(self, inp: Input, param: Parameter, te: TimeExtent, slot: int, flags: int) -> bool:
        ...

    def SetInputFlags(self, inp: Input, flags: int, slot: int) -> bool:
        ...

    def SetInputLayer(self, inp: Input, layername: str, slot: int) -> bool:
        ...

    def SetInputSelectedLayer(self, inp: Input, layername: str, slot: int, autolayer: str) -> bool:
        ...

    def SetInputTime(self, inp: Input, t: TimeStamp, slot: int) -> bool:
        ...

    def SetOp(self, op: Operator) -> bool:
        ...

    def SetOutputCurrent(self, out: Output, current: bool) -> bool:
        ...

    def SetOutputData(self, out: Output, param: Parameter, te: TimeExtent) -> bool:
        ...

    def SetPri(self, pri: int, pending: int) -> None:
        ...

    def SetReqAttrs(self, tags: TagList) -> None:
        ...

    def SetReqFlags(self, flags: int) -> None:
        ...

    def Unlock(self) -> None:
        ...

    def UnlockInputData(self, inp: Input, slot: int) -> None:
        ...

    def UnlockOutputData(self, out: Output) -> None:
        ...

