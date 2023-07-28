from ImgRectI import ImgRectI_
from Image import Image_


class EXRIO_:

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
	def ReadOpen(self, filename: str, frame: int) -> None:
		...
	def WriteHeader(self) -> bool:
		...
	def DataWindow(self, partnum: int) -> ImgRectI_:
		...
	def _PartR(self, partnum: int) -> int:
		...
	def EXRIO(self) -> EXRIO_:
		"""
		EXRIO constructor
		"""
		...
	def _PartW(self, name: str, dispw: ImgRectI_, dataw: ImgRectI_, aspect: float) -> int:
		...
	def header_text(self) -> None:
		...
	def ChannelImage(self, name: str, type: int, img: Image_, ichan: int, def_: float, cv: float) -> None:
		...
	def _WritePart(self, partnum: int, imgs: Image_) -> bool:
		...
	def info_text(self) -> None:
		...
	def ClearLastError(self) -> None:
		...
	def Close(self) -> bool:
		...
	def DisplayWindow(self, partnum: int) -> ImgRectI_:
		...
	def FindPart(self, name: str) -> int:
		...
	def _ReadPart(self, partnum: int, imgs: Image_) -> bool:
		...
	def GetLastError(self) -> str:
		...
	def ChannelIndex(self, name: str, type: int, index: int, ichan: int, def_: float, cv: float) -> None:
		...
	def ReadHeader(self) -> bool:
		...
	def WriteOpen(self, filename: str, frame: int) -> None:
		...

EXRIO = EXRIO_