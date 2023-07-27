from ViewShadeNode import _ViewShadeNode
from TagList import _TagList
from Input import _Input


class _ScriptViewShader:

	#---Properties---#
	m_ViewShadeNode: _ViewShadeNode
	"""
	Read/Write
	"""
	Height: int
	"""
	Read Only
	"""
	Width: int
	"""
	Read Only
	"""
	RealWidth: int
	"""
	Read Only
	"""
	RealHeight: int
	"""
	Read Only
	"""

	#---Attributes---#
	REGS_FileName: str

	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGB_ControlView: bool

	REGS_Name: str

	REGB_Unpredictable: bool

	REGS_UIName: str


	#---Methods---#
	def header_text(self):
		...
	def info_text(self):
		...
	def AddControlPage(self, name: str, tags: _TagList) -> int:
		...
	def _AddInput(self, name: str, id: str, tags: _TagList) -> _Input:
		...

ScriptViewShader = _ScriptViewShader