from typing import Any

class _UIComboBox:

	#---Properties---#
	InsertPolicy: Any
	"""
	Read/Write
	"""
	DuplicatesEnabled: Any
	"""
	Read/Write
	"""
	AutoCompletionCaseSensitivity: Any
	"""
	Read/Write
	"""
	Frame: Any
	"""
	Read/Write
	"""
	MinimumContentsLength: Any
	"""
	Read/Write
	"""
	Editable: Any
	"""
	Read/Write
	"""
	AutoCompletion: Any
	"""
	Read/Write
	"""
	ItemText: Any
	"""
	Read Only
	"""
	CurrentText: Any
	"""
	Read/Write
	"""
	MaxCount: Any
	"""
	Read/Write
	"""
	LineEdit: Any
	"""
	Read/Write
	"""
	CurrentIndex: Any
	"""
	Read/Write
	"""
	MaxVisibleItems: Any
	"""
	Read/Write
	"""
	SizeAdjustPolicy: Any
	"""
	Read/Write
	"""
	IconSize: Any
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
	def SetAutoCompletionCaseSensitivity(self) -> None:
		...
	def GetAutoCompletionCaseSensitivity(self) -> None:
		...
	def SetItemText(self) -> None:
		...
	def GetItemText(self) -> None:
		...
	def AddItem(self) -> None:
		...
	def AddItems(self) -> None:
		...
	def SetEditText(self) -> None:
		...
	def ClearEditText(self) -> None:
		...
	def InsertSeparator(self) -> None:
		...
	def InsertItem(self) -> None:
		...
	def HidePopup(self) -> None:
		...
	def ShowPopup(self) -> None:
		...
	def header_text(self):
		...
	def RemoveItem(self) -> None:
		...
	def SetLineEdit(self) -> None:
		...
	def GetLineEdit(self) -> None:
		...
	def SetEditable(self) -> None:
		...
	def GetEditable(self) -> None:
		...
	def SetCurrentText(self) -> None:
		...
	def GetCurrentText(self) -> None:
		...
	def SetCurrentIndex(self) -> None:
		...
	def GetCurrentIndex(self) -> None:
		...
	def SetIconSize(self) -> None:
		...
	def GetMinimumContentsLength(self) -> None:
		...
	def SetDuplicatesEnabled(self) -> None:
		...
	def GetDuplicatesEnabled(self) -> None:
		...
	def SetFrame(self) -> None:
		...
	def SetAutoCompletion(self) -> None:
		...
	def GetAutoCompletion(self) -> None:
		...
	def SetMaxCount(self) -> None:
		...
	def GetMaxCount(self) -> None:
		...
	def SetMaxVisibleItems(self) -> None:
		...
	def Clear(self) -> None:
		...
	def Count(self) -> None:
		...
	def SetMinimumContentsLength(self) -> None:
		...
	def GetFrame(self) -> None:
		...
	def InsertItems(self) -> None:
		...
	def GetIconSize(self) -> None:
		...
	def SetSizeAdjustPolicy(self) -> None:
		...
	def GetSizeAdjustPolicy(self) -> None:
		...
	def GetMaxVisibleItems(self) -> None:
		...
	def SetInsertPolicy(self) -> None:
		...
	def GetInsertPolicy(self) -> None:
		...

UIComboBox = _UIComboBox