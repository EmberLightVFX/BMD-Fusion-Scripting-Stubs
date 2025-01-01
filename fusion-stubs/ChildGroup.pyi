from Object import Object


class ChildGroup:

	#---Properties---#
	m_GroupID: str
	"""
	Read Only
	"""

	m_Owner: Object
	"""
	Read Only
	"""


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
	def GetID(self) -> None:
		...

	def GetOwner(self) -> None:
		...

