class FusionUI:

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
	def AskQuit(self) -> None:
		"""
		Quit Fusion
		"""
		...

	def CustomizeHotkeys(self) -> None:
		...

	def CustomizeToolbars(self) -> None:
		...

	def GetActiveFrameIndex(self) -> None:
		...

	def GetActiveWndIndex(self) -> None:
		...

	def GetFrameNameIndex(self) -> None:
		...

	def GetModifiers(self) -> None:
		...

	def GetMouseButtons(self) -> None:
		...

	def GetUILayout(self) -> None:
		...

	def GetWndNameIndex(self) -> None:
		...

	def IsConsoleShowing(self) -> None:
		...

	def IsUIVisible(self) -> None:
		...

	def NewScript(self) -> None:
		"""
		New Script
		"""
		...

	def RequestDir(self) -> None:
		...

	def RequestFile(self) -> None:
		...

	def SetActiveFrameIndex(self) -> None:
		...

	def SetActiveWndIndex(self) -> None:
		...

	def SetUILayout(self) -> None:
		...

	def ShowActions(self) -> None:
		...

	def ShowConsole(self) -> None:
		...

	def ShowHelp(self) -> None:
		...

	def ShowMenu(self) -> None:
		...

	def ShowUI(self) -> None:
		...

	def _MasterApp_Active(self) -> None:
		...

	def _Output_Error(self) -> None:
		...

	def _Output_Print(self) -> None:
		...

