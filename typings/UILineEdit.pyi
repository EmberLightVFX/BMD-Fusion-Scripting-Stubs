from typing import Any

class _UILineEdit:

	#---Properties---#
	DragEnabled: Any
	"""
	Read/Write
	"""
	Alignment: Any
	"""
	Read/Write
	"""
	Frame: Any
	"""
	Read/Write
	"""
	Modified: Any
	"""
	Read/Write
	"""
	Text: Any
	"""
	Read/Write
	"""
	ClearButtonEnabled: Any
	"""
	Read/Write
	"""
	CursorMoveStyle: Any
	"""
	Read/Write
	"""
	MaxLength: Any
	"""
	Read/Write
	"""
	PlaceholderText: Any
	"""
	Read/Write
	"""
	EchoMode: Any
	"""
	Read/Write
	"""
	CursorPosition: Any
	"""
	Read/Write
	"""
	ReadOnly: Any
	"""
	Read/Write
	"""
	InputMask: Any
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
	def End(self) -> None:
		...
	def SetAlignment(self) -> None:
		...
	def GetAlignment(self) -> None:
		...
	def SetCursorMoveStyle(self) -> None:
		...
	def GetCursorMoveStyle(self) -> None:
		...
	def SetEchoMode(self) -> None:
		...
	def GetEchoMode(self) -> None:
		...
	def Copy(self) -> None:
		...
	def CursorWordBackward(self) -> None:
		...
	def CursorWordForward(self) -> None:
		...
	def CursorBackward(self) -> None:
		...
	def CursorForward(self) -> None:
		...
	def HasSelectedText(self) -> None:
		...
	def Home(self) -> None:
		...
	def Del(self) -> None:
		...
	def Backspace(self) -> None:
		...
	def Insert(self) -> None:
		...
	def Deselect(self) -> None:
		...
	def Cut(self) -> None:
		...
	def Redo(self) -> None:
		...
	def Undo(self) -> None:
		...
	def HasAcceptableInput(self) -> None:
		...
	def IsRedoAvailable(self) -> None:
		...
	def IsUndoAvailable(self) -> None:
		...
	def SetInputMask(self) -> None:
		...
	def GetInputMask(self) -> None:
		...
	def GetText(self) -> None:
		...
	def GetCursorPosition(self) -> None:
		...
	def SetDragEnabled(self) -> None:
		...
	def GetDragEnabled(self) -> None:
		...
	def SetText(self) -> None:
		...
	def Clear(self) -> None:
		...
	def SetSelection(self) -> None:
		...
	def SetReadOnly(self) -> None:
		...
	def SetPlaceholderText(self) -> None:
		...
	def SetCursorPosition(self) -> None:
		...
	def SelectionStart(self) -> None:
		...
	def SetClearButtonEnabled(self) -> None:
		...
	def GetClearButtonEnabled(self) -> None:
		...
	def SetFrame(self) -> None:
		...
	def SetModified(self) -> None:
		...
	def GetModified(self) -> None:
		...
	def SetMaxLength(self) -> None:
		...
	def GetMaxLength(self) -> None:
		...
	def SelectedText(self) -> None:
		...
	def SelectAll(self) -> None:
		...
	def GetPlaceholderText(self) -> None:
		...
	def Paste(self) -> None:
		...
	def GetFrame(self) -> None:
		...
	def GetReadOnly(self) -> None:
		...
	def CursorPositionAt(self) -> None:
		...
	def header_text(self):
		...

UILineEdit = _UILineEdit