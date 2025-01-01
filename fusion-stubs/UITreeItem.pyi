from typing import Any

class UITreeItem:

	#---Properties---#
	BackgroundColor: Any
	"""
	Read Only
	"""

	CheckState: Any
	"""
	Read Only
	"""

	ChildIndicatorPolicy: Any

	Disabled: Any

	Expanded: Any

	FirstColumnSpanned: Any

	Flags: Any

	Font: Any
	"""
	Read Only
	"""

	Hidden: Any

	Icon: Any
	"""
	Read Only
	"""

	Selected: Any

	SizeHint: Any
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

	TextAlignment: Any
	"""
	Read Only
	"""

	TextColor: Any
	"""
	Read Only
	"""

	ToolTip: Any
	"""
	Read Only
	"""

	WhatsThis: Any
	"""
	Read Only
	"""


	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def AddChild(self) -> None:
		...

	def AddChildren(self) -> None:
		...

	def Child(self) -> None:
		...

	def ChildCount(self) -> None:
		...

	def Clone(self) -> None:
		...

	def ColumnCount(self) -> None:
		...

	def GetBackgroundColor(self) -> None:
		...

	def GetCheckState(self) -> None:
		...

	def GetChildIndicatorPolicy(self) -> None:
		...

	def GetData(self) -> None:
		...

	def GetDisabled(self) -> None:
		...

	def GetExpanded(self) -> None:
		...

	def GetFirstColumnSpanned(self) -> None:
		...

	def GetFlags(self) -> None:
		...

	def GetFont(self) -> None:
		...

	def GetHidden(self) -> None:
		...

	def GetIcon(self) -> None:
		...

	def GetSelected(self) -> None:
		...

	def GetSizeHint(self) -> None:
		...

	def GetStatusTip(self) -> None:
		...

	def GetText(self) -> None:
		...

	def GetTextAlignment(self) -> None:
		...

	def GetTextColor(self) -> None:
		...

	def GetToolTip(self) -> None:
		...

	def GetWhatsThis(self) -> None:
		...

	def IndexOfChild(self) -> None:
		...

	def InsertChild(self) -> None:
		...

	def InsertChildren(self) -> None:
		...

	def Parent(self) -> None:
		...

	def RemoveChild(self) -> None:
		...

	def SetBackgroundColor(self) -> None:
		...

	def SetCheckState(self) -> None:
		...

	def SetChildIndicatorPolicy(self) -> None:
		...

	def SetData(self) -> None:
		...

	def SetDisabled(self) -> None:
		...

	def SetExpanded(self) -> None:
		...

	def SetFirstColumnSpanned(self) -> None:
		...

	def SetFlags(self) -> None:
		...

	def SetFont(self) -> None:
		...

	def SetHidden(self) -> None:
		...

	def SetIcon(self) -> None:
		...

	def SetSelected(self) -> None:
		...

	def SetSizeHint(self) -> None:
		...

	def SetStatusTip(self) -> None:
		...

	def SetText(self) -> None:
		...

	def SetTextAlignment(self) -> None:
		...

	def SetTextColor(self) -> None:
		...

	def SetToolTip(self) -> None:
		...

	def SetWhatsThis(self) -> None:
		...

	def SortChildren(self) -> None:
		...

	def TakeChild(self) -> None:
		...

	def TreeWidget(self) -> None:
		...

