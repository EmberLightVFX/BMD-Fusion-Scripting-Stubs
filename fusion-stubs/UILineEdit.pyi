from typing import Any

class UILineEdit:

	#---Properties---#
	Alignment: Any

	ClearButtonEnabled: Any

	CursorMoveStyle: Any

	CursorPosition: Any

	DragEnabled: Any

	EchoMode: Any

	Frame: Any

	InputMask: Any

	MaxLength: Any

	Modified: Any

	PlaceholderText: Any

	ReadOnly: Any

	Text: Any


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
	def Backspace(self) -> None:
		...

	def Clear(self) -> None:
		...

	def Copy(self) -> None:
		...

	def CursorBackward(self) -> None:
		...

	def CursorForward(self) -> None:
		...

	def CursorPositionAt(self) -> None:
		...

	def CursorWordBackward(self) -> None:
		...

	def CursorWordForward(self) -> None:
		...

	def Cut(self) -> None:
		...

	def Del(self) -> None:
		...

	def Deselect(self) -> None:
		...

	def End(self) -> None:
		...

	def GetAlignment(self) -> None:
		...

	def GetClearButtonEnabled(self) -> None:
		...

	def GetCursorMoveStyle(self) -> None:
		...

	def GetCursorPosition(self) -> None:
		...

	def GetDragEnabled(self) -> None:
		...

	def GetEchoMode(self) -> None:
		...

	def GetFrame(self) -> None:
		...

	def GetInputMask(self) -> None:
		...

	def GetMaxLength(self) -> None:
		...

	def GetModified(self) -> None:
		...

	def GetPlaceholderText(self) -> None:
		...

	def GetReadOnly(self) -> None:
		...

	def GetText(self) -> None:
		...

	def HasAcceptableInput(self) -> None:
		...

	def HasSelectedText(self) -> None:
		...

	def Home(self) -> None:
		...

	def Insert(self) -> None:
		...

	def IsRedoAvailable(self) -> None:
		...

	def IsUndoAvailable(self) -> None:
		...

	def Paste(self) -> None:
		...

	def Redo(self) -> None:
		...

	def SelectAll(self) -> None:
		...

	def SelectedText(self) -> None:
		...

	def SelectionStart(self) -> None:
		...

	def SetAlignment(self) -> None:
		...

	def SetClearButtonEnabled(self) -> None:
		...

	def SetCursorMoveStyle(self) -> None:
		...

	def SetCursorPosition(self) -> None:
		...

	def SetDragEnabled(self) -> None:
		...

	def SetEchoMode(self) -> None:
		...

	def SetFrame(self) -> None:
		...

	def SetInputMask(self) -> None:
		...

	def SetMaxLength(self) -> None:
		...

	def SetModified(self) -> None:
		...

	def SetPlaceholderText(self) -> None:
		...

	def SetReadOnly(self) -> None:
		...

	def SetSelection(self) -> None:
		...

	def SetText(self) -> None:
		...

	def Undo(self) -> None:
		...

