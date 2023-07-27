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
	def _Library_Notify(self):
		...
	def _Library_UpdateItem(self):
		...
	def _Library_DeleteItem(self):
		...
	def _Library_AddItem(self):
		...
	def _Library_Reload(self):
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
	def header_text(self):
		...
	def SetLibraryRoot(self):
		...
	def ShowFolder(self):
		...
	def NewReel(self):
		...
	def NewFolder(self):
		...
	def Open(self):
		...
	def Close(self):
		...
	def IsOpen(self):
		...
	def DeleteSelected(self):
		...
	def NewItem(self):
		...
	def ClearSelection(self):
		...
	def SelectAll(self):
		...
	def Refresh(self):
		...

BinManager = BinManager_