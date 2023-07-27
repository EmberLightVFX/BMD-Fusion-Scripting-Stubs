from _non_existing import ScriptValType_


class ScriptVal_:

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
	def _newDef(self) -> ScriptVal_:
		...
	def info_text(self):
		...
	def _newScriptVal(self, sv: ScriptVal_) -> ScriptVal_:
		...
	def header_text(self):
		...
	def Type(self) -> ScriptValType_:
		...

ScriptVal = ScriptVal_