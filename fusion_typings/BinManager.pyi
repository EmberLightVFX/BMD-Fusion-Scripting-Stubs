from typing import Any

class BinManager_:

	#---Properties---#
	IconSize: Any
	ViewMode: Any
	ShowChecker: Any

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def _Library_Notify(self) -> None:
		...
	def _Library_UpdateItem(self) -> None:
		...
	def _Library_DeleteItem(self) -> None:
		...
	def _Library_AddItem(self) -> None:
		...
	def _Library_Reload(self) -> None:
		...
	def GetRootLibraryInfo(self) -> None:
		...
	def GetRootID(self) -> None:
		...
	def StopPlayback(self) -> None:
		...
	def GetSelectedIDs(self) -> None:
		...
	def CanPlaySelected(self) -> None:
		...
	def PlaySelected(self) -> None:
		...
	def RenameSelected(self) -> None:
		...
	def header_text(self) -> None:
		...
	def SetLibraryRoot(self) -> None:
		...
	def ShowFolder(self) -> None:
		...
	def NewReel(self) -> None:
		...
	def NewFolder(self) -> None:
		...
	def Open(self) -> None:
		...
	def Close(self) -> None:
		...
	def IsOpen(self) -> None:
		...
	def DeleteSelected(self) -> None:
		...
	def NewItem(self) -> None:
		...
	def ClearSelection(self) -> None:
		...
	def SelectAll(self) -> None:
		...
	def Refresh(self) -> None:
		...

BinManager = BinManager_