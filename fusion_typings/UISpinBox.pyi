from typing import Any

class UISpinBox_:

	#---Properties---#
	Alignment: Any
	"""
	Read/Write
	"""
	Wrapping: Any
	"""
	Read/Write
	"""
	CleanText: Any
	"""
	Read Only
	"""
	SpecialValueText: Any
	"""
	Read/Write
	"""
	DisplayIntegerBase: Any
	"""
	Read/Write
	"""
	Minimum: Any
	"""
	Read/Write
	"""
	Maximum: Any
	"""
	Read/Write
	"""
	ReadOnly: Any
	"""
	Read/Write
	"""
	Prefix: Any
	"""
	Read/Write
	"""
	CorrectionMode: Any
	"""
	Read/Write
	"""
	Frame: Any
	"""
	Read/Write
	"""
	ButtonSymbols: Any
	"""
	Read/Write
	"""
	Suffix: Any
	"""
	Read/Write
	"""
	GroupSeparatorShown: Any
	"""
	Read/Write
	"""
	Value: Any
	"""
	Read/Write
	"""
	SingleStep: Any
	"""
	Read/Write
	"""
	Accelerated: Any
	"""
	Read/Write
	"""
	KeyboardTracking: Any
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
	def GetMinimum(self) -> None:
		...
	def SetWrapping(self) -> None:
		...
	def GetWrapping(self) -> None:
		...
	def SetReadOnly(self) -> None:
		...
	def SetSpecialValueText(self) -> None:
		...
	def GetSpecialValueText(self) -> None:
		...
	def GetFrame(self) -> None:
		...
	def SelectAll(self) -> None:
		...
	def Clear(self) -> None:
		...
	def SetRange(self) -> None:
		...
	def StepUp(self) -> None:
		...
	def SetFrame(self) -> None:
		...
	def GetSingleStep(self) -> None:
		...
	def SetValue(self) -> None:
		...
	def GetCleanText(self) -> None:
		...
	def GetAlignment(self) -> None:
		...
	def SetDisplayIntegerBase(self) -> None:
		...
	def GetDisplayIntegerBase(self) -> None:
		...
	def header_text(self) -> None:
		...
	def SetSuffix(self) -> None:
		...
	def GetSuffix(self) -> None:
		...
	def GetKeyboardTracking(self) -> None:
		...
	def SetPrefix(self) -> None:
		...
	def GetPrefix(self) -> None:
		...
	def GetMaximum(self) -> None:
		...
	def StepDown(self) -> None:
		...
	def GetReadOnly(self) -> None:
		...
	def StepBy(self) -> None:
		...
	def SetCorrectionMode(self) -> None:
		...
	def GetCorrectionMode(self) -> None:
		...
	def SetAlignment(self) -> None:
		...
	def SetButtonSymbols(self) -> None:
		...
	def GetButtonSymbols(self) -> None:
		...
	def GetValue(self) -> None:
		...
	def SetGroupSeparatorShown(self) -> None:
		...
	def GetGroupSeparatorShown(self) -> None:
		...
	def SetSingleStep(self) -> None:
		...
	def SetAccelerated(self) -> None:
		...
	def GetAccelerated(self) -> None:
		...
	def SetMaximum(self) -> None:
		...
	def SetKeyboardTracking(self) -> None:
		...
	def SetMinimum(self) -> None:
		...

UISpinBox = UISpinBox_