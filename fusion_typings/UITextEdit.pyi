from typing import Any

class UITextEdit_:

	#---Properties---#
	Alignment: Any
	"""
	Read/Write
	"""
	FrameStyle: Any
	"""
	Read/Write
	"""
	AcceptRichText: Any
	"""
	Read/Write
	"""
	OverwriteMode: Any
	"""
	Read/Write
	"""
	HTML: Any
	"""
	Read/Write
	"""
	TabChangesFocus: Any
	"""
	Read/Write
	"""
	AutoFormatting: Any
	"""
	Read/Write
	"""
	CurrentFont: Any
	"""
	Write Only
	"""
	PlaceholderText: Any
	"""
	Read/Write
	"""
	TextBackgroundColor: Any
	"""
	Read/Write
	"""
	TextColor: Any
	"""
	Read/Write
	"""
	TextInteractionFlags: Any
	"""
	Read/Write
	"""
	LineWrapMode: Any
	"""
	Read/Write
	"""
	PlainText: Any
	"""
	Read/Write
	"""
	FontItalic: Any
	"""
	Read/Write
	"""
	ReadOnly: Any
	"""
	Read/Write
	"""
	Text: Any
	"""
	Write Only
	"""
	FontUnderline: Any
	"""
	Read/Write
	"""
	WordWrapMode: Any
	"""
	Read/Write
	"""
	Lexer: Any
	"""
	Read/Write
	"""
	UndoRedoEnabled: Any
	"""
	Read/Write
	"""
	FrameShadow: Any
	"""
	Read/Write
	"""
	FontFamily: Any
	"""
	Read/Write
	"""
	CursorWidth: Any
	"""
	Read/Write
	"""
	DocumentTitle: Any
	"""
	Read/Write
	"""
	FontPointSize: Any
	"""
	Read/Write
	"""
	LexerColors: Any
	"""
	Read/Write
	"""
	FrameShape: Any
	"""
	Read/Write
	"""
	FrameRect: Any
	"""
	Read/Write
	"""
	LineWidth: Any
	"""
	Read/Write
	"""
	LineWrapColumnOrWidth: Any
	"""
	Read/Write
	"""
	MidLineWidth: Any
	"""
	Read/Write
	"""
	FontWeight: Any
	"""
	Read/Write
	"""
	TabStopWidth: Any
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
	def SetLineWrapColumnOrWidth(self) -> None:
		...
	def GetLineWrapColumnOrWidth(self) -> None:
		...
	def SetReadOnly(self) -> None:
		...
	def SetAcceptRichText(self) -> None:
		...
	def GetAcceptRichText(self) -> None:
		...
	def SetText(self) -> None:
		...
	def SetOverwriteMode(self) -> None:
		...
	def GetOverwriteMode(self) -> None:
		...
	def SetUndoRedoEnabled(self) -> None:
		...
	def GetUndoRedoEnabled(self) -> None:
		...
	def SetTabChangesFocus(self) -> None:
		...
	def GetTabChangesFocus(self) -> None:
		...
	def SelectAll(self) -> None:
		...
	def Clear(self) -> None:
		...
	def SetTextInteractionFlags(self) -> None:
		...
	def GetTextInteractionFlags(self) -> None:
		...
	def SetAlignment(self) -> None:
		...
	def ScrollToAnchor(self) -> None:
		...
	def Copy(self) -> None:
		...
	def FrameWidth(self) -> None:
		...
	def GetReadOnly(self) -> None:
		...
	def SetFrameShadow(self) -> None:
		...
	def GetFrameShadow(self) -> None:
		...
	def SetFrameShape(self) -> None:
		...
	def GetFrameShape(self) -> None:
		...
	def SetFrameRect(self) -> None:
		...
	def GetFrameRect(self) -> None:
		...
	def SetMidLineWidth(self) -> None:
		...
	def GetMidLineWidth(self) -> None:
		...
	def SetLineWidth(self) -> None:
		...
	def GetLineWidth(self) -> None:
		...
	def SetFrameStyle(self) -> None:
		...
	def GetFrameStyle(self) -> None:
		...
	def Find(self) -> None:
		...
	def header_text(self):
		...
	def ZoomIn(self) -> None:
		...
	def Undo(self) -> None:
		...
	def SetHTML(self) -> None:
		...
	def SetLexerColors(self) -> None:
		...
	def SetPlaceholderText(self) -> None:
		...
	def InsertHTML(self) -> None:
		...
	def InsertPlainText(self) -> None:
		...
	def SetAutoFormatting(self) -> None:
		...
	def GetAutoFormatting(self) -> None:
		...
	def GetDocumentTitle(self) -> None:
		...
	def SetCurrentFont(self) -> None:
		...
	def GetFontFamily(self) -> None:
		...
	def SetTextBackgroundColor(self) -> None:
		...
	def GetTextBackgroundColor(self) -> None:
		...
	def GetFontUnderline(self) -> None:
		...
	def SetTextColor(self) -> None:
		...
	def GetTextColor(self) -> None:
		...
	def SetLexer(self) -> None:
		...
	def SetWordWrapMode(self) -> None:
		...
	def GetWordWrapMode(self) -> None:
		...
	def SetLineWrapMode(self) -> None:
		...
	def GetLineWrapMode(self) -> None:
		...
	def GetAlignment(self) -> None:
		...
	def Paste(self) -> None:
		...
	def GetHTML(self) -> None:
		...
	def SetPlainText(self) -> None:
		...
	def GetPlainText(self) -> None:
		...
	def GetLexer(self) -> None:
		...
	def SetFontItalic(self) -> None:
		...
	def GetFontItalic(self) -> None:
		...
	def GetFontPointSize(self) -> None:
		...
	def SetFontUnderline(self) -> None:
		...
	def GetLexerColors(self) -> None:
		...
	def Cut(self) -> None:
		...
	def SetFontWeight(self) -> None:
		...
	def GetFontWeight(self) -> None:
		...
	def MoveCursor(self) -> None:
		...
	def SetFontFamily(self) -> None:
		...
	def CanPaste(self) -> None:
		...
	def AnchorAt(self) -> None:
		...
	def SetFontPointSize(self) -> None:
		...
	def EnsureCursorVisible(self) -> None:
		...
	def ZoomOut(self) -> None:
		...
	def SetDocumentTitle(self) -> None:
		...
	def Append(self) -> None:
		...
	def Redo(self) -> None:
		...
	def SetCursorWidth(self) -> None:
		...
	def GetCursorWidth(self) -> None:
		...
	def GetPlaceholderText(self) -> None:
		...
	def SetTabStopWidth(self) -> None:
		...
	def GetTabStopWidth(self) -> None:
		...

UITextEdit = UITextEdit_