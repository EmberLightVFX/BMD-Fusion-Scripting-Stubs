class ImgRectI:

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
	def FlipX(self) -> ImgRectI:
		...

	def FlipY(self) -> ImgRectI:
		...

	def Height(self) -> int:
		...

	def Inflate(self, x: float, y: float) -> ImgRectI:
		...

	def IsEmpty(self) -> bool:
		...

	def IsNull(self) -> bool:
		...

	def Normalise(self) -> ImgRectI:
		...

	def Offset(self, x: float, y: float) -> ImgRectI:
		...

	def Scale(self, x: float, y: float) -> ImgRectI:
		...

	def Width(self) -> int:
		...

	def _IntersectNums(self, l: int, b: int, r: int, t: int) -> ImgRectI:
		...

	def _IntersectRect(self, rect: ImgRectI) -> ImgRectI:
		...

	def _IsWithinNums(self, x: int, y: int) -> bool:
		...

	def _IsWithinRect(self, rect: ImgRectI) -> bool:
		...

	def _SetNums(self, l: int, b: int, r: int, t: int) -> None:
		...

	def _UnionNums(self, l: int, b: int, r: int, t: int) -> ImgRectI:
		...

	def _UnionRect(self, rect: ImgRectI) -> ImgRectI:
		...

	def __tostring(self) -> str:
		...

	def _newCopy(self, x: ImgRectI) -> ImgRectI:
		...

	def _newDef(self) -> ImgRectI:
		...

	def _newNums(self, l: int, b: int, r: int, t: int) -> ImgRectI:
		...

