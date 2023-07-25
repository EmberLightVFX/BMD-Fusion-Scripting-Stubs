from ViewShadeNode import _ViewShadeNode
from TagList import _TagList
from Input import _Input


class _ScriptViewShader:

	#---Properties---#
	Height: int
	"""
	Read Only
	"""
	Width: int
	"""
	Read Only
	"""
	m_ViewShadeNode: _ViewShadeNode
	"""
	Read/Write
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
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGS_VersionString: str

	REGS_UIName: str

	REGI_ClassType: int

	REGS_FileName: str

	REGB_ControlView: bool

	REGS_ID: str

	REGI_Priority: int

	REGB_Unpredictable: bool


	#---Methods---#
	def _AddInput(self, name: str, id: str, tags: _TagList) -> _Input:
		...
	def info_text(self):
		...
	def AddControlPage(self, name: str, tags: _TagList) -> int:
		...
	def header_text(self):
		...

ScriptViewShader = _ScriptViewShader