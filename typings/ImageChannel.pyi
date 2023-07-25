from FillStyle import _FillStyle
from Shape import _Shape
from ImageChannel ImageChannelImage img import _ImageChannel ImageChannelImage img
from int32 super import _int32 super
from ImageRegion rgn import _ImageRegion rgn
from boolean map import _boolean map
from ChannelStyle import _ChannelStyle


class _ImageChannel:

	#---Properties---#
	TypeNamePtr: str
	"""
	Read Only
	"""
	TypeName: str
	"""
	Read Only
	"""

	#---Methods---#
	def SetStyleFill(self, style: _FillStyle) -> None:
		...
	def info_text(self):
		...
	def ShapeFill(self, shape: _Shape, str: str) -> None:
		...
	def CopyToAlpha(self) -> None:
		...
	def ImageChannel(self) -> tuple[_ImageChannel ImageChannelImage img, _int32 super, _ImageRegion rgn, _boolean map]:
		"""
		ImageChannel constructor
		"""
		...
	def PutToImage(self, str: str, cs: _ChannelStyle) -> None:
		...
	def SimpleShapeFill(self, shape: _Shape, invert: bool, str: str) -> None:
		...
	def header_text(self):
		...

ImageChannel = _ImageChannel