from typing import Any

class _UITabBar:

	#---Properties---#
	Movable: Any
	"""
	Read/Write
	"""
	TabToolTip: Any
	"""
	Read Only
	"""
	TabText: Any
	"""
	Read Only
	"""
	AutoHide: Any
	"""
	Read/Write
	"""
	UsesScrollButtons: Any
	"""
	Read/Write
	"""
	ChangeCurrentOnDrag: Any
	"""
	Read/Write
	"""
	TabsClosable: Any
	"""
	Read/Write
	"""
	TabWhatsThis: Any
	"""
	Read Only
	"""
	DrawBase: Any
	"""
	Read/Write
	"""
	CurrentIndex: Any
	"""
	Read/Write
	"""
	TabTextColor: Any
	"""
	Read Only
	"""
	DocumentMode: Any
	"""
	Read/Write
	"""
	Expanding: Any
	"""
	Read/Write
	"""

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGS_VersionString: str

	REGI_ClassType: int

	REGI_Priority: int

	REGB_ControlView: bool

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGB_Unpredictable: bool


	#---Methods---#
	def GetTabToolTip(self) -> None:
		...
	def SetUsesScrollButtons(self) -> None:
		...
	def SetTabText(self) -> None:
		...
	def GetTabText(self) -> None:
		...
	def SetTabsClosable(self) -> None:
		...
	def SetChangeCurrentOnDrag(self) -> None:
		...
	def GetChangeCurrentOnDrag(self) -> None:
		...
	def Count(self) -> None:
		...
	def SetDrawBase(self) -> None:
		...
	def GetDrawBase(self) -> None:
		...
	def GetCurrentIndex(self) -> None:
		...
	def SetDocumentMode(self) -> None:
		...
	def GetDocumentMode(self) -> None:
		...
	def SetTabTextColor(self) -> None:
		...
	def SetMovable(self) -> None:
		...
	def GetMovable(self) -> None:
		...
	def InsertTab(self) -> None:
		...
	def SetExpanding(self) -> None:
		...
	def GetExpanding(self) -> None:
		...
	def SetAutoHide(self) -> None:
		...
	def GetAutoHide(self) -> None:
		...
	def MoveTab(self) -> None:
		...
	def RemoveTab(self) -> None:
		...
	def GetTabsClosable(self) -> None:
		...
	def AddTab(self) -> None:
		...
	def SetCurrentIndex(self) -> None:
		...
	def GetUsesScrollButtons(self) -> None:
		...
	def header_text(self):
		...
	def SetTabWhatsThis(self) -> None:
		...
	def GetTabWhatsThis(self) -> None:
		...
	def GetTabTextColor(self) -> None:
		...
	def SetTabToolTip(self) -> None:
		...

UITabBar = _UITabBar