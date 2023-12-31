from _non_existing import void_


class ZipFile_:

	#---Methods---#
	def WriteFile(self, buf: void_, len: int) -> int:
		...
	def ReadFile(self, buf: void_, len: int) -> int:
		...
	def GetFileTime(self) -> int:
		...
	def GetFileName(self) -> str:
		...
	def GetFileSize(self) -> int:
		...
	def GetFileInternalAttrs(self) -> int:
		...
	def GetFileExternalAttrs(self) -> int:
		...
	def ZipFile(self, name: str, write: bool) -> ZipFile_:
		"""
		ZipFile constructor
		"""
		...
	def header_text(self) -> None:
		...
	def info_text(self) -> None:
		...
	def GetError(self) -> int:
		...
	def Open(self, name: str, write: bool) -> bool:
		...
	def Close(self) -> bool:
		...
	def IsOpen(self) -> bool:
		...
	def IsEOF(self) -> bool:
		...
	def Rewind(self) -> bool:
		...
	def NextFile(self) -> bool:
		...
	def LocateFile(self, name: str, casesens: bool) -> bool:
		...
	def OpenFile(self) -> bool:
		...
	def CreateFile(self, name: str, t: int, compress: bool) -> bool:
		...
	def CloseFile(self) -> bool:
		...

ZipFile = ZipFile_