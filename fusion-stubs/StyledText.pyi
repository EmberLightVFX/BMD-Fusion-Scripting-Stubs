class StyledText:

	#---Properties---#
	Value: str
	"""
	Read Only
	"""


	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGS_FileName: str

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGB_Utility_Toggle: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def __new(self, val: str) -> StyledText:
		"""
		StyledText constructor

		Args:
			val (str)

		Returns:
			StyledText
		"""
		...

