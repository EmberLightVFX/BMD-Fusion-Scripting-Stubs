from typing import Any

from Vector2 import _Vector2
from TextStyleFont TextStyleFontstring name import _TextStyleFont TextStyleFontstring name
from string style import _string style
from float64 size import _float64 size
from TextStyleFont import _TextStyleFont


class _TextStyleFont:

	#---Properties---#
	Size: float
	"""
	Read/Write
	"""
	SplitLigatures: bool
	"""
	Read/Write
	"""
	Strikeout: bool
	"""
	Read/Write
	"""
	StylisticSet: int
	"""
	Read/Write
	"""
	Underline: bool
	"""
	Read/Write
	"""
	TypeName: str
	"""
	Read Only
	"""
	Name: str
	"""
	Read/Write
	"""
	Valid: bool
	"""
	Read/Write
	"""
	TypeNamePtr: str
	"""
	Read Only
	"""
	DoKerning: bool
	"""
	Read/Write
	"""
	DoLigatures: int
	"""
	Read/Write
	"""
	Features: Any
	"""
	Write Only
	"""
	ManualKerning: _Vector2
	"""
	Read/Write
	"""
	ManualPositioning: _Vector2
	"""
	Read/Write
	"""
	Monospaced: float
	"""
	Read/Write
	"""
	UnderlinePosition: int
	"""
	Read/Write
	"""
	Style: str
	"""
	Read/Write
	"""
	Orientation: int
	"""
	Read/Write
	"""

	#---Methods---#
	def TextStyleFont(self) -> tuple[_TextStyleFont TextStyleFontstring name, _string style, _float64 size]:
		"""
		TextStyleFont constructor
		"""
		...
	def info_text(self):
		...
	def MetricsCompatibleWith(self, font: _TextStyleFont) -> bool:
		...
	def SetFeatures(self, features: str) -> None:
		...
	def header_text(self):
		...

TextStyleFont = _TextStyleFont