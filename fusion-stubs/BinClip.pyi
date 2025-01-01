class BinClip:

	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGS_FileName: str

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGS_UIName: str

	REGB_Unpredictable: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def CreateStamp(self) -> None:
		"""
		Create a stamp for this BinClip
		"""
		...

	def Defragment(self) -> None:
		"""
		Defragment this clip
		"""
		...

	def DeleteStamp(self) -> None:
		"""
		Delete the stamp for this BinClip
		"""
		...

