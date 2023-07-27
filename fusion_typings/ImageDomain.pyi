from ImgRectI import ImgRectI_


class ImageDomain_:

	#---Properties---#
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
	ImageWindow: ImgRectI_
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
	OriginalXScale: float
	"""
	Read Only
	"""
	OriginalYScale: float
	"""
	Read Only
	"""
	top: int
	"""
	Read Only
	"""
	right: int
	"""
	Read Only
	"""
	left: int
	"""
	Read Only
	"""
	ValidWindow: ImgRectI_
	"""
	Read Only
	"""
	bottom: int
	"""
	Read Only
	"""
	Width: int
	"""
	Read Only
	"""
	ProxyScale: int
	"""
	Read Only
	"""
	XOffset: float
	"""
	Read Only
	"""

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def FlipX(self) -> None:
		...
	def FlipY(self) -> None:
		...
	def Inflate(self, x: float, y: float) -> None:
		...
	def ValidHeight(self) -> int:
		...
	def ValidWidth(self) -> int:
		...
	def _new_Ints(self, dom: ImageDomain_, l: int, b: int, r: int, t: int) -> ImageDomain_:
		...
	def _Intersect_FuRectInt(self, rect: ImgRectI_) -> ImgRectI_:
		...
	def _new_FuRectInt(self, dom: ImageDomain_, rect: ImgRectI_) -> ImageDomain_:
		...
	def _Intersect_ImageDomain(self, dom: ImageDomain_) -> ImgRectI_:
		...
	def _newDom(self, dom: ImageDomain_) -> ImageDomain_:
		...
	def _Intersect_Ints(self, l: int, b: int, r: int, t: int) -> ImgRectI_:
		...
	def info_text(self):
		...
	def _Set_FuRectInt(self, rect: ImgRectI_) -> None:
		...
	def __tostring(self) -> str:
		...
	def _Set_Ints(self, l: int, b: int, r: int, t: int) -> None:
		...
	def Normalise(self) -> None:
		...
	def _Union_FuRectInt(self, rect: ImgRectI_) -> ImgRectI_:
		...
	def IsWithin(self, dom: ImageDomain_) -> bool:
		...
	def IsNull(self) -> bool:
		...
	def _Union_ImageDomain(self, dom: ImageDomain_) -> ImgRectI_:
		...
	def _Union_Ints(self, l: int, b: int, r: int, t: int) -> ImgRectI_:
		...
	def Offset(self, x: float, y: float) -> None:
		...
	def header_text(self):
		...
	def ImageHeight(self) -> int:
		...
	def IsEmpty(self) -> bool:
		...
	def ImageWidth(self) -> int:
		...

ImageDomain = ImageDomain_