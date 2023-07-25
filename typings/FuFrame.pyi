from typing import Any

from Tool import _Tool


class _FuFrame:

	#---Properties---#
	ConsoleView: Any
	"""
	Represents this frame window's console

			The ConsoleView variable represents the FuView object used to displayany scripting message, and to allow script commands to be entered.

	Read Only
	"""
	TransportView: Any
	"""
	Represents this frame window's transport controls view

	Read Only
	"""
	RightView: Any
	"""
	Represents this frame window's right display view

			The RightView variable represents the right-hand GLView object used todisplay images, 3D scenes and other parameters output by a tool.

	Read Only
	"""
	LeftView: Any
	"""
	Represents this frame window's left display view

			The LeftView variable represents the left-hand GLView object used todisplay images, 3D scenes and other parameters output by a tool.

	Read Only
	"""
	SplineView: Any
	"""
	Represents this frame window's spline editor view

	Read Only
	"""
	ModifierView: Any
	"""
	Represents this frame window's Modifier controls view

	Read Only
	"""
	TimeRulerView: Any
	"""
	Represents this frame window's time ruler

	Read Only
	"""
	CurrentView: Any
	"""
	Represents the currently active view for this frame window

			The CurrentView variable represents the currently active view for this frame window.

	Read Only
	"""
	ToolView: Any
	"""
	Represents this frame window's Tool controls view

	Read Only
	"""
	TimelineView: Any
	"""
	Represents this frame window's Timeline view

	Read Only
	"""
	FlowView: Any
	"""
	Represents this frame window's Flow view

			The FlowView variable represents the FuView object used to displaythe various tool connections for the frame's Composition.

	Read Only
	"""
	Composition: Any
	"""
	Represents this frame window's Composition

			The Composition variable represents the Composition object that thisframe window is displaying.

	Read Only
	"""
	InfoView: Any
	"""
	Represents this frame window's Info view

			The InfoView variable represents the FuView object used to displayany general notes for the frame's Composition.

	Read Only
	"""

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
	def SwitchView(self, id: str) -> None:
		"""
		Displays a given view within this frame

		where 'id' is the ID of one of the views in the frame.
		 e.g. 'FlowView', 'ConsoleView', 'TimelineView', 'SplineEditorView'
		"""
		...
	def ViewOn(self, tool: _Tool = _Tool(), view: int = int()) -> None:
		"""
		Displays a tool on a numbered view

		where 'view' is a number from 0..9.
		If 'tool' is omitted, the currently active tool is used.
		If 'tool' is nil, the view is cleared.
		If no arguments are supplied, all views are cleared.
		"""
		...
	def GetViewList(self) -> dict[Any, Any]:
		"""
		Returns the list of views within this frame

		where 'table' is a table of the FuView objects in the frame,
		and entries are named by the view's ID string.
		"""
		...
	def GetPreviewList(self, include_globals: bool = bool()) -> dict[Any, Any]:
		"""
		Retrieves a table of previews
		"""
		...
	def header_text(self):
		...

FuFrame = _FuFrame