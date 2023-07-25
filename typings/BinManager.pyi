from typing import Any

class _BinManager:

	#---Properties---#
	ShowChecker: Any
	IconSize: Any
	ViewMode: Any

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_VersionString: str

	REGS_ID: str

	REGB_ControlView: bool

	REGI_Priority: int


	#---Methods---#
	def Refresh(self):
		...
	def _Library_Notify(self):
		...
	def _Library_UpdateItem(self):
		...
	def Open(self):
		...
	def Close(self):
		...
	def IsOpen(self):
		...
	def GetRootLibraryInfo(self):
		...
	def GetRootID(self):
		...
	def StopPlayback(self):
		...
	def GetSelectedIDs(self):
		...
	def CanPlaySelected(self):
		...
	def PlaySelected(self):
		...
	def RenameSelected(self):
		...
	def DeleteSelected(self):
		...
	def NewItem(self):
		...
	def header_text(self):
		...
	def NewReel(self):
		...
	def NewFolder(self):
		...
	def _Library_Reload(self):
		...
	def _Library_DeleteItem(self):
		...
	def _Library_AddItem(self):
		...
	def ShowFolder(self):
		...
	def SetLibraryRoot(self):
		...
	def ClearSelection(self):
		...
	def SelectAll(self):
		...

BinManager = _BinManager