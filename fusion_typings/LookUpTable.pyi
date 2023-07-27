from TagList import TagList_
from LUT import LUT_
from Object import Object_


class LookUpTable_:

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
	def _newDef(self) -> LookUpTable_:
		...
	def info_text(self) -> None:
		...
	def _newCopy(self, lut: LookUpTable_) -> LookUpTable_:
		...
	def GetTable(self, tags: TagList_) -> LUT_:
		...
	def Attach(self, obj: Object_) -> None:
		...
	def _newLUT(self, lut: LUT_, id: str) -> LookUpTable_:
		...
	def Detach(self) -> None:
		...
	def header_text(self) -> None:
		...
	def SetOneToOne(self, set: bool) -> None:
		...
	def GetValue(self, inval: float) -> float:
		...
	def IsOneToOne(self) -> bool:
		...

LookUpTable = LookUpTable_