from typing import Literal

from _non_existing import _ScriptValType


class _ScriptVal:

	#---Properties---#
	TypeName: str
	"""
	Read Only
	"""
	TypeNamePtr: str
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

	REGB_Utility_Toggle: bool

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def _newDef(self) -> _ScriptVal:
		...
	def info_text(self):
		...
	def _newScriptVal(self, sv: _ScriptVal) -> _ScriptVal:
		...
	def header_text(self):
		...
	def Type(self) -> _ScriptValType:
		...

ScriptVal = _ScriptVal