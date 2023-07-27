from Object import Object_


class ChildGroup_:

	#---Properties---#
	m_GroupID: str
	"""
	Read Only
	"""
	m_Owner: Object_
	"""
	Read Only
	"""

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def header_text(self):
		...
	def GetID(self):
		...
	def GetOwner(self):
		...

ChildGroup = ChildGroup_