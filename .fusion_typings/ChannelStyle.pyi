from Matrix4 import Matrix4_
from FltPixel import FltPixel_
from Gradient import Gradient_
from Image import Image_


class ChannelStyle_:

	#---Properties---#
	ColorMappingAspect: float
	"""
	Read/Write
	"""
	ColorMappingSize: float
	"""
	Read/Write
	"""
	ImageTransform: Matrix4_
	"""
	Read/Write
	"""
	Level: str
	"""
	Read/Write
	"""
	BevelType: str
	"""
	Read/Write
	"""
	BgColor: FltPixel_
	"""
	Read/Write
	"""
	SoftnessGlow: float
	"""
	Read/Write
	"""
	BlurType: str
	"""
	Read/Write
	"""
	SoftnessImage: bool
	"""
	Read/Write
	"""
	Color: FltPixel_
	"""
	Read/Write
	"""
	ColorGradient: Gradient_
	"""
	Read/Write
	"""
	SoftnessY: float
	"""
	Read/Write
	"""
	Opacity: float
	"""
	Read/Write
	"""
	ColorImage: Image_
	"""
	Read/Write
	"""
	SoftnessX: float
	"""
	Read/Write
	"""
	ColorImageBevel: Image_
	"""
	Read/Write
	"""
	Type: str
	"""
	Read/Write
	"""
	ColorImageEdges: str
	"""
	Read/Write
	"""
	TypeName: str
	"""
	Read Only
	"""
	ColorImageSample: str
	"""
	Read/Write
	"""
	SoftnessBlend: float
	"""
	Read/Write
	"""
	ColorMapping: int
	"""
	Read/Write
	"""
	TypeNamePtr: str
	"""
	Read Only
	"""
	ColorMappingAngle: float
	"""
	Read/Write
	"""

	#---Methods---#
	def GetImageTransformInverse(self) -> Matrix4_:
		...
	def info_text(self) -> None:
		...
	def IsRenderCompatibleWith(self, cs: ChannelStyle_) -> bool:
		...
	def header_text(self) -> None:
		...
	def RequiresNewImage(self, line: int, tab: int, word: int, ch: int) -> bool:
		...
	def ChannelStyle(self) -> ChannelStyle_:
		"""
		ChannelStyle constructor
		"""
		...

ChannelStyle = ChannelStyle_