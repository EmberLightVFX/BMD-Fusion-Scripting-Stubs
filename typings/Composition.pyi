from typing import Any, overload

from FuFrame import _FuFrame
from Tool import _Tool
from object import _object


class _Composition:

	#---Properties---#
	AutoPos: bool
	"""
	Read/Write
	"""
	UpdateMode: Any
	"""
	Read/Write
	"""
	YPos: int
	"""
	Read/Write
	"""
	XPos: int
	"""
	Read/Write
	"""
	CurrentFrame: _FuFrame
	"""
	Represents the currently active frame for this composition

	Read Only
	"""
	CurrentTime: int
	"""
	The current time position for this composition

	Read/Write
	"""
	ActiveTool: _Tool
	"""
	Represents the currently active tool on this comp

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
	def AbortRender(self):
		...
	def Heartbeat(self):
		...
	def NetRenderAbort(self):
		...
	def GetNextKeyTime(self, time: int = int(), tool: _Tool = _Tool()) -> int:
		"""
		Gets the next key time

		Returns: The timestamp of the keyframe after the given time
			for the specified tool, or for any tool, if none is specified.
			If no time is given, the first keyframe time is returned.
		"""
		...
	def NetRenderEnd(self):
		...
	def GetPrevKeyTime(self, time: int = int(), tool: _Tool = _Tool()) -> int:
		"""
		Gets the previous key time

		Returns: The timestamp of the keyframe before the given time
			for the specified tool, or for any tool, if none is specified.
			If no time is given, the last keyframe time is returned.
		"""
		...
	def DisableSelectedTools(self) -> None:
		"""
		Pass-through the selected tools
		"""
		...
	@overload
	def CopySettings(self) -> dict[Any, Any]:
		"""
		Copy a list of tools to a settings table

		Can be passed a single tool or a table of tools.
		If no args are given, the currently selected tools will be copied.
		"""
		...
	@overload
	def CopySettings(self, tool: _Tool) -> dict[Any, Any]:
		"""
		Copy a list of tools to a settings table

		Can be passed a single tool or a table of tools.
		If no args are given, the currently selected tools will be copied.
		"""
		...
	@overload
	def CopySettings(self, toollist: dict[Any, Any]) -> dict[Any, Any]:
		"""
		Copy a list of tools to a settings table

		Can be passed a single tool or a table of tools.
		If no args are given, the currently selected tools will be copied.
		"""
		...
	def SaveCopyAs(self) -> None:
		"""
		Save a copy of the composition
		"""
		...
	def _SaveCopyAs(self) -> None:
		"""
		Save a copy of the composition
		"""
		...
	def SaveAs(self) -> None:
		"""
		Save the composition
		"""
		...
	@overload
	def Copy(self) -> bool:
		"""
		Copy a list of tools to the Clipboard

		Can be passed a single tool or a table of tools.
		If no args are given, the currently selected tools will be copied.
		"""
		...
	@overload
	def Copy(self, tool: _Tool) -> bool:
		"""
		Copy a list of tools to the Clipboard

		Can be passed a single tool or a table of tools.
		If no args are given, the currently selected tools will be copied.
		"""
		...
	@overload
	def Copy(self, toollist: dict[Any, Any]) -> bool:
		"""
		Copy a list of tools to the Clipboard

		Can be passed a single tool or a table of tools.
		If no args are given, the currently selected tools will be copied.
		"""
		...
	def _Save(self):
		...
	def IsReadOnly(self):
		...
	def SetActiveTool(self, tool: _Tool) -> None:
		"""
		Set the currently active tool
		"""
		...
	def _SetCurrentTime(self):
		...
	def FindTool(self, name: str) -> _Tool:
		"""
		Finds first tool by name
		"""
		...
	def FindToolByID(self, id: str, prev: _Tool = _Tool()) -> _Tool:
		"""
		Finds tools of a given type

		Args:		id	 - string type of tool
						 prev - optional tool to start search from
		"""
		...
	def AddTool(self, id: str, defsettings: bool = bool(), xpos: int = int(), ypos: int = int()) -> _Tool:
		"""
		Adds a tool to the comp at a given position

		Args:		id					- string type of tool to be created
						 defsettings - boolean to use saved default settings
						 xpos, ypos	- integer position on flow view
		"""
		...
	def AddSettingAction(self, filename: str, xpos: int = int(), ypos: int = int()) -> _Tool:
		"""
		Adds a .settings to the comp
		"""
		...
	def AddToolAction(self, id: str, xpos: int = int(), ypos: int = int()) -> _Tool:
		"""
		Adds a tool to the comp
		"""
		...
	def SetData(self, name: str, value: int | str | bool | dict[Any, Any]) -> None:
		"""
		Set custom persistent data
		"""
		...
	def Close(self) -> None:
		"""
		Close the composition
		"""
		...
	def _SaveAs(self) -> None:
		"""
		Save the composition
		"""
		...
	def Lock(self) -> None:
		"""
		Lock the composition from updating
		"""
		...
	def Paste(self, settings: dict[Any, Any] = dict[Any, Any]()) -> bool:
		"""
		Paste tools from the Clipboard

		'settings' may contain the results of Copy() or Operator:SaveSettings()
		If no args are given, the Clipboard will be pasted.
		"""
		...
	def ExpandZone(self):
		...
	def Unlock(self) -> None:
		"""
		Unlock the composition
		"""
		...
	def header_text(self):
		...
	def MapPath(self, path: str) -> str:
		"""
		Expands path mappings in a path string

		Returns the path string with all mappings expanded. Only the first path of a multipath is returned.
		"""
		...
	def IsRendering(self) -> bool:
		...
	def StartUndo(self, name: str) -> None:
		"""
		Start an undo event
		"""
		...
	def EndUndo(self, keep: bool) -> None:
		"""
		End an undo event
		"""
		...
	def SetReadOnly(self):
		...
	def SaveVersion(self, filename: str, version: int = int()) -> bool:
		"""
		Save the composition
		"""
		...
	def Save(self, filename: str) -> bool:
		"""
		Save the composition
		"""
		...
	def NetRenderStart(self):
		...
	def ReverseMapPath(self, mapped: str) -> str:
		"""
		Collapses a path into best-matching path map

		Returns the path string relative to nearest applicable mapped path.
		"""
		...
	def Export(self, filename: str) -> bool:
		"""
		Exports the current composition to a file.

		This saves the composition to an external .comp file, translating as required.
		"""
		...
	def AddMedia(self):
		...
	def Reset(self):
		...
	def GetViewList(self):
		...
	def IsZoneExpanded(self):
		...
	def GetToolList(self, selected: bool = bool(), regid: str = str()) -> dict[Any, Any]:
		"""
		Returns a list of all tools, or selected tools, in the composition

		selected - pass 'true' to get only selected tools
		regid		- pass a Registry ID string to get only tools of that type
		"""
		...
	def IsViewShowing(self):
		...
	def ShowView(self):
		...
	def AskRenderSettings(self):
		...
	def GetPrefs(self, prefname: str = str(), exclude_defaults: bool = bool()) -> dict[Any, Any]:
		"""
		Retrieve a table of preferences
		"""
		...
	def ChooseAction(self, execute: bool, target: _object) -> str:
		"""
		Displays a dialog with a list of selectable actions

		Allows the user to select from a list of actions, and returns the action.
		"""
		...
	def ChooseTool(self, execute: bool) -> tuple[str, str]:
		"""
		Displays a dialog with a list of selectable tools

		Allows the user to select from a list of tools, and returns the tool ID.
		If a macro is selected, the path is also returned.
		"""
		...
	@overload
	def SetPrefs(self, prefname: str, val: int) -> None:
		"""
		Set preferences from a table of attributes
		"""
		...
	@overload
	def SetPrefs(self, prefs: dict[Any, Any]) -> None:
		"""
		Set preferences from a table of attributes
		"""
		...
	def GetCompPathMap(self, built_ins: bool = bool(), defaults: bool = bool()) -> dict[Any, Any]:
		"""
		Returns a table of all Composition path maps

		Args:	built_ins - include built-in path maps (default: true)
					 defaults	- include factory default path maps (default: true)
		Returns: Table of path strings, keyed by map name.
		"""
		...
	def MapPathSegments(self, path: str) -> dict[Any, Any]:
		"""
		Expands all path mappings in a multipath

		Returns a table of path strings with all mappings expanded. All paths of a multipath are returned.
		"""
		...
	def GetConsoleHistory(self):
		...
	def Execute(self):
		...
	def UpdateViews(self):
		...
	def GetFrameList(self):
		...
	def Print(self):
		...
	@overload
	def Loop(self, enable: bool) -> None:
		"""
		Enables looping interactive playback

		where "mode" is one of the following:
			 "none"
			 "loop"
			 "pingpong"
		"""
		...
	@overload
	def Loop(self, mode: str) -> None:
		"""
		Enables looping interactive playback

		where "mode" is one of the following:
			 "none"
			 "loop"
			 "pingpong"
		"""
		...
	def Stop(self) -> None:
		"""
		Stops interactive playback
		"""
		...
	def IsPlaying(self) -> bool:
		...
	def Play(self, reverse: bool = bool()) -> None:
		"""
		Starts interactive playback
		"""
		...
	def GetData(self, name: str = str()) -> int | str | bool | dict[Any, Any]:
		"""
		Get custom persistent data
		"""
		...
	def AskUser(self, title: str, controls: dict[Any, Any]) -> dict[Any, Any]:
		"""
		Present a custom dialog to the user, and return selected values

		Returns a table of result values, determined by individual control types
		"""
		...
	def RunScript(self, filename: str) -> None:
		"""
		Run a script
		"""
		...
	def _Output_Error(self):
		...
	def _Output_Print(self):
		...
	def GetPreviewList(self, include_globals: bool = bool()) -> dict[Any, Any]:
		"""
		Retrieves a table of previews
		"""
		...
	def NetRenderTime(self):
		...
	def ClearUndo(self) -> None:
		"""
		Clears the Undo/Redo history
		"""
		...
	def Redo(self, count: int) -> None:
		"""
		Redo one or more changes to the composition
		"""
		...
	def Undo(self, count: int) -> None:
		"""
		Undo one or more changes to the composition
		"""
		...
	def GetRedoStack(self):
		...
	def GetUndoStack(self):
		...
	def IsLocked(self) -> bool:
		...
	@overload
	def Render(self, wait: bool = bool(), start: int = int(), end: int = int(), proxy: int = int(), hiq: bool = bool(), motionblur: bool = bool()) -> bool:
		"""
		Start a render
		"""
		...
	@overload
	def Render(self, settings: dict[Any, Any]) -> bool:
		"""
		Start a render
		"""
		...
	def AbortRenderUI(self):
		...

Composition = _Composition