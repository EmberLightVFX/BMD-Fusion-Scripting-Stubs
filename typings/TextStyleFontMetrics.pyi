from char32_t import _char32_t
from TextStyleFontMetrics TextStyleFontMetricsTextStyleFont font import _TextStyleFontMetrics TextStyleFontMetricsTextStyleFont font
from int direction import _int direction


class _TextStyleFontMetrics:

	#---Properties---#
	UnderlineThickness: float
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
	DoStrikeout: bool
	"""
	Read/Write
	"""
	DoUnderline: bool
	"""
	Read/Write
	"""
	TypeName: str
	"""
	Read Only
	"""
	FontSize: float
	"""
	Read/Write
	"""
	TypeNamePtr: str
	"""
	Read Only
	"""
	StrikeoutThickness: float
	"""
	Read/Write
	"""
	TextAscent: float
	"""
	Read/Write
	"""
	Scale: float
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
	StrikeoutOffset: float
	"""
	Read/Write
	"""
	UnderlineOffsetH: float
	"""
	Read/Write
	"""

	#---Methods---#
	def WordWidth(self, str: str, direction: int) -> float:
		...
	def info_text(self):
		...
	def CharacterKerning(self, first: _char32_t, second: _char32_t) -> float:
		...
	def GetError(self) -> int:
		...
	def TextStyleFontMetrics(self) -> tuple[_TextStyleFontMetrics TextStyleFontMetricsTextStyleFont font, _int direction]:
		"""
		TextStyleFontMetrics constructor
		"""
		...
	def CharacterWidth(self, ch: _char32_t) -> float:
		...
	def header_text(self):
		...
	def CalcCharacterWidth(self, ch: int) -> float:
		...

TextStyleFontMetrics = _TextStyleFontMetrics