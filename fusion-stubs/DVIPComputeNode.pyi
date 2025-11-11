from _non_existing import void
from Image import Image
from Request import Request

class DVIPComputeNode:

    #---Methods---#
    def AddInput(self, name: str, img: Image) -> None:
        ...

    def AddOutput(self, name: str, img: Image) -> None:
        ...

    def AddSampler(self, name: str, filterMode: int, addressMode: int, normCoordsMode: int) -> None:
        ...

    def ForceRebuild(self) -> None:
        ...

    def GetErrorLog(self) -> str:
        ...

    def GetKernelName(self) -> str:
        ...

    def GetKernelParams(self) -> str:
        ...

    def GetParamsHash(self, paramStr: str) -> int:
        ...

    def RunSession(self, req: Request) -> bool:
        ...

    def SetGlobalSize(self, w: int, h: int, d: int) -> None:
        ...

    def SetParamStructCopy(self, params: void, size: int) -> None:
        ...

    def SetWorkSize(self, w: int, h: int, d: int) -> None:
        ...

    def __new(self, req: Request, kernelName: str, source: str, kernelParamsName: str, kernelParams: str) -> DVIPComputeNode:
        """
        DVIPComputeNode constructor

        Args:
            req (Request)
            kernelName (str)
            source (str)
            kernelParamsName (str)
            kernelParams (str)

        Returns:
            DVIPComputeNode
        """
        ...

