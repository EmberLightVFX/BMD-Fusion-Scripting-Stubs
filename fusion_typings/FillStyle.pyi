class FillStyle_:

	#---Properties---#
	OutsideOnly: bool
	"""
	Read/Write
	"""
	Overlap: str
	"""
	Read/Write
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
	ExpandType: str
	"""
	Read/Write
	"""
	TypeNamePtr: str
	"""
	Read Only
	"""
	JoinType: str
	"""
	Read/Write
	"""
	TypeName: str
	"""
	Read Only
	"""
	Type: str
	"""
	Read/Write
	"""
	MiterLimit: float
	"""
	Read/Write
	"""
	LineType: str
	"""
	Read/Write
	"""

	#---Methods---#
	def info_text(self):
		...
	def FillStyle(self) -> FillStyle_:
		"""
		FillStyle constructor
		"""
		...
	def header_text(self):
		...
	def IsTraceCompatibleWith(self, style: FillStyle_) -> bool:
		...
	def ActualThickness(self) -> float:
		...

FillStyle = FillStyle_