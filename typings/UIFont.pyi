from typing import Any, Literal

class _UIFont:

	#---Properties---#
	Italic: Any
	"""
	Read/Write
	"""
	Bold: Any
	"""
	Read/Write
	"""
	HintingPreference: Any
	"""
	Read/Write
	"""
	StyleStrategy: Any
	"""
	Read/Write
	"""
	PointSize: Any
	"""
	Read/Write
	"""
	Stretch: Any
	"""
	Read/Write
	"""
	StyleName: Any
	"""
	Read/Write
	"""
	Family: Any
	"""
	Read/Write
	"""
	RawMode: Any
	"""
	Read/Write
	"""
	Kerning: Any
	"""
	Read/Write
	"""
	Weight: Any
	"""
	Read/Write
	"""
	FixedPitch: Any
	"""
	Read/Write
	"""
	PixelSize: Any
	"""
	Read/Write
	"""
	StrikeOut: Any
	"""
	Read/Write
	"""
	Overline: Any
	"""
	Read/Write
	"""
	Underline: Any
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
	def SetHintingPreference(self) -> None:
		...
	def GetHintingPreference(self) -> None:
		...
	def SetStyleStrategy(self) -> None:
		...
	def GetStyleStrategy(self) -> None:
		...
	def SetStretch(self) -> None:
		...
	def GetStretch(self) -> None:
		...
	def SetWeight(self) -> None:
		...
	def header_text(self):
		...
	def SetRawMode(self) -> None:
		...
	def GetRawMode(self) -> None:
		...
	def SetKerning(self) -> None:
		...
	def GetKerning(self) -> None:
		...
	def SetFixedPitch(self) -> None:
		...
	def GetFixedPitch(self) -> None:
		...
	def SetStrikeOut(self) -> None:
		...
	def GetStrikeOut(self) -> None:
		...
	def SetOverline(self) -> None:
		...
	def GetOverline(self) -> None:
		...
	def SetUnderline(self) -> None:
		...
	def GetUnderline(self) -> None:
		...
	def SetItalic(self) -> None:
		...
	def GetItalic(self) -> None:
		...
	def SetBold(self) -> None:
		...
	def GetBold(self) -> None:
		...
	def SetPixelSize(self) -> None:
		...
	def GetPixelSize(self) -> None:
		...
	def SetPointSize(self) -> None:
		...
	def GetPointSize(self) -> None:
		...
	def SetStyleName(self) -> None:
		...
	def GetStyleName(self) -> None:
		...
	def SetFamily(self) -> None:
		...
	def GetFamily(self) -> None:
		...
	def GetWeight(self) -> None:
		...

UIFont = _UIFont