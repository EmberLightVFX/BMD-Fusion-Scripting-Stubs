from typing import Any

class UIComboBox:

	#---Properties---#
	AutoCompletion: Any

	AutoCompletionCaseSensitivity: Any

	CurrentIndex: Any

	CurrentText: Any

	DuplicatesEnabled: Any

	Editable: Any

	Frame: Any

	IconSize: Any

	InsertPolicy: Any

	ItemText: Any
	"""
	Read Only
	"""

	LineEdit: Any

	MaxCount: Any

	MaxVisibleItems: Any

	MinimumContentsLength: Any

	SizeAdjustPolicy: Any


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
	def AddItem(self) -> None:
		...

	def AddItems(self) -> None:
		...

	def Clear(self) -> None:
		...

	def ClearEditText(self) -> None:
		...

	def Count(self) -> None:
		...

	def GetAutoCompletion(self) -> None:
		...

	def GetAutoCompletionCaseSensitivity(self) -> None:
		...

	def GetCurrentIndex(self) -> None:
		...

	def GetCurrentText(self) -> None:
		...

	def GetDuplicatesEnabled(self) -> None:
		...

	def GetEditable(self) -> None:
		...

	def GetFrame(self) -> None:
		...

	def GetIconSize(self) -> None:
		...

	def GetInsertPolicy(self) -> None:
		...

	def GetItemText(self) -> None:
		...

	def GetLineEdit(self) -> None:
		...

	def GetMaxCount(self) -> None:
		...

	def GetMaxVisibleItems(self) -> None:
		...

	def GetMinimumContentsLength(self) -> None:
		...

	def GetSizeAdjustPolicy(self) -> None:
		...

	def HidePopup(self) -> None:
		...

	def InsertItem(self) -> None:
		...

	def InsertItems(self) -> None:
		...

	def InsertSeparator(self) -> None:
		...

	def RemoveItem(self) -> None:
		...

	def SetAutoCompletion(self) -> None:
		...

	def SetAutoCompletionCaseSensitivity(self) -> None:
		...

	def SetCurrentIndex(self) -> None:
		...

	def SetCurrentText(self) -> None:
		...

	def SetDuplicatesEnabled(self) -> None:
		...

	def SetEditText(self) -> None:
		...

	def SetEditable(self) -> None:
		...

	def SetFrame(self) -> None:
		...

	def SetIconSize(self) -> None:
		...

	def SetInsertPolicy(self) -> None:
		...

	def SetItemText(self) -> None:
		...

	def SetLineEdit(self) -> None:
		...

	def SetMaxCount(self) -> None:
		...

	def SetMaxVisibleItems(self) -> None:
		...

	def SetMinimumContentsLength(self) -> None:
		...

	def SetSizeAdjustPolicy(self) -> None:
		...

	def ShowPopup(self) -> None:
		...

