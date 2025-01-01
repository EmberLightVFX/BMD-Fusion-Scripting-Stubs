from _non_existing import void


class ZipFile:

	#---Methods---#
	def Close(self) -> bool:
		...

	def CloseFile(self) -> bool:
		...

	def CreateFile(self, name: str, t: int, compress: bool) -> bool:
		...

	def GetError(self) -> int:
		...

	def GetFileExternalAttrs(self) -> int:
		...

	def GetFileInternalAttrs(self) -> int:
		...

	def GetFileName(self) -> str:
		...

	def GetFileSize(self) -> int:
		...

	def GetFileTime(self) -> int:
		...

	def IsEOF(self) -> bool:
		...

	def IsOpen(self) -> bool:
		...

	def LocateFile(self, name: str, casesens: bool) -> bool:
		...

	def NextFile(self) -> bool:
		...

	def Open(self, name: str, write: bool) -> bool:
		...

	def OpenFile(self) -> bool:
		...

	def ReadFile(self, buf: void, len: int) -> int:
		...

	def Rewind(self) -> bool:
		...

	def WriteFile(self, buf: void, len: int) -> int:
		...

	def __new(self, name: str, write: bool) -> ZipFile:
		"""
		ZipFile constructor

		Args:
			name (str)
			write (bool)

		Returns:
			ZipFile
		"""
		...

