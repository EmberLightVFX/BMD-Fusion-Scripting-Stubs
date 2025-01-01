from ImgRectI import ImgRectI


class ImageDomain:

	#---Properties---#
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

	ImageWindow: ImgRectI
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

	ProxyScale: int
	"""
	Read Only
	"""

	ValidWindow: ImgRectI
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

	bottom: int
	"""
	Read Only
	"""

	left: int
	"""
	Read Only
	"""

	right: int
	"""
	Read Only
	"""

	top: int
	"""
	Read Only
	"""


	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def FlipX(self) -> None:
		...

	def FlipY(self) -> None:
		...

	def ImageHeight(self) -> int:
		...

	def ImageWidth(self) -> int:
		...

	def Inflate(self, x: float, y: float) -> None:
		...

	def IsEmpty(self) -> bool:
		...

	def IsNull(self) -> bool:
		...

	def IsWithin(self, dom: ImageDomain) -> bool:
		...

	def Normalise(self) -> None:
		...

	def Offset(self, x: float, y: float) -> None:
		...

	def ValidHeight(self) -> int:
		...

	def ValidWidth(self) -> int:
		...

	def _Intersect_FuRectInt(self, rect: ImgRectI) -> ImgRectI:
		...

	def _Intersect_ImageDomain(self, dom: ImageDomain) -> ImgRectI:
		...

	def _Intersect_Ints(self, l: int, b: int, r: int, t: int) -> ImgRectI:
		...

	def _Set_FuRectInt(self, rect: ImgRectI) -> None:
		...

	def _Set_Ints(self, l: int, b: int, r: int, t: int) -> None:
		...

	def _Union_FuRectInt(self, rect: ImgRectI) -> ImgRectI:
		...

	def _Union_ImageDomain(self, dom: ImageDomain) -> ImgRectI:
		...

	def _Union_Ints(self, l: int, b: int, r: int, t: int) -> ImgRectI:
		...

	def __tostring(self) -> str:
		...

	def _newDom(self, dom: ImageDomain) -> ImageDomain:
		...

	def _new_FuRectInt(self, dom: ImageDomain, rect: ImgRectI) -> ImageDomain:
		...

	def _new_Ints(self, dom: ImageDomain, l: int, b: int, r: int, t: int) -> ImageDomain:
		...

