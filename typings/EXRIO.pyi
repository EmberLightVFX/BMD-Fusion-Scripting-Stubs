from Image import _Image
from ImgRectI import _ImgRectI
from EXRIO EXRIO import _EXRIO EXRIO


class _EXRIO:

	#---Properties---#
	IsWriting: bool
	"""
	Read Only
	"""
	NumParts: int
	"""
	Read Only
	"""
	IsOpen: bool
	"""
	Read Only
	"""

	#---Methods---#
	def _ReadPart(self, partnum: int, imgs: _Image) -> bool:
		...
	def ChannelImage(self, name: str, type: int, img: _Image, ichan: int, def: float, cv: float) -> None:
		...
	def _WritePart(self, partnum: int, imgs: _Image) -> bool:
		...
	def ChannelIndex(self, name: str, type: int, index: int, ichan: int, def: float, cv: float) -> None:
		...
	def ClearLastError(self) -> None:
		...
	def header_text(self):
		...
	def DataWindow(self, partnum: int) -> _ImgRectI:
		...
	def GetLastError(self) -> str:
		...
	def ReadHeader(self) -> bool:
		...
	def EXRIO(self) -> _EXRIO EXRIO:
		"""
		EXRIO constructor
		"""
		...
	def ReadOpen(self, filename: str, frame: int) -> None:
		...
	def info_text(self):
		...
	def WriteHeader(self) -> bool:
		...
	def DisplayWindow(self, partnum: int) -> _ImgRectI:
		...
	def WriteOpen(self, filename: str, frame: int) -> None:
		...
	def Close(self) -> bool:
		...
	def _PartR(self, partnum: int) -> int:
		...
	def FindPart(self, name: str) -> int:
		...
	def _PartW(self, name: str, dispw: _ImgRectI, dataw: _ImgRectI, aspect: float) -> int:
		...

EXRIO = _EXRIO