from typing import Literal

from FillStyle import _FillStyle
from Image import _Image
from ImageRegion import _ImageRegion
from ChannelStyle import _ChannelStyle
from Shape import _Shape


class _ImageChannel:

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
	def SetStyleFill(self, style: _FillStyle) -> None:
		...
	def info_text(self):
		...
	def ImageChannel(self, img: _Image, super: int, rgn: _ImageRegion, map: bool) -> _ImageChannel:
		"""
		ImageChannel constructor
		"""
		...
	def CopyToAlpha(self) -> None:
		...
	def header_text(self):
		...
	def PutToImage(self, str: str, cs: _ChannelStyle) -> None:
		...
	def ShapeFill(self, shape: _Shape, str: str) -> None:
		...
	def SimpleShapeFill(self, shape: _Shape, invert: bool, str: str) -> None:
		...

ImageChannel = _ImageChannel