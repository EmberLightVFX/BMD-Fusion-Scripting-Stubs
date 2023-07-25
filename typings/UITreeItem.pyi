from typing import Any

class _UITreeItem:

	#---Properties---#
	ToolTip: Any
	"""
	Read Only
	"""
	StatusTip: Any
	"""
	Read Only
	"""
	ChildIndicatorPolicy: Any
	"""
	Read/Write
	"""
	Text: Any
	"""
	Read Only
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
	Hidden: Any
	"""
	Read/Write
	"""
	Selected: Any
	"""
	Read/Write
	"""
	BackgroundColor: Any
	"""
	Read Only
	"""
	CheckState: Any
	"""
	Read Only
	"""
	TextAlignment: Any
	"""
	Read Only
	"""
	Expanded: Any
	"""
	Read/Write
	"""
	SizeHint: Any
	"""
	Read Only
	"""
	Font: Any
	"""
	Read Only
	"""
	WhatsThis: Any
	"""
	Read Only
	"""
	TextColor: Any
	"""
	Read Only
	"""
	Icon: Any
	"""
	Read Only
	"""

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
	def SetStatusTip(self) -> None:
		...
	def GetStatusTip(self) -> None:
		...
	def SetChildIndicatorPolicy(self) -> None:
		...
	def GetChildIndicatorPolicy(self) -> None:
		...
	def SetFlags(self) -> None:
		...
	def SetText(self) -> None:
		...
	def SetDisabled(self) -> None:
		...
	def GetDisabled(self) -> None:
		...
	def GetFlags(self) -> None:
		...
	def SetFirstColumnSpanned(self) -> None:
		...
	def GetFirstColumnSpanned(self) -> None:
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
	def Clone(self) -> None:
		...
	def SetIcon(self) -> None:
		...
	def GetIcon(self) -> None:
		...
	def GetText(self) -> None:
		...
	def SetData(self) -> None:
		...
	def GetData(self) -> None:
		...
	def AddChildren(self) -> None:
		...
	def InsertChildren(self) -> None:
		...
	def SortChildren(self) -> None:
		...
	def RemoveChild(self) -> None:
		...
	def InsertChild(self) -> None:
		...
	def IndexOfChild(self) -> None:
		...
	def GetFont(self) -> None:
		...
	def TakeChild(self) -> None:
		...
	def Child(self) -> None:
		...
	def TreeWidget(self) -> None:
		...
	def ColumnCount(self) -> None:
		...
	def GetTextColor(self) -> None:
		...
	def header_text(self):
		...
	def SetBackgroundColor(self) -> None:
		...
	def GetBackgroundColor(self) -> None:
		...
	def Parent(self) -> None:
		...
	def SetCheckState(self) -> None:
		...
	def GetCheckState(self) -> None:
		...
	def SetTextColor(self) -> None:
		...
	def SetTextAlignment(self) -> None:
		...
	def GetTextAlignment(self) -> None:
		...
	def AddChild(self) -> None:
		...
	def SetSizeHint(self) -> None:
		...
	def GetSizeHint(self) -> None:
		...
	def SetFont(self) -> None:
		...
	def SetWhatsThis(self) -> None:
		...
	def GetWhatsThis(self) -> None:
		...
	def ChildCount(self) -> None:
		...
	def SetToolTip(self) -> None:
		...
	def GetToolTip(self) -> None:
		...

UITreeItem = _UITreeItem