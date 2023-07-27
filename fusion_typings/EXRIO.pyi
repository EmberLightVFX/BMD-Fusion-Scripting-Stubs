from ImgRectI import _ImgRectI
from Image import _Image


class _EXRIO:

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
	def DataWindow(self, partnum: int) -> _ImgRectI:
		...
	def _PartR(self, partnum: int) -> int:
		...
	def EXRIO(self) -> _EXRIO:
		"""
		EXRIO constructor
		"""
		...
	def _PartW(self, name: str, dispw: _ImgRectI, dataw: _ImgRectI, aspect: float) -> int:
		...
	def header_text(self):
		...
	def ChannelImage(self, name: str, type: int, img: _Image, ichan: int, def_: float, cv: float) -> None:
		...
	def _WritePart(self, partnum: int, imgs: _Image) -> bool:
		...
	def info_text(self):
		...
	def ClearLastError(self) -> None:
		...
	def Close(self) -> bool:
		...
	def DisplayWindow(self, partnum: int) -> _ImgRectI:
		...
	def FindPart(self, name: str) -> int:
		...
	def _ReadPart(self, partnum: int, imgs: _Image) -> bool:
		...
	def GetLastError(self) -> str:
		...
	def ChannelIndex(self, name: str, type: int, index: int, ichan: int, def_: float, cv: float) -> None:
		...
	def ReadHeader(self) -> bool:
		...
	def WriteOpen(self, filename: str, frame: int) -> None:
		...

EXRIO = _EXRIO