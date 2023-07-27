class FusionUI_:

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
	def SetActiveWndIndex(self) -> None:
		...
	def SetActiveFrameIndex(self) -> None:
		...
	def RequestDir(self) -> None:
		...
	def AskQuit(self) -> None:
		"""
		Quit Fusion
		"""
		...
	def ShowHelp(self) -> None:
		...
	def CustomizeHotkeys(self) -> None:
		...
	def GetWndNameIndex(self) -> None:
		...
	def GetFrameNameIndex(self) -> None:
		...
	def GetMouseButtons(self) -> None:
		...
	def GetModifiers(self) -> None:
		...
	def header_text(self) -> None:
		...
	def _Output_Print(self) -> None:
		...
	def _Output_Error(self) -> None:
		...
	def _MasterApp_Active(self) -> None:
		...
	def ShowUI(self) -> None:
		...
	def ShowMenu(self) -> None:
		...
	def ShowConsole(self) -> None:
		...
	def ShowActions(self) -> None:
		...
	def GetActiveFrameIndex(self) -> None:
		...
	def GetActiveWndIndex(self) -> None:
		...
	def NewScript(self) -> None:
		"""
		New Script
		"""
		...
	def SetUILayout(self) -> None:
		...
	def GetUILayout(self) -> None:
		...
	def IsConsoleShowing(self) -> None:
		...
	def CustomizeToolbars(self) -> None:
		...
	def RequestFile(self) -> None:
		...
	def IsUIVisible(self) -> None:
		...

FusionUI = FusionUI_