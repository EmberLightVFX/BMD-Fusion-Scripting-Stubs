from typing import Any

class _UISlider:

	#---Properties---#
	SingleStep: Any
	"""
	Read/Write
	"""
	InvertedControls: Any
	"""
	Read/Write
	"""
	Value: Any
	"""
	Read/Write
	"""
	InvertedAppearance: Any
	"""
	Read/Write
	"""
	SliderDown: Any
	"""
	Read/Write
	"""
	Tracking: Any
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
	Minimum: Any
	"""
	Read/Write
	"""
	PageStep: Any
	"""
	Read/Write
	"""
	TickPosition: Any
	"""
	Read/Write
	"""
	Maximum: Any
	"""
	Read/Write
	"""
	Orientation: Any
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
	def SetTracking(self) -> None:
		...
	def GetTracking(self) -> None:
		...
	def GetSliderDown(self) -> None:
		...
	def TriggerAction(self) -> None:
		...
	def SetSliderPosition(self) -> None:
		...
	def GetSliderPosition(self) -> None:
		...
	def GetTickInterval(self) -> None:
		...
	def SetPageStep(self) -> None:
		...
	def GetPageStep(self) -> None:
		...
	def GetTickPosition(self) -> None:
		...
	def SetMinimum(self) -> None:
		...
	def GetMinimum(self) -> None:
		...
	def header_text(self):
		...
	def GetSingleStep(self) -> None:
		...
	def GetInvertedControls(self) -> None:
		...
	def SetTickInterval(self) -> None:
		...
	def SetInvertedAppearance(self) -> None:
		...
	def GetInvertedAppearance(self) -> None:
		...
	def GetValue(self) -> None:
		...
	def SetSliderDown(self) -> None:
		...
	def SetTickPosition(self) -> None:
		...
	def SetValue(self) -> None:
		...
	def SetSingleStep(self) -> None:
		...
	def SetRange(self) -> None:
		...
	def SetOrientation(self) -> None:
		...
	def SetMaximum(self) -> None:
		...
	def GetOrientation(self) -> None:
		...
	def GetMaximum(self) -> None:
		...
	def SetInvertedControls(self) -> None:
		...

UISlider = _UISlider