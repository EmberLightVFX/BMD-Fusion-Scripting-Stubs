class IOClass_:

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
	def GetFileSize(self) -> None:
		...
	def Close(self) -> None:
		...
	def WriteLine(self) -> None:
		...
	def Seek(self) -> None:
		...
	def GetFilePos(self) -> None:
		...
	def Flush(self) -> None:
		...
	def header_text(self) -> None:
		...
	def ReadLine(self) -> None:
		...
	def Write(self) -> None:
		...
	def Read(self) -> None:
		...

IOClass = IOClass_