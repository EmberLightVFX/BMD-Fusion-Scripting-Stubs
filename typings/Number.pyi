from Number Numberfloat64 val import _Number Numberfloat64 val


class _Number:

	#---Properties---#
	Value: float
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
	def info_text(self):
		...
	def Number(self) -> _Number Numberfloat64 val:
		"""
		Number constructor
		"""
		...
	def header_text(self):
		...

Number = _Number