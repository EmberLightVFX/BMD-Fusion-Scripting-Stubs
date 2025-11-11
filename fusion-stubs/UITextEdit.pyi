from typing import Any

class UITextEdit:

    #---Properties---#
    AcceptRichText: Any

    Alignment: Any

    AutoFormatting: Any

    CurrentFont: Any
    """
    Write Only
    """

    CursorWidth: Any

    DocumentTitle: Any

    FontFamily: Any

    FontItalic: Any

    FontPointSize: Any

    FontUnderline: Any

    FontWeight: Any

    FrameRect: Any

    FrameShadow: Any

    FrameShape: Any

    FrameStyle: Any

    HTML: Any

    Lexer: Any

    LexerColors: Any

    LineWidth: Any

    LineWrapColumnOrWidth: Any

    LineWrapMode: Any

    MidLineWidth: Any

    OverwriteMode: Any

    PlaceholderText: Any

    PlainText: Any

    ReadOnly: Any

    TabChangesFocus: Any

    TabStopWidth: Any

    Text: Any
    """
    Write Only
    """

    TextBackgroundColor: Any

    TextColor: Any

    TextInteractionFlags: Any

    UndoRedoEnabled: Any

    WordWrapMode: Any


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
    def AnchorAt(self) -> None:
        ...

    def Append(self) -> None:
        ...

    def CanPaste(self) -> None:
        ...

    def Clear(self) -> None:
        ...

    def Copy(self) -> None:
        ...

    def Cut(self) -> None:
        ...

    def EnsureCursorVisible(self) -> None:
        ...

    def Find(self) -> None:
        ...

    def FrameWidth(self) -> None:
        ...

    def GetAcceptRichText(self) -> None:
        ...

    def GetAlignment(self) -> None:
        ...

    def GetAutoFormatting(self) -> None:
        ...

    def GetCursorWidth(self) -> None:
        ...

    def GetDocumentTitle(self) -> None:
        ...

    def GetFontFamily(self) -> None:
        ...

    def GetFontItalic(self) -> None:
        ...

    def GetFontPointSize(self) -> None:
        ...

    def GetFontUnderline(self) -> None:
        ...

    def GetFontWeight(self) -> None:
        ...

    def GetFrameRect(self) -> None:
        ...

    def GetFrameShadow(self) -> None:
        ...

    def GetFrameShape(self) -> None:
        ...

    def GetFrameStyle(self) -> None:
        ...

    def GetHTML(self) -> None:
        ...

    def GetLexer(self) -> None:
        ...

    def GetLexerColors(self) -> None:
        ...

    def GetLineWidth(self) -> None:
        ...

    def GetLineWrapColumnOrWidth(self) -> None:
        ...

    def GetLineWrapMode(self) -> None:
        ...

    def GetMidLineWidth(self) -> None:
        ...

    def GetOverwriteMode(self) -> None:
        ...

    def GetPlaceholderText(self) -> None:
        ...

    def GetPlainText(self) -> None:
        ...

    def GetReadOnly(self) -> None:
        ...

    def GetTabChangesFocus(self) -> None:
        ...

    def GetTabStopWidth(self) -> None:
        ...

    def GetTextBackgroundColor(self) -> None:
        ...

    def GetTextColor(self) -> None:
        ...

    def GetTextInteractionFlags(self) -> None:
        ...

    def GetUndoRedoEnabled(self) -> None:
        ...

    def GetWordWrapMode(self) -> None:
        ...

    def InsertHTML(self) -> None:
        ...

    def InsertPlainText(self) -> None:
        ...

    def MoveCursor(self) -> None:
        ...

    def Paste(self) -> None:
        ...

    def Redo(self) -> None:
        ...

    def ScrollToAnchor(self) -> None:
        ...

    def SelectAll(self) -> None:
        ...

    def SetAcceptRichText(self) -> None:
        ...

    def SetAlignment(self) -> None:
        ...

    def SetAutoFormatting(self) -> None:
        ...

    def SetCurrentFont(self) -> None:
        ...

    def SetCursorWidth(self) -> None:
        ...

    def SetDocumentTitle(self) -> None:
        ...

    def SetFontFamily(self) -> None:
        ...

    def SetFontItalic(self) -> None:
        ...

    def SetFontPointSize(self) -> None:
        ...

    def SetFontUnderline(self) -> None:
        ...

    def SetFontWeight(self) -> None:
        ...

    def SetFrameRect(self) -> None:
        ...

    def SetFrameShadow(self) -> None:
        ...

    def SetFrameShape(self) -> None:
        ...

    def SetFrameStyle(self) -> None:
        ...

    def SetHTML(self) -> None:
        ...

    def SetLexer(self) -> None:
        ...

    def SetLexerColors(self) -> None:
        ...

    def SetLineWidth(self) -> None:
        ...

    def SetLineWrapColumnOrWidth(self) -> None:
        ...

    def SetLineWrapMode(self) -> None:
        ...

    def SetMidLineWidth(self) -> None:
        ...

    def SetOverwriteMode(self) -> None:
        ...

    def SetPlaceholderText(self) -> None:
        ...

    def SetPlainText(self) -> None:
        ...

    def SetReadOnly(self) -> None:
        ...

    def SetTabChangesFocus(self) -> None:
        ...

    def SetTabStopWidth(self) -> None:
        ...

    def SetText(self) -> None:
        ...

    def SetTextBackgroundColor(self) -> None:
        ...

    def SetTextColor(self) -> None:
        ...

    def SetTextInteractionFlags(self) -> None:
        ...

    def SetUndoRedoEnabled(self) -> None:
        ...

    def SetWordWrapMode(self) -> None:
        ...

    def Undo(self) -> None:
        ...

    def ZoomIn(self) -> None:
        ...

    def ZoomOut(self) -> None:
        ...

