from LUT import _LUT
from LookUpTable import _LookUpTable
from TagList import _TagList
from Object import _Object


class _LookUpTable:

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
	def SetOneToOne(self, set: bool) -> None:
		...
	def GetValue(self, inval: float) -> float:
		...
	def _newLUT(self, lut: _LUT, id: str) -> _LookUpTable:
		...
	def _newDef(self) -> _LookUpTable:
		...
	def info_text(self):
		...
	def GetTable(self, tags: _TagList) -> _LUT:
		...
	def Detach(self) -> None:
		...
	def _newCopy(self, lut: _LookUpTable) -> _LookUpTable:
		...
	def header_text(self):
		...
	def Attach(self, obj: _Object) -> None:
		...
	def IsOneToOne(self) -> bool:
		...

LookUpTable = _LookUpTable