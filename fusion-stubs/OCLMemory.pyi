from Image import Image

class OCLMemory:

    #---Methods---#
    def Download(self, img: Image) -> bool:
        ...

    def ObtainCLObject(self, wait: bool) -> bool:
        ...

    def Release(self) -> bool:
        ...

    def ReleaseCLObject(self) -> bool:
        ...

    def __new(self) -> OCLMemory:
        """
        OCLMemory constructor

        Returns:
            OCLMemory
        """
        ...

