from typing import Any, Literal

class _UITree:

	#---Properties---#
	Indentation: Any
	"""
	Read/Write
	"""
	AutoExpandDelay: Any
	"""
	Read/Write
	"""
	SortingEnabled: Any
	"""
	Read/Write
	"""
	VerticalScrollMode: Any
	"""
	Read/Write
	"""
	AutoScroll: Any
	"""
	Read/Write
	"""
	UniformRowHeights: Any
	"""
	Read/Write
	"""
	HeaderHidden: Any
	"""
	Read/Write
	"""
	HorizontalScrollMode: Any
	"""
	Read/Write
	"""
	ColumnCount: Any
	"""
	Read/Write
	"""
	TabKeyNavigation: Any
	"""
	Read/Write
	"""
	WordWrap: Any
	"""
	Read/Write
	"""
	LineWidth: Any
	"""
	Read/Write
	"""
	SelectionMode: Any
	"""
	Read/Write
	"""
	RootIsDecorated: Any
	"""
	Read/Write
	"""
	MidLineWidth: Any
	"""
	Read/Write
	"""
	SelectionBehavior: Any
	"""
	Read/Write
	"""
	ItemsExpandable: Any
	"""
	Read/Write
	"""
	FrameShadow: Any
	"""
	Read/Write
	"""
	ColumnWidth: Any
	"""
	Read Only
	"""
	IconSize: Any
	"""
	Read/Write
	"""
	FrameShape: Any
	"""
	Read/Write
	"""
	FrameStyle: Any
	"""
	Read/Write
	"""
	TreePosition: Any
	"""
	Read/Write
	"""
	FrameRect: Any
	"""
	Read/Write
	"""
	ExpandsOnDoubleClick: Any
	"""
	Read/Write
	"""
	AllColumnsShowFocus: Any
	"""
	Read/Write
	"""
	AlternatingRowColors: Any
	"""
	Read/Write
	"""
	AutoScrollMargin: Any
	"""
	Read/Write
	"""
	Animated: Any
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
	def SetAutoScrollMargin(self) -> None:
		...
	def GetAutoScrollMargin(self) -> None:
		...
	def SetAutoScroll(self) -> None:
		...
	def GetAutoScroll(self) -> None:
		...
	def SetHorizontalScrollMode(self) -> None:
		...
	def GetHorizontalScrollMode(self) -> None:
		...
	def SetVerticalScrollMode(self) -> None:
		...
	def GetVerticalScrollMode(self) -> None:
		...
	def SetSelectionMode(self) -> None:
		...
	def GetSelectionMode(self) -> None:
		...
	def SetSelectionBehavior(self) -> None:
		...
	def GetSelectionBehavior(self) -> None:
		...
	def SetColumnWidth(self) -> None:
		...
	def GetColumnWidth(self) -> None:
		...
	def ResetIndentation(self) -> None:
		...
	def SetTreePosition(self) -> None:
		...
	def GetTreePosition(self) -> None:
		...
	def SetAllColumnsShowFocus(self) -> None:
		...
	def GetAllColumnsShowFocus(self) -> None:
		...
	def Clear(self) -> None:
		...
	def SetAnimated(self) -> None:
		...
	def GetAnimated(self) -> None:
		...
	def NewItem(self) -> None:
		...
	def AddTopLevelItems(self) -> None:
		...
	def SortByColumn(self) -> None:
		...
	def SetWordWrap(self) -> None:
		...
	def FindItems(self) -> None:
		...
	def SetSortingEnabled(self) -> None:
		...
	def FrameWidth(self) -> None:
		...
	def SetHeaderHidden(self) -> None:
		...
	def GetHeaderHidden(self) -> None:
		...
	def SetFrameShadow(self) -> None:
		...
	def GetExpandsOnDoubleClick(self) -> None:
		...
	def SetFrameShape(self) -> None:
		...
	def GetFrameShape(self) -> None:
		...
	def SetFrameRect(self) -> None:
		...
	def GetFrameRect(self) -> None:
		...
	def SetMidLineWidth(self) -> None:
		...
	def GetRootIsDecorated(self) -> None:
		...
	def SetIndentation(self) -> None:
		...
	def GetIndentation(self) -> None:
		...
	def SetFrameStyle(self) -> None:
		...
	def GetFrameStyle(self) -> None:
		...
	def SortItems(self) -> None:
		...
	def InsertTopLevelItems(self) -> None:
		...
	def SetHeaderItem(self) -> None:
		...
	def SetHeaderLabels(self) -> None:
		...
	def VisualItemRect(self) -> None:
		...
	def ItemAt(self) -> None:
		...
	def ItemBelow(self) -> None:
		...
	def ItemAbove(self) -> None:
		...
	def header_text(self):
		...
	def HeaderItem(self) -> None:
		...
	def InvisibleRootItem(self) -> None:
		...
	def TakeTopLevelItem(self) -> None:
		...
	def CurrentItem(self) -> None:
		...
	def SortColumn(self) -> None:
		...
	def CurrentColumn(self) -> None:
		...
	def SetHeaderLabel(self) -> None:
		...
	def InsertTopLevelItem(self) -> None:
		...
	def AddTopLevelItem(self) -> None:
		...
	def SetColumnCount(self) -> None:
		...
	def GetColumnCount(self) -> None:
		...
	def GetAutoExpandDelay(self) -> None:
		...
	def GetWordWrap(self) -> None:
		...
	def SetUniformRowHeights(self) -> None:
		...
	def ScrollToItem(self) -> None:
		...
	def SetAutoExpandDelay(self) -> None:
		...
	def SetRootIsDecorated(self) -> None:
		...
	def SetLineWidth(self) -> None:
		...
	def SetItemsExpandable(self) -> None:
		...
	def SelectedItems(self) -> None:
		...
	def IndexOfTopLevelItem(self) -> None:
		...
	def GetLineWidth(self) -> None:
		...
	def GetMidLineWidth(self) -> None:
		...
	def TopLevelItemCount(self) -> None:
		...
	def TopLevelItem(self) -> None:
		...
	def SetExpandsOnDoubleClick(self) -> None:
		...
	def GetFrameShadow(self) -> None:
		...
	def GetItemsExpandable(self) -> None:
		...
	def SetIconSize(self) -> None:
		...
	def GetIconSize(self) -> None:
		...
	def GetSortingEnabled(self) -> None:
		...
	def SetAlternatingRowColors(self) -> None:
		...
	def GetAlternatingRowColors(self) -> None:
		...
	def GetUniformRowHeights(self) -> None:
		...
	def SetTabKeyNavigation(self) -> None:
		...
	def GetTabKeyNavigation(self) -> None:
		...

UITree = _UITree