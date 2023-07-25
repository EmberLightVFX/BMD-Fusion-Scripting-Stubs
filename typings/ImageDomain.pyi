from ImgRectI import _ImgRectI
from ImageDomain import _ImageDomain


class _ImageDomain:

	#---Properties---#
	OriginalXScale: float
	"""
	Read Only
	"""
	OriginalYScale: float
	"""
	Read Only
	"""
	bottom: int
	"""
	Read Only
	"""
	left: int
	"""
	Read Only
	"""
	ProxyScale: int
	"""
	Read Only
	"""
	right: int
	"""
	Read Only
	"""
	ValidWindow: _ImgRectI
	"""
	Read Only
	"""
	top: int
	"""
	Read Only
	"""
	Width: int
	"""
	Read Only
	"""
	XOffset: float
	"""
	Read Only
	"""
	XScale: float
	"""
	Read Only
	"""
	YOffset: float
	"""
	Read Only
	"""
	YScale: float
	"""
	Read Only
	"""
	Depth: int
	"""
	Read Only
	"""
	Field: int
	"""
	Read Only
	"""
	Height: int
	"""
	Read Only
	"""
	ImageWindow: _ImgRectI
	"""
	Read Only
	"""
	OriginalHeight: int
	"""
	Read Only
	"""
	OriginalWidth: int
	"""
	Read Only
	"""

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_VersionString: str

	REGS_ID: str

	REGB_ControlView: bool

	REGI_Priority: int


	#---Methods---#
	def FlipY(self) -> None:
		...
	def _Union_Ints(self, l: int, b: int, r: int, t: int) -> _ImgRectI:
		...
	def Inflate(self, x: float, y: float) -> None:
		...
	def ImageHeight(self) -> int:
		...
	def IsEmpty(self) -> bool:
		...
	def ImageWidth(self) -> int:
		...
	def _new_Ints(self, dom: _ImageDomain, l: int, b: int, r: int, t: int) -> _ImageDomain:
		...
	def Normalise(self) -> None:
		...
	def _new_FuRectInt(self, dom: _ImageDomain, rect: _ImgRectI) -> _ImageDomain:
		...
	def ValidHeight(self) -> int:
		...
	def _newDom(self, dom: _ImageDomain) -> _ImageDomain:
		...
	def ValidWidth(self) -> int:
		...
	def Offset(self, x: float, y: float) -> None:
		...
	def _Intersect_FuRectInt(self, rect: _ImgRectI) -> _ImgRectI:
		...
	def __tostring(self) -> str:
		...
	def _Intersect_ImageDomain(self, dom: _ImageDomain) -> _ImgRectI:
		...
	def IsWithin(self, dom: _ImageDomain) -> bool:
		...
	def _Intersect_Ints(self, l: int, b: int, r: int, t: int) -> _ImgRectI:
		...
	def _Set_FuRectInt(self, rect: _ImgRectI) -> None:
		...
	def info_text(self):
		...
	def IsNull(self) -> bool:
		...
	def _Set_Ints(self, l: int, b: int, r: int, t: int) -> None:
		...
	def header_text(self):
		...
	def _Union_FuRectInt(self, rect: _ImgRectI) -> _ImgRectI:
		...
	def FlipX(self) -> None:
		...
	def _Union_ImageDomain(self, dom: _ImageDomain) -> _ImgRectI:
		...

ImageDomain = _ImageDomain