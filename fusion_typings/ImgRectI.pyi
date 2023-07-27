class ImgRectI_:

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
	def FlipX(self) -> ImgRectI_:
		...
	def _newCopy(self, x: ImgRectI_) -> ImgRectI_:
		...
	def FlipY(self) -> ImgRectI_:
		...
	def Inflate(self, x: float, y: float) -> ImgRectI_:
		...
	def IsEmpty(self) -> bool:
		...
	def Height(self) -> int:
		...
	def header_text(self) -> None:
		...
	def _newDef(self) -> ImgRectI_:
		...
	def info_text(self) -> None:
		...
	def __tostring(self) -> str:
		...
	def _newNums(self, l: int, b: int, r: int, t: int) -> ImgRectI_:
		...
	def Scale(self, x: float, y: float) -> ImgRectI_:
		...
	def _IntersectNums(self, l: int, b: int, r: int, t: int) -> ImgRectI_:
		...
	def Offset(self, x: float, y: float) -> ImgRectI_:
		...
	def _IsWithinNums(self, x: int, y: int) -> bool:
		...
	def IsNull(self) -> bool:
		...
	def _IsWithinRect(self, rect: ImgRectI_) -> bool:
		...
	def Normalise(self) -> ImgRectI_:
		...
	def _SetNums(self, l: int, b: int, r: int, t: int) -> None:
		...
	def Width(self) -> int:
		...
	def _UnionNums(self, l: int, b: int, r: int, t: int) -> ImgRectI_:
		...
	def _IntersectRect(self, rect: ImgRectI_) -> ImgRectI_:
		...
	def _UnionRect(self, rect: ImgRectI_) -> ImgRectI_:
		...

ImgRectI = ImgRectI_