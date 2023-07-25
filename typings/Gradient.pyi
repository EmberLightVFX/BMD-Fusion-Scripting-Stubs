from typing import Any

from Gradient import _Gradient
from FltPixel import _FltPixel


class _Gradient:

	#---Properties---#
	Value: dict[Any, Any]
	"""
	The gradient in table form

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
	def SetPreset(self, pstr: str) -> None:
		...
	def _newGrad(self, grad: _Gradient) -> _Gradient:
		...
	def _newPreset(self, pstr: str) -> _Gradient:
		...
	def ClearTables(self) -> None:
		...
	def info_text(self):
		...
	def GetColor(self, pos: float) -> _FltPixel:
		...
	def Clear(self) -> None:
		...
	def GetColorCount(self) -> int:
		...
	def AddColor(self, pos: float, pix: _FltPixel) -> None:
		...
	def QuickEvaluate(self, pos: float, cstr: str) -> _FltPixel:
		...
	def header_text(self):
		...

Gradient = _Gradient