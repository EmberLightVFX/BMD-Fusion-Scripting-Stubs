from typing import Any

class UITabBar:

	#---Properties---#
	AutoHide: Any

	ChangeCurrentOnDrag: Any

	CurrentIndex: Any

	DocumentMode: Any

	DrawBase: Any

	Expanding: Any

	Movable: Any

	TabText: Any
	"""
	Read Only
	"""

	TabTextColor: Any
	"""
	Read Only
	"""

	TabToolTip: Any
	"""
	Read Only
	"""

	TabWhatsThis: Any
	"""
	Read Only
	"""

	TabsClosable: Any

	UsesScrollButtons: Any


	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGB_Utility_Toggle: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def AddTab(self) -> None:
		...

	def Count(self) -> None:
		...

	def GetAutoHide(self) -> None:
		...

	def GetChangeCurrentOnDrag(self) -> None:
		...

	def GetCurrentIndex(self) -> None:
		...

	def GetDocumentMode(self) -> None:
		...

	def GetDrawBase(self) -> None:
		...

	def GetExpanding(self) -> None:
		...

	def GetMovable(self) -> None:
		...

	def GetTabText(self) -> None:
		...

	def GetTabTextColor(self) -> None:
		...

	def GetTabToolTip(self) -> None:
		...

	def GetTabWhatsThis(self) -> None:
		...

	def GetTabsClosable(self) -> None:
		...

	def GetUsesScrollButtons(self) -> None:
		...

	def InsertTab(self) -> None:
		...

	def MoveTab(self) -> None:
		...

	def RemoveTab(self) -> None:
		...

	def SetAutoHide(self) -> None:
		...

	def SetChangeCurrentOnDrag(self) -> None:
		...

	def SetCurrentIndex(self) -> None:
		...

	def SetDocumentMode(self) -> None:
		...

	def SetDrawBase(self) -> None:
		...

	def SetExpanding(self) -> None:
		...

	def SetMovable(self) -> None:
		...

	def SetTabText(self) -> None:
		...

	def SetTabTextColor(self) -> None:
		...

	def SetTabToolTip(self) -> None:
		...

	def SetTabWhatsThis(self) -> None:
		...

	def SetTabsClosable(self) -> None:
		...

	def SetUsesScrollButtons(self) -> None:
		...

