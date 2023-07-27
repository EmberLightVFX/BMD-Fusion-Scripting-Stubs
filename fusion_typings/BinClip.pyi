class _BinClip:

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
	def header_text(self):
		...
	def DeleteStamp(self) -> None:
		"""
		Delete the stamp for this BinClip
		"""
		...
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

BinClip = _BinClip