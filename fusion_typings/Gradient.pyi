from typing import Any

from FltPixel import _FltPixel


class _Gradient:

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
	def GetColor(self, pos: float) -> _FltPixel:
		...
	def info_text(self):
		...
	def GetColorCount(self) -> int:
		...
	def QuickEvaluate(self, pos: float, cstr: str) -> _FltPixel:
		...
	def SetPreset(self, pstr: str) -> None:
		...
	def _newGrad(self, grad: _Gradient) -> _Gradient:
		...
	def AddColor(self, pos: float, pix: _FltPixel) -> None:
		...
	def header_text(self):
		...
	def _newPreset(self, pstr: str) -> _Gradient:
		...
	def ClearTables(self) -> None:
		...
	def Clear(self) -> None:
		...

Gradient = _Gradient