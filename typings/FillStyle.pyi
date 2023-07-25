from FillStyle FillStyle import _FillStyle FillStyle
from FillStyle import _FillStyle


class _FillStyle:

	#---Properties---#
	OutsideOnly: bool
	"""
	Read/Write
	"""
	TypeNamePtr: str
	"""
	Read Only
	"""
	Overlap: str
	"""
	Read/Write
	"""
	TypeName: str
	"""
	Read Only
	"""
	AdaptToPerspective: bool
	"""
	Read/Write
	"""
	RelativeThickness: float
	"""
	Read/Write
	"""
	CleanIntersections: bool
	"""
	Read/Write
	"""
	Thickness: float
	"""
	Read/Write
	"""
	Type: str
	"""
	Read/Write
	"""
	JoinType: str
	"""
	Read/Write
	"""
	LineType: str
	"""
	Read/Write
	"""
	ExpandType: str
	"""
	Read/Write
	"""
	MiterLimit: float
	"""
	Read/Write
	"""

	#---Methods---#
	def info_text(self):
		...
	def FillStyle(self) -> _FillStyle FillStyle:
		"""
		FillStyle constructor
		"""
		...
	def IsTraceCompatibleWith(self, style: _FillStyle) -> bool:
		...
	def header_text(self):
		...
	def ActualThickness(self) -> float:
		...

FillStyle = _FillStyle