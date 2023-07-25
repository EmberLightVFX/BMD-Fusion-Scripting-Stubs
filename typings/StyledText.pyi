from StyledText StyledTextstring val import _StyledText StyledTextstring val


class _StyledText:

	#---Properties---#
	Value: str
	"""
	Read Only
	"""

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGS_VersionString: str

	REGB_ControlView: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_FileName: str

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGB_Unpredictable: bool


	#---Methods---#
	def info_text(self):
		...
	def StyledText(self) -> _StyledText StyledTextstring val:
		"""
		StyledText constructor
		"""
		...
	def header_text(self):
		...

StyledText = _StyledText