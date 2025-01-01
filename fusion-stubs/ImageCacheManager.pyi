class ImageCacheManager:

	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def FreeSpace(self, size: int) -> bool:
		...

	def GetSize(self) -> int:
		...

	def IsRoom(self, size: int) -> bool:
		...

	def Purge(self) -> None:
		...

