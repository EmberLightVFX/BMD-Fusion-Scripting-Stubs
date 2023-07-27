from typing import Any

class _UITreeItem:

	#---Properties---#
	ToolTip: Any
	"""
	Read Only
	"""
	TextAlignment: Any
	"""
	Read Only
	"""
	SizeHint: Any
	"""
	Read Only
	"""
	Hidden: Any
	"""
	Read/Write
	"""
	Selected: Any
	"""
	Read/Write
	"""
	Font: Any
	"""
	Read Only
	"""
	StatusTip: Any
	"""
	Read Only
	"""
	Text: Any
	"""
	Read Only
	"""
	Icon: Any
	"""
	Read Only
	"""
	ChildIndicatorPolicy: Any
	"""
	Read/Write
	"""
	Flags: Any
	"""
	Read/Write
	"""
	Disabled: Any
	"""
	Read/Write
	"""
	FirstColumnSpanned: Any
	"""
	Read/Write
	"""
	WhatsThis: Any
	"""
	Read Only
	"""
	BackgroundColor: Any
	"""
	Read Only
	"""
	TextColor: Any
	"""
	Read Only
	"""
	CheckState: Any
	"""
	Read Only
	"""
	Expanded: Any
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

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def SetText(self) -> None:
		...
	def header_text(self):
		...
	def GetText(self) -> None:
		...
	def SetFirstColumnSpanned(self) -> None:
		...
	def SortChildren(self) -> None:
		...
	def GetFirstColumnSpanned(self) -> None:
		...
	def SetToolTip(self) -> None:
		...
	def SetTextColor(self) -> None:
		...
	def SetFont(self) -> None:
		...
	def SetStatusTip(self) -> None:
		...
	def ChildCount(self) -> None:
		...
	def TakeChild(self) -> None:
		...
	def Child(self) -> None:
		...
	def TreeWidget(self) -> None:
		...
	def SetBackgroundColor(self) -> None:
		...
	def GetBackgroundColor(self) -> None:
		...
	def SetChildIndicatorPolicy(self) -> None:
		...
	def SetCheckState(self) -> None:
		...
	def GetTextColor(self) -> None:
		...
	def ColumnCount(self) -> None:
		...
	def SetTextAlignment(self) -> None:
		...
	def GetTextAlignment(self) -> None:
		...
	def SetFlags(self) -> None:
		...
	def SetSizeHint(self) -> None:
		...
	def GetSizeHint(self) -> None:
		...
	def Clone(self) -> None:
		...
	def SetWhatsThis(self) -> None:
		...
	def GetWhatsThis(self) -> None:
		...
	def SetDisabled(self) -> None:
		...
	def AddChild(self) -> None:
		...
	def GetToolTip(self) -> None:
		...
	def GetFont(self) -> None:
		...
	def GetStatusTip(self) -> None:
		...
	def SetIcon(self) -> None:
		...
	def GetIcon(self) -> None:
		...
	def GetChildIndicatorPolicy(self) -> None:
		...
	def SetData(self) -> None:
		...
	def GetData(self) -> None:
		...
	def Parent(self) -> None:
		...
	def InsertChildren(self) -> None:
		...
	def GetDisabled(self) -> None:
		...
	def RemoveChild(self) -> None:
		...
	def InsertChild(self) -> None:
		...
	def IndexOfChild(self) -> None:
		...
	def GetCheckState(self) -> None:
		...
	def SetExpanded(self) -> None:
		...
	def GetExpanded(self) -> None:
		...
	def SetHidden(self) -> None:
		...
	def GetHidden(self) -> None:
		...
	def SetSelected(self) -> None:
		...
	def GetSelected(self) -> None:
		...
	def GetFlags(self) -> None:
		...
	def AddChildren(self) -> None:
		...

UITreeItem = _UITreeItem