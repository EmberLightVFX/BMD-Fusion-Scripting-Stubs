from typing import Any, Literal

class _UISlider:

	#---Properties---#
	SliderDown: Any
	"""
	Read/Write
	"""
	Orientation: Any
	"""
	Read/Write
	"""
	Value: Any
	"""
	Read/Write
	"""
	TickPosition: Any
	"""
	Read/Write
	"""
	SliderPosition: Any
	"""
	Read/Write
	"""
	TickInterval: Any
	"""
	Read/Write
	"""
	PageStep: Any
	"""
	Read/Write
	"""
	InvertedControls: Any
	"""
	Read/Write
	"""
	Maximum: Any
	"""
	Read/Write
	"""
	SingleStep: Any
	"""
	Read/Write
	"""
	InvertedAppearance: Any
	"""
	Read/Write
	"""
	Minimum: Any
	"""
	Read/Write
	"""
	Tracking: Any
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
	def GetTickInterval(self) -> None:
		...
	def SetTickPosition(self) -> None:
		...
	def GetTickPosition(self) -> None:
		...
	def SetOrientation(self) -> None:
		...
	def GetOrientation(self) -> None:
		...
	def SetInvertedControls(self) -> None:
		...
	def GetInvertedControls(self) -> None:
		...
	def SetInvertedAppearance(self) -> None:
		...
	def header_text(self):
		...
	def TriggerAction(self) -> None:
		...
	def SetSliderDown(self) -> None:
		...
	def GetSliderDown(self) -> None:
		...
	def SetTickInterval(self) -> None:
		...
	def SetTracking(self) -> None:
		...
	def GetTracking(self) -> None:
		...
	def SetValue(self) -> None:
		...
	def SetSliderPosition(self) -> None:
		...
	def GetSliderPosition(self) -> None:
		...
	def GetValue(self) -> None:
		...
	def SetPageStep(self) -> None:
		...
	def GetPageStep(self) -> None:
		...
	def SetRange(self) -> None:
		...
	def SetSingleStep(self) -> None:
		...
	def GetSingleStep(self) -> None:
		...
	def GetInvertedAppearance(self) -> None:
		...
	def SetMaximum(self) -> None:
		...
	def GetMaximum(self) -> None:
		...
	def SetMinimum(self) -> None:
		...

UISlider = _UISlider