from typing import Any, Literal

class _UITabBar:

	#---Properties---#
	TabsClosable: Any
	"""
	Read/Write
	"""
	DrawBase: Any
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
	TabWhatsThis: Any
	"""
	Read Only
	"""
	UsesScrollButtons: Any
	"""
	Read/Write
	"""
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
	Expanding: Any
	"""
	Read/Write
	"""
	CurrentIndex: Any
	"""
	Read/Write
	"""
	ChangeCurrentOnDrag: Any
	"""
	Read/Write
	"""

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def AddTab(self) -> None:
		...
	def SetTabTextColor(self) -> None:
		...
	def GetTabTextColor(self) -> None:
		...
	def SetUsesScrollButtons(self) -> None:
		...
	def SetTabWhatsThis(self) -> None:
		...
	def GetTabWhatsThis(self) -> None:
		...
	def SetTabsClosable(self) -> None:
		...
	def SetTabToolTip(self) -> None:
		...
	def GetTabToolTip(self) -> None:
		...
	def GetCurrentIndex(self) -> None:
		...
	def SetTabText(self) -> None:
		...
	def GetTabText(self) -> None:
		...
	def header_text(self):
		...
	def SetChangeCurrentOnDrag(self) -> None:
		...
	def GetChangeCurrentOnDrag(self) -> None:
		...
	def InsertTab(self) -> None:
		...
	def SetDrawBase(self) -> None:
		...
	def GetDrawBase(self) -> None:
		...
	def SetCurrentIndex(self) -> None:
		...
	def SetDocumentMode(self) -> None:
		...
	def GetDocumentMode(self) -> None:
		...
	def GetUsesScrollButtons(self) -> None:
		...
	def SetMovable(self) -> None:
		...
	def GetMovable(self) -> None:
		...
	def MoveTab(self) -> None:
		...
	def SetExpanding(self) -> None:
		...
	def GetExpanding(self) -> None:
		...
	def SetAutoHide(self) -> None:
		...
	def GetAutoHide(self) -> None:
		...
	def RemoveTab(self) -> None:
		...
	def Count(self) -> None:
		...
	def GetTabsClosable(self) -> None:
		...

UITabBar = _UITabBar