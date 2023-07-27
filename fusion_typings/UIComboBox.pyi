from typing import Any

class UIComboBox_:

	#---Properties---#
	MaxVisibleItems: Any
	"""
	Read/Write
	"""
	SizeAdjustPolicy: Any
	"""
	Read/Write
	"""
	MinimumContentsLength: Any
	"""
	Read/Write
	"""
	InsertPolicy: Any
	"""
	Read/Write
	"""
	DuplicatesEnabled: Any
	"""
	Read/Write
	"""
	LineEdit: Any
	"""
	Read/Write
	"""
	Frame: Any
	"""
	Read/Write
	"""
	ItemText: Any
	"""
	Read Only
	"""
	Editable: Any
	"""
	Read/Write
	"""
	AutoCompletion: Any
	"""
	Read/Write
	"""
	IconSize: Any
	"""
	Read/Write
	"""
	CurrentText: Any
	"""
	Read/Write
	"""
	MaxCount: Any
	"""
	Read/Write
	"""
	AutoCompletionCaseSensitivity: Any
	"""
	Read/Write
	"""
	CurrentIndex: Any
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
	def GetFrame(self) -> None:
		...
	def SetSizeAdjustPolicy(self) -> None:
		...
	def GetSizeAdjustPolicy(self) -> None:
		...
	def SetInsertPolicy(self) -> None:
		...
	def GetInsertPolicy(self) -> None:
		...
	def SetAutoCompletionCaseSensitivity(self) -> None:
		...
	def GetAutoCompletionCaseSensitivity(self) -> None:
		...
	def SetItemText(self) -> None:
		...
	def GetItemText(self) -> None:
		...
	def InsertItems(self) -> None:
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
	def Count(self) -> None:
		...
	def RemoveItem(self) -> None:
		...
	def SetLineEdit(self) -> None:
		...
	def GetLineEdit(self) -> None:
		...
	def SetEditable(self) -> None:
		...
	def AddItem(self) -> None:
		...
	def SetCurrentText(self) -> None:
		...
	def GetCurrentText(self) -> None:
		...
	def SetCurrentIndex(self) -> None:
		...
	def GetCurrentIndex(self) -> None:
		...
	def SetMinimumContentsLength(self) -> None:
		...
	def GetMinimumContentsLength(self) -> None:
		...
	def GetIconSize(self) -> None:
		...
	def SetDuplicatesEnabled(self) -> None:
		...
	def GetDuplicatesEnabled(self) -> None:
		...
	def Clear(self) -> None:
		...
	def SetFrame(self) -> None:
		...
	def SetIconSize(self) -> None:
		...
	def SetAutoCompletion(self) -> None:
		...
	def GetAutoCompletion(self) -> None:
		...
	def GetEditable(self) -> None:
		...
	def SetMaxCount(self) -> None:
		...
	def GetMaxCount(self) -> None:
		...
	def header_text(self) -> None:
		...
	def SetMaxVisibleItems(self) -> None:
		...
	def GetMaxVisibleItems(self) -> None:
		...

UIComboBox = UIComboBox_