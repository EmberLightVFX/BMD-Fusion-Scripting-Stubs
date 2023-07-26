from Matrix4 import _Matrix4
from FltPixel import _FltPixel
from Gradient import _Gradient
from Image import _Image


class _ChannelStyle:

	#---Properties---#
	ColorMappingAspect: float
	"""
	Read/Write
	"""
	ColorMappingSize: float
	"""
	Read/Write
	"""
	ImageTransform: _Matrix4
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
	BgColor: _FltPixel
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
	Color: _FltPixel
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
	Opacity: float
	"""
	Read/Write
	"""
	ColorImage: _Image
	"""
	Read/Write
	"""
	SoftnessX: float
	"""
	Read/Write
	"""
	ColorImageBevel: _Image
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
	def GetImageTransformInverse(self) -> _Matrix4:
		...
	def info_text(self):
		...
	def IsRenderCompatibleWith(self, cs: _ChannelStyle) -> bool:
		...
	def header_text(self):
		...
	def RequiresNewImage(self, line: int, tab: int, word: int, ch: int) -> bool:
		...
	def ChannelStyle(self) -> _ChannelStyle:
		"""
		ChannelStyle constructor
		"""
		...

ChannelStyle = _ChannelStyle