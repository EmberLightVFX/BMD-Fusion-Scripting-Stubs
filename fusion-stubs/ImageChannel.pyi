from FillStyle import FillStyle
from Shape import Shape
from ChannelStyle import ChannelStyle
from Image import Image
from ImageRegion import ImageRegion


class ImageChannel:

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
	def CopyToAlpha(self) -> None:
		...

	def PutToImage(self, str: str, cs: ChannelStyle) -> None:
		...

	def SetStyleFill(self, style: FillStyle) -> None:
		...

	def ShapeFill(self, shape: Shape, str: str) -> None:
		...

	def SimpleShapeFill(self, shape: Shape, invert: bool, str: str) -> None:
		...

	def __new(self, img: Image, super: int, rgn: ImageRegion, map: bool) -> ImageChannel:
		"""
		ImageChannel constructor

		Args:
			img (Image)
			super (int)
			rgn (ImageRegion)
			map (bool)

		Returns:
			ImageChannel
		"""
		...

