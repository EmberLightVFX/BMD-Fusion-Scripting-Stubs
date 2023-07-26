from typing import Literal

from TagList import _TagList
from LUT import _LUT
from Object import _Object


class _LookUpTable:

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
	def _newDef(self) -> _LookUpTable:
		...
	def info_text(self):
		...
	def _newCopy(self, lut: _LookUpTable) -> _LookUpTable:
		...
	def GetTable(self, tags: _TagList) -> _LUT:
		...
	def Attach(self, obj: _Object) -> None:
		...
	def _newLUT(self, lut: _LUT, id: str) -> _LookUpTable:
		...
	def Detach(self) -> None:
		...
	def header_text(self):
		...
	def SetOneToOne(self, set: bool) -> None:
		...
	def GetValue(self, inval: float) -> float:
		...
	def IsOneToOne(self) -> bool:
		...

LookUpTable = _LookUpTable