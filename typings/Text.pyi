from Text Textstring val import _Text Textstring val


class _Text:

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

	REGI_ClassType: int

	REGI_Priority: int

	REGB_ControlView: bool

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGB_Unpredictable: bool


	#---Methods---#
	def info_text(self):
		...
	def Text(self) -> _Text Textstring val:
		"""
		Text constructor
		"""
		...
	def header_text(self):
		...

Text = _Text