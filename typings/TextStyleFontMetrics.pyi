from typing import Literal

from TextStyleFont import _TextStyleFont


class _TextStyleFontMetrics:

	#---Properties---#
	StrikeoutOffset: float
	"""
	Read/Write
	"""
	StrikeoutThickness: float
	"""
	Read/Write
	"""
	TextAscent: float
	"""
	Read/Write
	"""
	TextDescent: float
	"""
	Read/Write
	"""
	TextExternalLeading: float
	"""
	Read/Write
	"""
	TextInternalLeading: float
	"""
	Read/Write
	"""
	UnderlineOffsetH: float
	"""
	Read/Write
	"""
	UnderlineThickness: float
	"""
	Read/Write
	"""
	Scale: float
	"""
	Read/Write
	"""
	CharWidthAverage: float
	"""
	Read/Write
	"""
	CharWidthSpace: float
	"""
	Read/Write
	"""
	TypeName: str
	"""
	Read Only
	"""
	DoStrikeout: bool
	"""
	Read/Write
	"""
	DoUnderline: bool
	"""
	Read/Write
	"""
	TypeNamePtr: str
	"""
	Read Only
	"""
	FontSize: float
	"""
	Read/Write
	"""

	#---Methods---#
	def WordWidth(self, str: str, direction: int) -> float:
		...
	def info_text(self):
		...
	def TextStyleFontMetrics(self, font: _TextStyleFont, direction: int) -> _TextStyleFontMetrics:
		"""
		TextStyleFontMetrics constructor
		"""
		...
	def GetError(self) -> int:
		...
	def header_text(self):
		...
	def CalcCharacterWidth(self, ch: int) -> float:
		...
	def CharacterWidth(self, ch: str) -> float:
		...
	def CharacterKerning(self, first: str, second: str) -> float:
		...

TextStyleFontMetrics = _TextStyleFontMetrics