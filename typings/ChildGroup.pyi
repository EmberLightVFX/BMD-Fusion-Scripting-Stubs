from Object import _Object


class _ChildGroup:

	#---Properties---#
	m_Owner: _Object
	"""
	Read Only
	"""
	m_GroupID: str
	"""
	Read Only
	"""

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_VersionString: str

	REGS_ID: str

	REGB_ControlView: bool

	REGI_Priority: int


	#---Methods---#
	def GetOwner(self):
		...
	def GetID(self):
		...
	def header_text(self):
		...

ChildGroup = _ChildGroup