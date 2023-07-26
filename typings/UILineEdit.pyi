from typing import Any, Literal

class _UILineEdit:

	#---Properties---#
	CursorMoveStyle: Any
	"""
	Read/Write
	"""
	EchoMode: Any
	"""
	Read/Write
	"""
	Alignment: Any
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
	Frame: Any
	"""
	Read/Write
	"""
	PlaceholderText: Any
	"""
	Read/Write
	"""
	CursorPosition: Any
	"""
	Read/Write
	"""
	Modified: Any
	"""
	Read/Write
	"""
	MaxLength: Any
	"""
	Read/Write
	"""
	Text: Any
	"""
	Read/Write
	"""
	DragEnabled: Any
	"""
	Read/Write
	"""
	ClearButtonEnabled: Any
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
	def SetModified(self) -> None:
		...
	def GetModified(self) -> None:
		...
	def SetReadOnly(self) -> None:
		...
	def SetMaxLength(self) -> None:
		...
	def GetMaxLength(self) -> None:
		...
	def SelectedText(self) -> None:
		...
	def HasSelectedText(self) -> None:
		...
	def GetPlaceholderText(self) -> None:
		...
	def header_text(self):
		...
	def End(self) -> None:
		...
	def Undo(self) -> None:
		...
	def SetText(self) -> None:
		...
	def SetSelection(self) -> None:
		...
	def SetPlaceholderText(self) -> None:
		...
	def SelectAll(self) -> None:
		...
	def GetFrame(self) -> None:
		...
	def Clear(self) -> None:
		...
	def Deselect(self) -> None:
		...
	def SetCursorMoveStyle(self) -> None:
		...
	def GetCursorMoveStyle(self) -> None:
		...
	def CursorWordForward(self) -> None:
		...
	def SetEchoMode(self) -> None:
		...
	def GetEchoMode(self) -> None:
		...
	def SelectionStart(self) -> None:
		...
	def CursorWordBackward(self) -> None:
		...
	def GetAlignment(self) -> None:
		...
	def CursorBackward(self) -> None:
		...
	def CursorForward(self) -> None:
		...
	def CursorPositionAt(self) -> None:
		...
	def Home(self) -> None:
		...
	def Del(self) -> None:
		...
	def Backspace(self) -> None:
		...
	def Insert(self) -> None:
		...
	def GetText(self) -> None:
		...
	def Cut(self) -> None:
		...
	def Redo(self) -> None:
		...
	def GetReadOnly(self) -> None:
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
	def SetAlignment(self) -> None:
		...
	def SetCursorPosition(self) -> None:
		...
	def GetCursorPosition(self) -> None:
		...
	def Paste(self) -> None:
		...
	def SetDragEnabled(self) -> None:
		...
	def GetDragEnabled(self) -> None:
		...
	def Copy(self) -> None:
		...
	def SetFrame(self) -> None:
		...
	def SetClearButtonEnabled(self) -> None:
		...
	def GetClearButtonEnabled(self) -> None:
		...

UILineEdit = _UILineEdit