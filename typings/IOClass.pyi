class _IOClass:

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_VersionString: str

	REGS_ID: str

	REGB_ControlView: bool

	REGI_Priority: int


	#---Methods---#
	def Seek(self):
		...
	def Close(self):
		...
	def Flush(self):
		...
	def WriteLine(self):
		...
	def ReadLine(self):
		...
	def Write(self):
		...
	def Read(self):
		...
	def header_text(self):
		...
	def GetFilePos(self):
		...
	def GetFileSize(self):
		...

IOClass = _IOClass