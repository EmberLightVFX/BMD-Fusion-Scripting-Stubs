class BinManager:

	#---Properties---#

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
	def CanPlaySelected(self) -> None:
		...

	def ClearSelection(self) -> None:
		...

	def Close(self) -> None:
		...

	def DeleteSelected(self) -> None:
		...

	def GetRootID(self) -> None:
		...

	def GetRootLibraryInfo(self) -> None:
		...

	def GetSelectedIDs(self) -> None:
		...

	def IsOpen(self) -> None:
		...

	def NewFolder(self) -> None:
		...

	def NewItem(self) -> None:
		...

	def NewReel(self) -> None:
		...

	def Open(self) -> None:
		...

	def PlaySelected(self) -> None:
		...

	def Refresh(self) -> None:
		...

	def RenameSelected(self) -> None:
		...

	def SelectAll(self) -> None:
		...

	def SetLibraryRoot(self) -> None:
		...

	def ShowFolder(self) -> None:
		...

	def StopPlayback(self) -> None:
		...

	def _Library_AddItem(self) -> None:
		...

	def _Library_DeleteItem(self) -> None:
		...

	def _Library_Notify(self) -> None:
		...

	def _Library_Reload(self) -> None:
		...

	def _Library_UpdateItem(self) -> None:
		...

