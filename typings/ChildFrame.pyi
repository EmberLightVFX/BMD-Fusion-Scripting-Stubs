from typing import Any

class _ChildFrame:

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
	def ActivateNextFrame(self) -> None:
		"""
		Activates the next frame window
		"""
		...
	def SwitchControlView(self, id: str) -> None:
		"""
		Displays a given view from the Control tabs

		where 'id' is the ID of one of the views in the Controls tab list.
		e.g. 'ControlView', 'ModifierView'
		"""
		...
	def SetScreenLayout(self):
		...
	def GetMainViewList(self) -> dict[Any, Any]:
		"""
		Returns the list of views from the Main tabs

		where 'views' is a table of the FuView objects in the Main view tabs,and entries are named by the view's ID string.
		"""
		...
	def ResetLayout(self) -> None:
		...
	def SaveLayout(self) -> None:
		...
	def LoadLayout(self) -> None:
		...
	def ActivatePrevFrame(self) -> None:
		"""
		Activates the previous frame window
		"""
		...
	def header_text(self):
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

ChildFrame = _ChildFrame