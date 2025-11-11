from typing import Any, overload

from _non_existing import time
from FuFrame import FuFrame
from Tool import Tool

class Composition:

    #---Properties---#
    ActiveTool: Tool
    """
    Represents the currently active tool on this comp

    Read Only
    """

    AutoPos: bool

    CurrentFrame: FuFrame
    """
    Represents the currently active frame for this composition

    Read Only
    """

    CurrentTime: int
    """
    The current time position for this composition

    """

    UpdateMode: Any

    XPos: int

    YPos: int

    TIME_UNDEFINED: float
    """
    Read Only
    """


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
    def AbortRender(self) -> None:
        ...

    def AbortRenderUI(self) -> None:
        ...

    def AddMedia(self) -> None:
        ...

    def AddSettingAction(self, filename: str, xpos: int | None = None, ypos: int | None = None) -> Tool:
        """
        Adds a .settings to the comp

        Args:
            filename (str)
            xpos (Optional[int])
            ypos (Optional[int])

        Returns:
            tool (Tool)
        """
        ...

    def AddTool(self, id: str, defsettings: bool | None = None, xpos: int | None = None, ypos: int | None = None) -> Tool:
        """
        Adds a tool to the comp at a given position

        Args:    id          - string type of tool to be created
        defsettings - boolean to use saved default settings
        xpos, ypos  - integer position on flow view

        Args:
            id (str)
            defsettings (Optional[bool])
            xpos (Optional[int])
            ypos (Optional[int])

        Returns:
            tool (Tool)
        """
        ...

    def AddToolAction(self, id: str, xpos: int | None = None, ypos: int | None = None) -> Tool:
        """
        Adds a tool to the comp

        Args:
            id (str)
            xpos (Optional[int])
            ypos (Optional[int])

        Returns:
            tool (Tool)
        """
        ...

    def AskRenderSettings(self) -> None:
        ...

    def AskUser(self, title: str, controls: dict[Any, Any]) -> dict[Any, Any]:
        """
        Present a custom dialog to the user, and return selected values

        Returns a table of result values, determined by individual control types

        Args:
            title (str)
            controls (dict[Any, Any])

        Returns:
            results (dict[Any, Any])
        """
        ...

    def ChooseAction(self, execute: bool, target: object) -> str:
        """
        Displays a dialog with a list of selectable actions

        Allows the user to select from a list of actions, and returns the action.

        Args:
            execute (bool)
            target (object)

        Returns:
            ID (str)
        """
        ...

    def ChooseTool(self, execute: bool) -> str | tuple[str, str]:
        """
        Displays a dialog with a list of selectable tools

        Allows the user to select from a list of tools, and returns the tool ID.
        If a macro is selected, the path is also returned.

        Args:
            execute (bool)

        Returns:
            ID (str)
            path (str)
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

        Returns:
            success (bool)
        """
        ...

    @overload
    def Copy(self, tool: Tool) -> bool:
        """
        Copy a list of tools to the Clipboard

        Can be passed a single tool or a table of tools.
        If no args are given, the currently selected tools will be copied.

        Args:
            tool (Tool)

        Returns:
            success (bool)
        """
        ...

    @overload
    def Copy(self, toollist: list[Tool]) -> bool:
        """
        Copy a list of tools to the Clipboard

        Can be passed a single tool or a table of tools.
        If no args are given, the currently selected tools will be copied.

        Args:
            toollist (list[Tool])

        Returns:
            success (bool)
        """
        ...

    @overload
    def CopySettings(self) -> dict[Any, Any]:
        """
        Copy a list of tools to a settings table

        Can be passed a single tool or a table of tools.
        If no args are given, the currently selected tools will be copied.

        Returns:
            settings (dict[Any, Any])
        """
        ...

    @overload
    def CopySettings(self, tool: Tool) -> dict[Any, Any]:
        """
        Copy a list of tools to a settings table

        Can be passed a single tool or a table of tools.
        If no args are given, the currently selected tools will be copied.

        Args:
            tool (Tool)

        Returns:
            settings (dict[Any, Any])
        """
        ...

    @overload
    def CopySettings(self, toollist: list[Tool]) -> dict[Any, Any]:
        """
        Copy a list of tools to a settings table

        Can be passed a single tool or a table of tools.
        If no args are given, the currently selected tools will be copied.

        Args:
            toollist (list[Tool])

        Returns:
            settings (dict[Any, Any])
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

        Args:
            keep (bool)
        """
        ...

    def Execute(self, script_text: str) -> None:
        """
        Executes a script string

        Args:
            script text (str)
        """
        ...

    def ExecuteFile(self, filename: str, args: dict[Any, Any]) -> None:
        """
        Executes a script file internally

        Args:
            filename (str)
            args (dict[Any, Any])
        """
        ...

    def ExpandZone(self) -> None:
        ...

    def Export(self, filename: str) -> bool:
        """
        Exports the current composition to a file.

        This saves the composition to an external .comp file, translating as required.

        Args:
            filename (str)

        Returns:
            success (bool)
        """
        ...

    def FindTool(self, name: str) -> Tool:
        """
        Finds first tool by name

        Args:
            name (str)

        Returns:
            tool (Tool)
        """
        ...

    def FindToolByID(self, id: str, prev: Tool | None = None) -> Tool:
        """
        Finds tools of a given type

        Args:    id   - string type of tool
        prev - optional tool to start search from

        Args:
            id (str)
            prev (Optional[Tool])

        Returns:
            tool (Tool)
        """
        ...

    def GetCompPathMap(self, built_ins: bool | None = None, defaults: bool | None = None) -> dict[str, str]:
        """
        Returns a table of all Composition path maps

        Args:  built_ins - include built-in path maps (default: true)
        defaults  - include factory default path maps (default: true)
        Returns: Table of path strings, keyed by map name.

        Args:
            built_ins (Optional[bool])
            defaults (Optional[bool])

        Returns:
            map (dict[str, str])
        """
        ...

    def GetConsoleHistory(self) -> None:
        ...

    def GetData(self, name: str | None = None) -> (int|str|bool|dict[Any, Any]):
        """
        Get custom persistent data

        Args:
            name (Optional[str])

        Returns:
            value ((number_or_string_or_boolean_or_table))
        """
        ...

    def GetFrameList(self) -> None:
        ...

    def GetMarkers(self, timestamp: time | None = None) -> list:
        """
        Returns a table of timeline markers.

        This returns a list of timeline markers, each with a table/dict of attributes.

        Args:
            timestamp (Optional[time])

        Returns:
            marker data (list)
        """
        ...

    def GetNextKeyTime(self, time: int | None = None, tool: Tool | None = None) -> int:
        """
        Gets the next key time

        Returns: The timestamp of the keyframe after the given time
        for the specified tool, or for any tool, if none is specified.
        If no time is given, the first keyframe time is returned.

        Args:
            time (Optional[int])
            tool (Optional[Tool])

        Returns:
            time (int)
        """
        ...

    def GetPrefs(self, prefname: str | None = None, exclude_defaults: bool | None = None) -> dict[Any, Any]:
        """
        Retrieve a table of preferences

        Args:
            prefname (Optional[str])
            exclude-defaults (Optional[bool])

        Returns:
            prefs (dict[Any, Any])
        """
        ...

    def GetPrevKeyTime(self, time: int | None = None, tool: Tool | None = None) -> int:
        """
        Gets the previous key time

        Returns: The timestamp of the keyframe before the given time
        for the specified tool, or for any tool, if none is specified.
        If no time is given, the last keyframe time is returned.

        Args:
            time (Optional[int])
            tool (Optional[Tool])

        Returns:
            time (int)
        """
        ...

    def GetPreviewList(self, include_globals: bool | None = None) -> dict[Any, Any]:
        """
        Retrieves a table of previews

        Args:
            include_globals (Optional[bool])

        Returns:
            previews (dict[Any, Any])
        """
        ...

    def GetRedoStack(self) -> None:
        ...

    def GetToolList(self, selected: bool | None = None, regid: str | None = None) -> dict[int, Tool]:
        """
        Returns a list of all tools, or selected tools, in the composition

        selected - pass 'true' to get only selected tools
        regid    - pass a Registry ID string to get only tools of that type

        Args:
            selected (Optional[bool])
            regid (Optional[str])

        Returns:
            tools (dict[int, Tool])
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

        Args:
            enable (bool)
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

        Args:
            mode (str)
        """
        ...

    def MapPath(self, path: str) -> str:
        """
        Expands path mappings in a path string

        Returns the path string with all mappings expanded. Only the first path of a multipath is returned.

        Args:
            path (str)

        Returns:
            mapped (str)
        """
        ...

    def MapPathSegments(self, path: str) -> dict[str, str]:
        """
        Expands all path mappings in a multipath

        Returns a table of path strings with all mappings expanded. All paths of a multipath are returned.

        Args:
            path (str)

        Returns:
            mapped (dict[str, str])
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

    def Paste(self, settings: dict[Any, Any] | None = None) -> bool:
        """
        Paste tools from the Clipboard

        'settings' may contain the results of Copy() or Operator:SaveSettings()
        If no args are given, the Clipboard will be pasted.

        Args:
            settings (Optional[dict[Any, Any]])

        Returns:
            success (bool)
        """
        ...

    def Play(self, reverse: bool | None = None) -> None:
        """
        Starts interactive playback

        Args:
            reverse (Optional[bool])
        """
        ...

    def Print(self) -> None:
        ...

    def Redo(self, count: int) -> None:
        """
        Redo one or more changes to the composition

        Args:
            count (int)
        """
        ...

    @overload
    def Render(self, wait: bool | None = None, start: int | None = None, end: int | None = None, proxy: int | None = None, hiq: bool | None = None, motionblur: bool | None = None) -> bool:
        """
        Start a render

        Args:
            wait (Optional[bool])
            start (Optional[int])
            end (Optional[int])
            proxy (Optional[int])
            hiq (Optional[bool])
            motionblur (Optional[bool])

        Returns:
            success (bool)
        """
        ...

    @overload
    def Render(self, settings: dict[Any, Any] | None = None) -> bool:
        """
        Start a render

        Args:
            settings (dict[Any, Any] | None = None)

        Returns:
            success (bool)
        """
        ...

    def Reset(self) -> None:
        ...

    def ReverseMapPath(self, mapped: str) -> str:
        """
        Collapses a path into best-matching path map

        Returns the path string relative to nearest applicable mapped path.

        Args:
            mapped (str)

        Returns:
            path (str)
        """
        ...

    def RunScript(self, filename: str) -> None:
        """
        Run a script file externally

        Args:
            filename (str)
        """
        ...

    def Save(self, filename: str) -> bool:
        """
        Save the composition

        Args:
            filename (str)

        Returns:
            success (bool)
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

    def SaveVersion(self, filename: str, version: int | None = None) -> bool:
        """
        Save the composition

        Args:
            filename (str)
            version (Optional[int])

        Returns:
            success (bool)
        """
        ...

    def SetActiveTool(self, tool: Tool = Tool()) -> None:
        """
        Set the currently active tool

        Args:
            tool (Tool = Tool())
        """
        ...

    def SetData(self, name: str, value: int | str | bool | dict[Any, Any]) -> None:
        """
        Set custom persistent data

        Args:
            name (str)
            value ((number_or_string_or_boolean_or_table))
        """
        ...

    def SetMarker(self, timestamp: int, marker_data: dict[Any, Any]) -> None:
        """
        Creates or changes a timeline marker.

        This will add or overwrite a timeline marker. Pass a table/dict of attributes, or nil to delete the marker.

        Args:
            timestamp (int)
            marker data (dict[Any, Any])
        """
        ...

    @overload
    def SetPrefs(self, prefname: str, val: float) -> None:
        """
        Set preferences from a table of attributes

        Args:
            prefname (str)
            val (float)
        """
        ...

    @overload
    def SetPrefs(self, prefs: dict[Any, Any]) -> None:
        """
        Set preferences from a table of attributes

        Args:
            prefs (dict[Any, Any])
        """
        ...

    def SetReadOnly(self) -> None:
        ...

    def ShowView(self) -> None:
        ...

    def StartUndo(self, name: str) -> None:
        """
        Start an undo event

        Args:
            name (str)
        """
        ...

    def Stop(self) -> None:
        """
        Stops interactive playback
        """
        ...

    def Transcribe(self, media_ID: str, detect_speaker: bool | None = None) -> dict[Any, Any]:
        """
        Fetches transcription data for given media.

        Resolve: This takes a media ID string, performs transcription on the media, then returns a table of text and timing.

        Args:
            media ID (str)
            detect speaker (Optional[bool])

        Returns:
            data (dict[Any, Any])
        """
        ...

    def Undo(self, count: int) -> None:
        """
        Undo one or more changes to the composition

        Args:
            count (int)
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

    @overload
    def GetAttrs(self, attribute_name: str) -> (int|str|bool|dict[Any, Any]):
        """
        Returns the content of an attributes

        You can get all attributes by not passing anything

        Args:
            attribute_name (str)

        Returns:
            attribute_value (number_or_string_or_boolean_or_table)
        """
        ...

    @overload
    def GetAttrs(self) -> dict[Any, Any]:
        """
        Returns the content of an attributes

        You can get all attributes by not passing anything

        Returns:
            all_attributes (dict[Any, Any])
        """
        ...

    def SetAttrs(self, attributes: dict[Any, Any]) -> None:
        """
        Set the content of an attributes

        Args:
            attributes (dict[Any, Any])
        """
        ...

