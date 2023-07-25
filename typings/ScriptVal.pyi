from ScriptVal import _ScriptVal
from ScriptValType import _ScriptValType


class _ScriptVal:

	#---Properties---#
	TypeNamePtr: str
	"""
	Read Only
	"""
	TypeName: str
	"""
	Read Only
	"""

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
	def _newDef(self) -> _ScriptVal:
		...
	def Type(self) -> _ScriptValType:
		...
	def info_text(self):
		...
	def _newScriptVal(self, sv: _ScriptVal) -> _ScriptVal:
		...
	def header_text(self):
		...

ScriptVal = _ScriptVal