class FuPath:

	#---Methods---#
	def AddSegment(self, str: str, skipDupes: bool) -> bool:
		...

	def Exists(self, str: str) -> bool:
		...

	def GetAllSegments(self) -> str:
		...

	def GetClosestMatch(self, str: str) -> str:
		...

	def GetFirstMatch(self, str: str) -> str:
		...

	def GetNumSegments(self) -> int:
		...

	def GetSegment(self, seg: int) -> str:
		...

	def IsDir(self, str: str) -> bool:
		...

	def IsFile(self, str: str) -> bool:
		...

	def RemoveSegment(self, seg: int) -> bool:
		...

	def SetSegment(self, seg: int, str: str) -> bool:
		...

	def __new(self, str: str) -> FuPath:
		"""
		FuPath constructor

		Args:
			str (str)

		Returns:
			FuPath
		"""
		...

