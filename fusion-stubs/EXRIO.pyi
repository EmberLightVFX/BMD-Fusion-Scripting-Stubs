from ImgRectI import ImgRectI
from Image import Image


class EXRIO:

	#---Properties---#
	IsOpen: bool
	"""
	Read Only
	"""

	IsWriting: bool
	"""
	Read Only
	"""

	NumParts: int
	"""
	Read Only
	"""


	#---Methods---#
	def ChannelImage(self, name: str, type: int, img: Image, ichan: int, def_: float, cv: float) -> None:
		...

	def ChannelIndex(self, name: str, type: int, index: int, ichan: int, def_: float, cv: float) -> None:
		...

	def ClearLastError(self) -> None:
		...

	def Close(self) -> bool:
		...

	def DataWindow(self, partnum: int) -> ImgRectI:
		...

	def DisplayWindow(self, partnum: int) -> ImgRectI:
		...

	def FindPart(self, name: str) -> int:
		...

	def GetLastError(self) -> str:
		...

	def ReadHeader(self) -> bool:
		...

	def ReadOpen(self, filename: str, frame: int) -> None:
		...

	def WriteHeader(self) -> bool:
		...

	def WriteOpen(self, filename: str, frame: int) -> None:
		...

	def _PartR(self, partnum: int) -> int:
		...

	def _PartW(self, name: str, dispw: ImgRectI, dataw: ImgRectI, aspect: float) -> int:
		...

	def _ReadPart(self, partnum: int, imgs: Image) -> bool:
		...

	def _WritePart(self, partnum: int, imgs: Image) -> bool:
		...

	def __new(self) -> EXRIO:
		"""
		EXRIO constructor

		Returns:
			EXRIO
		"""
		...

