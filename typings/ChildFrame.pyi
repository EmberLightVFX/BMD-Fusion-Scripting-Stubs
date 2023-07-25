from typing import Any

class _ChildFrame:

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
	def LoadLayout(self) -> None:
		...
	def ActivatePrevFrame(self) -> None:
		"""
		Activates the previous frame window
		"""
		...
	def ActivateNextFrame(self) -> None:
		"""
		Activates the next frame window
		"""
		...
	def ActivateFrame(self) -> None:
		"""
		Activates this frame window
		"""
		...
	def SetViewLayout(self, layout: dict[Any, Any]) -> bool:
		"""
		Sets the current view layout from a table

		Args:	table describing the view layout
		"""
		...
	def GetViewLayout(self) -> dict[Any, Any]:
		"""
		Retrieves the current view layout

		Returns a table describing the current view layout
		"""
		...
	def SwitchLayout(self):
		...
	def GetControlViewList(self) -> dict[Any, Any]:
		"""
		Returns the list of views from the Controls tabs

		where 'table' is a table of the FuView objects in the Controls view tabs,and entries are named by the view's ID string.
		"""
		...
	def SwitchMainView(self, id: str) -> None:
		"""
		Displays a given view from the Main tabs

		where 'id' is the ID of one of the views in the Main tab list.
		e.g. 'FlowView', 'ConsoleView', 'TimelineView', 'SplineEditorView'
		"""
		...
	def SwitchControlView(self, id: str) -> None:
		"""
		Displays a given view from the Control tabs

		where 'id' is the ID of one of the views in the Controls tab list.
		e.g. 'ControlView', 'ModifierView'
		"""
		...
	def header_text(self):
		...
	def SaveLayout(self) -> None:
		...
	def SetScreenLayout(self):
		...
	def ResetLayout(self) -> None:
		...
	def GetMainViewList(self) -> dict[Any, Any]:
		"""
		Returns the list of views from the Main tabs

		where 'views' is a table of the FuView objects in the Main view tabs,and entries are named by the view's ID string.
		"""
		...

ChildFrame = _ChildFrame