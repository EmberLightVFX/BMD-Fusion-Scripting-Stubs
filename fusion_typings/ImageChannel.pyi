from FillStyle import FillStyle_
from Image import Image_
from ImageRegion import ImageRegion_
from ChannelStyle import ChannelStyle_
from Shape import Shape_


class ImageChannel_:

	#---Properties---#
	TypeName: str
	"""
	Read Only
	"""
	TypeNamePtr: str
	"""
	Read Only
	"""

	#---Methods---#
	def SetStyleFill(self, style: FillStyle_) -> None:
		...
	def info_text(self):
		...
	def ImageChannel(self, img: Image_, super: int, rgn: ImageRegion_, map: bool) -> ImageChannel_:
		"""
		ImageChannel constructor
		"""
		...
	def CopyToAlpha(self) -> None:
		...
	def header_text(self):
		...
	def PutToImage(self, str: str, cs: ChannelStyle_) -> None:
		...
	def ShapeFill(self, shape: Shape_, str: str) -> None:
		...
	def SimpleShapeFill(self, shape: Shape_, invert: bool, str: str) -> None:
		...

ImageChannel = ImageChannel_