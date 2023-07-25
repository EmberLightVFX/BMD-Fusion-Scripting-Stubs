from typing import Any

class _UIFont:

	#---Properties---#
	Stretch: Any
	"""
	Read/Write
	"""
	StyleName: Any
	"""
	Read/Write
	"""
	PixelSize: Any
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
	FixedPitch: Any
	"""
	Read/Write
	"""
	Underline: Any
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
	Weight: Any
	"""
	Read/Write
	"""
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
	Family: Any
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
	def SetWeight(self) -> None:
		...
	def GetWeight(self) -> None:
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
	def header_text(self):
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
	def SetHintingPreference(self) -> None:
		...
	def GetHintingPreference(self) -> None:
		...
	def SetStyleStrategy(self) -> None:
		...
	def GetStyleStrategy(self) -> None:
		...
	def SetOverline(self) -> None:
		...
	def SetStretch(self) -> None:
		...
	def GetStretch(self) -> None:
		...

UIFont = _UIFont