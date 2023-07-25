from typing import Any

class _UITree:

	#---Properties---#
	TreePosition: Any
	"""
	Read/Write
	"""
	WordWrap: Any
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
	RootIsDecorated: Any
	"""
	Read/Write
	"""
	Animated: Any
	"""
	Read/Write
	"""
	TabKeyNavigation: Any
	"""
	Read/Write
	"""
	HeaderHidden: Any
	"""
	Read/Write
	"""
	SortingEnabled: Any
	"""
	Read/Write
	"""
	AutoScrollMargin: Any
	"""
	Read/Write
	"""
	FrameShape: Any
	"""
	Read/Write
	"""
	UniformRowHeights: Any
	"""
	Read/Write
	"""
	AutoScroll: Any
	"""
	Read/Write
	"""
	FrameRect: Any
	"""
	Read/Write
	"""
	FrameShadow: Any
	"""
	Read/Write
	"""
	HorizontalScrollMode: Any
	"""
	Read/Write
	"""
	ItemsExpandable: Any
	"""
	Read/Write
	"""
	VerticalScrollMode: Any
	"""
	Read/Write
	"""
	LineWidth: Any
	"""
	Read/Write
	"""
	MidLineWidth: Any
	"""
	Read/Write
	"""
	SelectionMode: Any
	"""
	Read/Write
	"""
	FrameStyle: Any
	"""
	Read/Write
	"""
	IconSize: Any
	"""
	Read/Write
	"""
	SelectionBehavior: Any
	"""
	Read/Write
	"""
	Indentation: Any
	"""
	Read/Write
	"""
	ColumnCount: Any
	"""
	Read/Write
	"""
	ColumnWidth: Any
	"""
	Read Only
	"""
	AutoExpandDelay: Any
	"""
	Read/Write
	"""
	ExpandsOnDoubleClick: Any
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
	def GetTreePosition(self) -> None:
		...
	def SetAllColumnsShowFocus(self) -> None:
		...
	def GetAllColumnsShowFocus(self) -> None:
		...
	def SetAnimated(self) -> None:
		...
	def GetAnimated(self) -> None:
		...
	def SetSortingEnabled(self) -> None:
		...
	def GetSortingEnabled(self) -> None:
		...
	def SetHeaderHidden(self) -> None:
		...
	def GetHeaderHidden(self) -> None:
		...
	def SetExpandsOnDoubleClick(self) -> None:
		...
	def GetExpandsOnDoubleClick(self) -> None:
		...
	def SetItemsExpandable(self) -> None:
		...
	def GetItemsExpandable(self) -> None:
		...
	def SetUniformRowHeights(self) -> None:
		...
	def GetUniformRowHeights(self) -> None:
		...
	def SelectedItems(self) -> None:
		...
	def GetRootIsDecorated(self) -> None:
		...
	def SetIndentation(self) -> None:
		...
	def GetIndentation(self) -> None:
		...
	def TopLevelItem(self) -> None:
		...
	def SetAutoExpandDelay(self) -> None:
		...
	def GetIconSize(self) -> None:
		...
	def SortItems(self) -> None:
		...
	def SetWordWrap(self) -> None:
		...
	def GetWordWrap(self) -> None:
		...
	def FrameWidth(self) -> None:
		...
	def SetFrameShadow(self) -> None:
		...
	def GetFrameShadow(self) -> None:
		...
	def SetFrameShape(self) -> None:
		...
	def Clear(self) -> None:
		...
	def SetFrameRect(self) -> None:
		...
	def NewItem(self) -> None:
		...
	def AddTopLevelItems(self) -> None:
		...
	def SetMidLineWidth(self) -> None:
		...
	def GetMidLineWidth(self) -> None:
		...
	def SetLineWidth(self) -> None:
		...
	def InsertTopLevelItems(self) -> None:
		...
	def SetHeaderItem(self) -> None:
		...
	def SetFrameStyle(self) -> None:
		...
	def GetFrameStyle(self) -> None:
		...
	def ItemAt(self) -> None:
		...
	def ItemBelow(self) -> None:
		...
	def ItemAbove(self) -> None:
		...
	def IndexOfTopLevelItem(self) -> None:
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
	def header_text(self):
		...
	def VisualItemRect(self) -> None:
		...
	def TopLevelItemCount(self) -> None:
		...
	def SortByColumn(self) -> None:
		...
	def SetAlternatingRowColors(self) -> None:
		...
	def GetAlternatingRowColors(self) -> None:
		...
	def SetIconSize(self) -> None:
		...
	def SetTabKeyNavigation(self) -> None:
		...
	def GetTabKeyNavigation(self) -> None:
		...
	def ScrollToItem(self) -> None:
		...
	def SetAutoScrollMargin(self) -> None:
		...
	def GetAutoScrollMargin(self) -> None:
		...
	def GetAutoExpandDelay(self) -> None:
		...
	def SetAutoScroll(self) -> None:
		...
	def GetAutoScroll(self) -> None:
		...
	def FindItems(self) -> None:
		...
	def SetHorizontalScrollMode(self) -> None:
		...
	def GetHorizontalScrollMode(self) -> None:
		...
	def SetRootIsDecorated(self) -> None:
		...
	def SetVerticalScrollMode(self) -> None:
		...
	def GetVerticalScrollMode(self) -> None:
		...
	def SetHeaderLabels(self) -> None:
		...
	def SetSelectionMode(self) -> None:
		...
	def GetSelectionMode(self) -> None:
		...
	def GetFrameRect(self) -> None:
		...
	def SetSelectionBehavior(self) -> None:
		...
	def GetSelectionBehavior(self) -> None:
		...
	def GetLineWidth(self) -> None:
		...
	def SetColumnWidth(self) -> None:
		...
	def GetColumnWidth(self) -> None:
		...
	def GetFrameShape(self) -> None:
		...
	def ResetIndentation(self) -> None:
		...
	def SetTreePosition(self) -> None:
		...

UITree = _UITree