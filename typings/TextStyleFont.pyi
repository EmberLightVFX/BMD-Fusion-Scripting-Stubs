from typing import Any

from Vector2 import _Vector2


class _TextStyleFont:

	#---Properties---#
	Underline: bool
	"""
	Read/Write
	"""
	UnderlinePosition: int
	"""
	Read/Write
	"""
	Name: str
	"""
	Read/Write
	"""
	Valid: bool
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
	DoLigatures: int
	"""
	Read/Write
	"""
	Monospaced: float
	"""
	Read/Write
	"""
	Orientation: int
	"""
	Read/Write
	"""
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
	TypeName: str
	"""
	Read Only
	"""
	StylisticSet: int
	"""
	Read/Write
	"""
	DoKerning: bool
	"""
	Read/Write
	"""
	TypeNamePtr: str
	"""
	Read Only
	"""
	Style: str
	"""
	Read/Write
	"""

	#---Methods---#
	def info_text(self):
		...
	def TextStyleFont(self, name: str, style: str, size: float) -> _TextStyleFont:
		"""
		TextStyleFont constructor
		"""
		...
	def MetricsCompatibleWith(self, font: _TextStyleFont) -> bool:
		...
	def header_text(self):
		...
	def SetFeatures(self, features: str) -> None:
		...

TextStyleFont = _TextStyleFont