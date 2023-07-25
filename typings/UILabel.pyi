from typing import Any

class _UILabel:

	#---Properties---#
	WordWrap: Any
	"""
	Read/Write
	"""
	Alignment: Any
	"""
	Read/Write
	"""
	Margin: Any
	"""
	Read/Write
	"""
	TextFormat: Any
	"""
	Read/Write
	"""
	TextInteractionFlags: Any
	"""
	Read/Write
	"""
	LineWidth: Any
	"""
	Read/Write
	"""
	Text: Any
	"""
	Read/Write
	"""
	ScaledContents: Any
	"""
	Read/Write
	"""
	FrameStyle: Any
	"""
	Read/Write
	"""
	FrameShadow: Any
	"""
	Read/Write
	"""
	OpenExternalLinks: Any
	"""
	Read/Write
	"""
	MidLineWidth: Any
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
	Indent: Any
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
	def SetAlignment(self) -> None:
		...
	def GetAlignment(self) -> None:
		...
	def SetText(self) -> None:
		...
	def SelectionStart(self) -> None:
		...
	def SelectedText(self) -> None:
		...
	def HasSelectedText(self) -> None:
		...
	def SetSelection(self) -> None:
		...
	def SetTextInteractionFlags(self) -> None:
		...
	def GetTextInteractionFlags(self) -> None:
		...
	def SetScaledContents(self) -> None:
		...
	def GetScaledContents(self) -> None:
		...
	def SetOpenExternalLinks(self) -> None:
		...
	def GetOpenExternalLinks(self) -> None:
		...
	def SetMargin(self) -> None:
		...
	def GetMargin(self) -> None:
		...
	def SetIndent(self) -> None:
		...
	def GetIndent(self) -> None:
		...
	def GetText(self) -> None:
		...
	def SetWordWrap(self) -> None:
		...
	def GetWordWrap(self) -> None:
		...
	def FrameWidth(self) -> None:
		...
	def SetTextFormat(self) -> None:
		...
	def GetTextFormat(self) -> None:
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
	def header_text(self):
		...

UILabel = _UILabel