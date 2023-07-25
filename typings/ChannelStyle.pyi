from Image import _Image
from Matrix4 import _Matrix4
from FltPixel import _FltPixel
from Gradient import _Gradient
from ChannelStyle ChannelStyle import _ChannelStyle ChannelStyle
from ChannelStyle import _ChannelStyle


class _ChannelStyle:

	#---Properties---#
	ColorImage: _Image
	"""
	Read/Write
	"""
	ColorImageBevel: _Image
	"""
	Read/Write
	"""
	ColorImageEdges: str
	"""
	Read/Write
	"""
	ColorImageSample: str
	"""
	Read/Write
	"""
	ColorMapping: int
	"""
	Read/Write
	"""
	ColorMappingAngle: float
	"""
	Read/Write
	"""
	BlurType: str
	"""
	Read/Write
	"""
	ColorMappingAspect: float
	"""
	Read/Write
	"""
	TypeNamePtr: str
	"""
	Read Only
	"""
	ColorMappingSize: float
	"""
	Read/Write
	"""
	TypeName: str
	"""
	Read Only
	"""
	ImageTransform: _Matrix4
	"""
	Read/Write
	"""
	SoftnessGlow: float
	"""
	Read/Write
	"""
	Level: str
	"""
	Read/Write
	"""
	Color: _FltPixel
	"""
	Read/Write
	"""
	Opacity: float
	"""
	Read/Write
	"""
	BgColor: _FltPixel
	"""
	Read/Write
	"""
	BevelType: str
	"""
	Read/Write
	"""
	Type: str
	"""
	Read/Write
	"""
	SoftnessImage: bool
	"""
	Read/Write
	"""
	SoftnessBlend: float
	"""
	Read/Write
	"""
	SoftnessX: float
	"""
	Read/Write
	"""
	ColorGradient: _Gradient
	"""
	Read/Write
	"""
	SoftnessY: float
	"""
	Read/Write
	"""

	#---Methods---#
	def info_text(self):
		...
	def GetImageTransformInverse(self) -> _Matrix4:
		...
	def RequiresNewImage(self, line: int, tab: int, word: int, ch: int) -> bool:
		...
	def ChannelStyle(self) -> _ChannelStyle ChannelStyle:
		"""
		ChannelStyle constructor
		"""
		...
	def IsRenderCompatibleWith(self, cs: _ChannelStyle) -> bool:
		...
	def header_text(self):
		...

ChannelStyle = _ChannelStyle