from ViewShadeNode import ViewShadeNode_
from TagList import TagList_
from Input import Input_


class ScriptViewShader_:

	#---Properties---#
	m_ViewShadeNode: ViewShadeNode_
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
	def header_text(self) -> None:
		...
	def info_text(self) -> None:
		...
	def AddControlPage(self, name: str, tags: TagList_) -> int:
		...
	def _AddInput(self, name: str, id: str, tags: TagList_) -> Input_:
		...

ScriptViewShader = ScriptViewShader_