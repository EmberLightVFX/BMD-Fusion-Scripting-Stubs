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
	def GetFileSize(self):
		...
	def Close(self):
		...
	def WriteLine(self):
		...
	def Seek(self):
		...
	def GetFilePos(self):
		...
	def Flush(self):
		...
	def header_text(self):
		...
	def ReadLine(self):
		...
	def Write(self):
		...
	def Read(self):
		...

IOClass = IOClass_