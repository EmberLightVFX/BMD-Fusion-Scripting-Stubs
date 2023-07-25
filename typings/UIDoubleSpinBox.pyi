from typing import Any

class _UIDoubleSpinBox:

	#---Properties---#
	Alignment: Any
	"""
	Read/Write
	"""
	ButtonSymbols: Any
	"""
	Read/Write
	"""
	Frame: Any
	"""
	Read/Write
	"""
	CleanText: Any
	"""
	Read Only
	"""
	Decimals: Any
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
	SingleStep: Any
	"""
	Read/Write
	"""
	Wrapping: Any
	"""
	Read/Write
	"""
	Suffix: Any
	"""
	Read/Write
	"""
	SpecialValueText: Any
	"""
	Read/Write
	"""
	Prefix: Any
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
	Accelerated: Any
	"""
	Read/Write
	"""
	KeyboardTracking: Any
	"""
	Read/Write
	"""
	CorrectionMode: Any
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
	def SetButtonSymbols(self) -> None:
		...
	def GetButtonSymbols(self) -> None:
		...
	def SetAlignment(self) -> None:
		...
	def GetAlignment(self) -> None:
		...
	def SetGroupSeparatorShown(self) -> None:
		...
	def GetGroupSeparatorShown(self) -> None:
		...
	def SetAccelerated(self) -> None:
		...
	def GetAccelerated(self) -> None:
		...
	def SetKeyboardTracking(self) -> None:
		...
	def GetKeyboardTracking(self) -> None:
		...
	def SetReadOnly(self) -> None:
		...
	def GetReadOnly(self) -> None:
		...
	def SetWrapping(self) -> None:
		...
	def GetWrapping(self) -> None:
		...
	def SetSpecialValueText(self) -> None:
		...
	def GetSpecialValueText(self) -> None:
		...
	def GetValue(self) -> None:
		...
	def GetFrame(self) -> None:
		...
	def SetFrame(self) -> None:
		...
	def SetRange(self) -> None:
		...
	def GetCleanText(self) -> None:
		...
	def SetDecimals(self) -> None:
		...
	def GetDecimals(self) -> None:
		...
	def SetMaximum(self) -> None:
		...
	def GetMaximum(self) -> None:
		...
	def SetMinimum(self) -> None:
		...
	def GetMinimum(self) -> None:
		...
	def SetSingleStep(self) -> None:
		...
	def GetSingleStep(self) -> None:
		...
	def SetSuffix(self) -> None:
		...
	def GetSuffix(self) -> None:
		...
	def SetPrefix(self) -> None:
		...
	def GetPrefix(self) -> None:
		...
	def header_text(self):
		...
	def SetValue(self) -> None:
		...
	def SelectAll(self) -> None:
		...
	def StepDown(self) -> None:
		...
	def StepUp(self) -> None:
		...
	def StepBy(self) -> None:
		...
	def SetCorrectionMode(self) -> None:
		...
	def GetCorrectionMode(self) -> None:
		...
	def Clear(self) -> None:
		...

UIDoubleSpinBox = _UIDoubleSpinBox