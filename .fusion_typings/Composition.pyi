from typing import Any, overload

from Tool import Tool_
from FuFrame import FuFrame_
from _non_existing import object_


class Composition_:

	#---Properties---#
	ActiveTool: Tool_
	"""
	Represents the currently active tool on this comp

	Read Only
	"""
	AutoPos: bool
	"""
	Read/Write
	"""
	CurrentFrame: FuFrame_
	"""
	Represents the currently active frame for this composition

	Read Only
	"""
	CurrentTime: int
	"""
	The current time position for this composition

	Read/Write
	"""
	TIME_UNDEFINED: int
	"""
	Read Only
	"""
	UpdateMode: Any
	"""
	Read/Write
	"""
	XPos: int
	"""
	Read/Write
	"""
	YPos: int
	"""
	Read/Write
	"""

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
	def AbortRender(self) -> None:
		...
	def AbortRenderUI(self) -> None:
		...
	def AddMedia(self) -> None:
		...
	def AddSettingAction(self, filename: str, xpos: int = int(), ypos: int = int()) -> Tool_:
		"""
		Adds a .settings to the comp
		"""
		...
	def AddTool(self, id: str, defsettings: bool = bool(), xpos: int = int(), ypos: int = int()) -> Tool_:
		"""
		Adds a tool to the comp at a given position

		Args:		id					- string type of tool to be created
						 defsettings - boolean to use saved default settings
						 xpos, ypos	- integer position on flow view
		"""
		...
	def AddToolAction(self, id: str, xpos: int = int(), ypos: int = int()) -> Tool_:
		"""
		Adds a tool to the comp
		"""
		...
	def AskRenderSettings(self) -> None:
		...
	def AskUser(self, title: str, controls: dict[Any, Any]) -> dict[Any, Any]:
		"""
		Present a custom dialog to the user, and return selected values

		Returns a table of result values, determined by individual control types
		"""
		...
	def ChooseAction(self, execute: bool, target: object_) -> str:
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
	def ClearUndo(self) -> None:
		"""
		Clears the Undo/Redo history
		"""
		...
	def Close(self) -> None:
		"""
		Close the composition
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
	def Copy(self, tool: Tool_) -> bool:
		"""
		Copy a list of tools to the Clipboard

		Can be passed a single tool or a table of tools.
		If no args are given, the currently selected tools will be copied.
		"""
		...
	@overload
	def Copy(self, toollist: list[Tool_]) -> bool:
		"""
		Copy a list of tools to the Clipboard

		Can be passed a single tool or a table of tools.
		If no args are given, the currently selected tools will be copied.
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
	def CopySettings(self, tool: Tool_) -> dict[Any, Any]:
		"""
		Copy a list of tools to a settings table

		Can be passed a single tool or a table of tools.
		If no args are given, the currently selected tools will be copied.
		"""
		...
	@overload
	def CopySettings(self, toollist: list[Tool_]) -> dict[Any, Any]:
		"""
		Copy a list of tools to a settings table

		Can be passed a single tool or a table of tools.
		If no args are given, the currently selected tools will be copied.
		"""
		...
	def DisableSelectedTools(self) -> None:
		"""
		Pass-through the selected tools
		"""
		...
	def EndUndo(self, keep: bool) -> None:
		"""
		End an undo event
		"""
		...
	def Execute(self) -> None:
		...
	def ExpandZone(self) -> None:
		...
	def Export(self, filename: str) -> bool:
		"""
		Exports the current composition to a file.

		This saves the composition to an external .comp file, translating as required.
		"""
		...
	def FindTool(self, name: str) -> Tool_:
		"""
		Finds first tool by name
		"""
		...
	def FindToolByID(self, id: str, prev: Tool_ = Tool_()) -> Tool_:
		"""
		Finds tools of a given type

		Args:		id	 - string type of tool
						 prev - optional tool to start search from
		"""
		...
	@overload
	def GetAttrs(self, attribute_name: str) -> int | str | bool | dict[Any, Any] | list[Any]:
		"""
		Returns the content of an attributes

		You can get all attributes by not passing anything
		"""
		...
	@overload
	def GetAttrs(self) -> dict[Any, Any]:
		"""
		Returns the content of an attributes

		You can get all attributes by not passing anything
		"""
		...
	def GetCompPathMap(self, built_ins: bool = bool(), defaults: bool = bool()) -> dict[str, str]:
		"""
		Returns a table of all Composition path maps

		Args:	built_ins - include built-in path maps (default: true)
					 defaults	- include factory default path maps (default: true)
		Returns: Table of path strings, keyed by map name.
		"""
		...
	def GetConsoleHistory(self) -> None:
		...
	def GetData(self, name: str = str()) -> int | str | bool | dict[Any, Any] | list[Any]:
		"""
		Get custom persistent data
		"""
		...
	def GetFrameList(self) -> None:
		...
	def GetNextKeyTime(self, time: int = int(), tool: Tool_ = Tool_()) -> int:
		"""
		Gets the next key time

		Returns: The timestamp of the keyframe after the given time
			for the specified tool, or for any tool, if none is specified.
			If no time is given, the first keyframe time is returned.
		"""
		...
	def GetPrefs(self, prefname: str = str(), exclude_defaults: bool = bool()) -> dict[Any, Any]:
		"""
		Retrieve a table of preferences
		"""
		...
	def GetPrevKeyTime(self, time: int = int(), tool: Tool_ = Tool_()) -> int:
		"""
		Gets the previous key time

		Returns: The timestamp of the keyframe before the given time
			for the specified tool, or for any tool, if none is specified.
			If no time is given, the last keyframe time is returned.
		"""
		...
	def GetPreviewList(self, include_globals: bool = bool()) -> dict[Any, Any]:
		"""
		Retrieves a table of previews
		"""
		...
	def GetRedoStack(self) -> None:
		...
	def GetToolList(self, selected: bool = bool(), regid: str = str()) -> dict[int, Tool_]:
		"""
		Returns a list of all tools, or selected tools, in the composition

		selected - pass 'true' to get only selected tools
		regid		- pass a Registry ID string to get only tools of that type
		"""
		...
	def GetUndoStack(self) -> None:
		...
	def GetViewList(self) -> None:
		...
	def Heartbeat(self) -> None:
		...
	def IsLocked(self) -> bool:
		...
	def IsPlaying(self) -> bool:
		...
	def IsReadOnly(self) -> None:
		...
	def IsRendering(self) -> bool:
		...
	def IsViewShowing(self) -> None:
		...
	def IsZoneExpanded(self) -> None:
		...
	def Lock(self) -> None:
		"""
		Lock the composition from updating
		"""
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
	def MapPath(self, path: str) -> str:
		"""
		Expands path mappings in a path string

		Returns the path string with all mappings expanded. Only the first path of a multipath is returned.
		"""
		...
	def MapPathSegments(self, path: str) -> dict[str, str]:
		"""
		Expands all path mappings in a multipath

		Returns a table of path strings with all mappings expanded. All paths of a multipath are returned.
		"""
		...
	def NetRenderAbort(self) -> None:
		...
	def NetRenderEnd(self) -> None:
		...
	def NetRenderStart(self) -> None:
		...
	def NetRenderTime(self) -> None:
		...
	def Paste(self, settings: dict[Any, Any] = dict[Any, Any]()) -> bool:
		"""
		Paste tools from the Clipboard

		'settings' may contain the results of Copy() or Operator:SaveSettings()
		If no args are given, the Clipboard will be pasted.
		"""
		...
	def Play(self, reverse: bool = bool()) -> None:
		"""
		Starts interactive playback
		"""
		...
	def Print(self) -> None:
		...
	def Redo(self, count: int) -> None:
		"""
		Redo one or more changes to the composition
		"""
		...
	@overload
	def Render(self, wait: bool = bool(), start: int = int(), end: int = int(), proxy: int = int(), hiq: bool = bool(), motionblur: bool = bool()) -> bool:
		"""
		Start a render
		"""
		...
	@overload
	def Render(self, settings: dict[Any, Any] = dict[Any, Any]()) -> bool:
		"""
		Start a render
		"""
		...
	def Reset(self) -> None:
		...
	def ReverseMapPath(self, mapped: str) -> str:
		"""
		Collapses a path into best-matching path map

		Returns the path string relative to nearest applicable mapped path.
		"""
		...
	def RunScript(self, filename: str) -> None:
		"""
		Run a script
		"""
		...
	def Save(self, filename: str) -> bool:
		"""
		Save the composition
		"""
		...
	def SaveAs(self) -> None:
		"""
		Save the composition
		"""
		...
	def SaveCopyAs(self) -> None:
		"""
		Save a copy of the composition
		"""
		...
	def SaveVersion(self, filename: str, version: int = int()) -> bool:
		"""
		Save the composition
		"""
		...
	def SetActiveTool(self, tool: Tool_ = Tool_()) -> None:
		"""
		Set the currently active tool
		"""
		...
	def SetAttrs(self, attributes: dict[Any, Any]) -> None:
		"""
		Set the content of an attributes
		"""
		...
	def SetData(self, name: str, value: int | str | bool | dict[Any, Any] | list[Any]) -> None:
		"""
		Set custom persistent data
		"""
		...
	@overload
	def SetPrefs(self, prefname: str, val: float) -> None:
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
	def SetReadOnly(self) -> None:
		...
	def ShowView(self) -> None:
		...
	def StartUndo(self, name: str) -> None:
		"""
		Start an undo event
		"""
		...
	def Stop(self) -> None:
		"""
		Stops interactive playback
		"""
		...
	def Undo(self, count: int) -> None:
		"""
		Undo one or more changes to the composition
		"""
		...
	def Unlock(self) -> None:
		"""
		Unlock the composition
		"""
		...
	def UpdateViews(self) -> None:
		...
	def _Output_Error(self) -> None:
		...
	def _Output_Print(self) -> None:
		...
	def _Save(self) -> None:
		...
	def _SaveAs(self) -> None:
		"""
		Save the composition
		"""
		...
	def _SaveCopyAs(self) -> None:
		"""
		Save a copy of the composition
		"""
		...
	def _SetCurrentTime(self) -> None:
		...
	def header_text(self) -> None:
		...

Composition = Composition_