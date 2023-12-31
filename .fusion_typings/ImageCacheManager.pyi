class ImageCacheManager_:

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def Purge(self) -> None:
		...
	def FreeSpace(self, size: int) -> bool:
		...
	def header_text(self) -> None:
		...
	def IsRoom(self, size: int) -> bool:
		...
	def GetSize(self) -> int:
		...

ImageCacheManager = ImageCacheManager_