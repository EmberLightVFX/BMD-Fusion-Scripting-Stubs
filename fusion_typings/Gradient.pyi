from typing import Any

from FltPixel import FltPixel_


class Gradient_:

	#---Properties---#
	Value: dict[Any, Any]
	"""
	The gradient in table form

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
	def GetColor(self, pos: float) -> FltPixel_:
		...
	def info_text(self):
		...
	def GetColorCount(self) -> int:
		...
	def QuickEvaluate(self, pos: float, cstr: str) -> FltPixel_:
		...
	def SetPreset(self, pstr: str) -> None:
		...
	def _newGrad(self, grad: Gradient_) -> Gradient_:
		...
	def AddColor(self, pos: float, pix: FltPixel_) -> None:
		...
	def header_text(self):
		...
	def _newPreset(self, pstr: str) -> Gradient_:
		...
	def ClearTables(self) -> None:
		...
	def Clear(self) -> None:
		...

Gradient = Gradient_