from FltPixel import FltPixel
from Gradient import Gradient
from Image import Image
from Matrix4 import Matrix4

class ChannelStyle:

    #---Properties---#
    BevelType: str

    BgColor: FltPixel

    BlurType: str

    Color: FltPixel

    ColorGradient: Gradient

    ColorImage: Image

    ColorImageBevel: Image

    ColorImageEdges: str

    ColorImageSample: str

    ColorMapping: int

    ColorMappingAngle: float

    ColorMappingAspect: float

    ColorMappingSize: float

    ImageTransform: Matrix4

    Level: str

    Opacity: float

    SoftnessBlend: float

    SoftnessGlow: float

    SoftnessImage: bool

    SoftnessX: float

    SoftnessY: float

    Type: str

    TypeName: str
    """
    Read Only
    """

    TypeNamePtr: str
    """
    Read Only
    """


    #---Methods---#
    def GetImageTransformInverse(self) -> Matrix4:
        ...

    def IsRenderCompatibleWith(self, cs: ChannelStyle) -> bool:
        ...

    def RequiresNewImage(self, line: int, tab: int, word: int, ch: int) -> bool:
        ...

    def __new(self) -> ChannelStyle:
        """
        ChannelStyle constructor

        Returns:
            ChannelStyle
        """
        ...

