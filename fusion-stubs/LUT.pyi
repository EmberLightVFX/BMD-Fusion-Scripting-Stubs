from TagList import TagList


class LUT:

	#---Properties---#
	m_EndIn: float

	m_EndSlope: float

	m_Maximum: float

	m_MaximumValue: float

	m_Minimum: float

	m_MinimumValue: float

	m_NumEntries: int

	m_Offset: int

	m_StartIn: float

	m_StartSlope: float

	m_Type: int

	m_Table: None


	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def EntrySize(self, ty: int) -> int:
		...

	def GetValue(self, inval: float) -> float:
		...

	def Table(self) -> None:
		...

	def _newLUT(self, lut: LUT) -> LUT:
		...

	def _newNums(self, num: int, ty: int) -> LUT:
		...

	def _newTags(self, tags: TagList) -> LUT:
		...

