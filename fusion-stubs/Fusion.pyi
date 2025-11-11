from typing import Any, overload

from _non_existing import Bins, CacheManager, File, MenuManager
from ActionManager import ActionManager
from Composition import Composition
from FontList import FontList
from HotkeyManager import HotkeyManager
from MailMessage import MailMessage
from MemBlock import MemBlock
from QueueManager import QueueManager
from Registry import Registry
from RenderJob import RenderJob
from UIManager import UIManager

class Fusion:

    #---Properties---#
    ActionManager: ActionManager
    """
    The Global Action Manager

    Read Only
    """

    BinManager: Bins
    """
    Bins

    Read Only
    """

    Bins: Bins
    """
    Bins

    Read Only
    """

    Build: int
    """
    The build number of Fusion.

    Read Only
    """

    CacheManager: CacheManager
    """
    The Global Cache Manager

    Read Only
    """

    CurrentComp: Composition
    """
    Represents the currently active composition

    The CurrentComp variable represents the currently active composition within Fusion.

    Read Only
    """

    CurrentFrame: Any

    FileLogging: Any

    FontManager: FontList
    """
    The Global Font Manager

    Read Only
    """

    HotkeyManager: HotkeyManager
    """
    The Global Hotkey Manager

    Read Only
    """

    MenuManager: MenuManager
    """
    The Global Menu Manager

    Read Only
    """

    MouseX: Any

    MouseY: Any

    QueueManager: QueueManager
    """
    The global render manager for this instance of Fusion

    Read Only
    """

    RenderManager: QueueManager
    """
    The global render manager for this instance of Fusion

    Read Only
    """

    UIManager: UIManager
    """
    Read Only
    """

    Version: int
    """
    The version number of Fusion.

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
    def AddConfig(self) -> None:
        ...

    def AllowNetwork(self) -> None:
        ...

    def ClearFileLog(self) -> None:
        ...

    def ClearRecentCompList(self) -> None:
        ...

    def Copy(self) -> None:
        ...

    def CreateFloatingView(self) -> None:
        ...

    def CreateMail(self) -> MailMessage:
        """
        Create an empty Mail message object

        Returns:
            mail (MailMessage)
        """
        ...

    def CustomizeToolbars(self) -> None:
        ...

    def Cut(self) -> None:
        ...

    def DeactivateLicense(self) -> None:
        """
        Deactivate Fusion Studio on this machine
        """
        ...

    def Delete(self) -> None:
        ...

    def DeselectAll(self) -> None:
        ...

    def DumpGLObjects(self, filename: str) -> bool:
        """
        Dumps OpenGL Objects

        Args:
            filename (str)

        Returns:
            success (bool)
        """
        ...

    def EditScript(self) -> None:
        """
        Edit Script
        """
        ...

    def Execute(self) -> None:
        ...

    def FindReg(self, id: str, type: int | None = None) -> Registry:
        """
        Find a registry object by ID

        Args:
            id (str)
            type (Optional[int])

        Returns:
            reg (Registry)
        """
        ...

    def GetActiveFrameIndex(self) -> None:
        ...

    def GetActiveWndIndex(self) -> None:
        ...

    def GetAppInfo(self) -> None:
        ...

    def GetArgs(self) -> dict[Any, Any]:
        """
        Get command line arguments

        Returns:
            args (dict[Any, Any])
        """
        ...

    def GetCPULoad(self) -> None:
        ...

    def GetClipboard(self) -> dict[Any, Any] | str:
        """
        Retrieves the tool(s) on the clipboard, as tables and as ASCII text.

        Returns:
            cliptbl (dict[Any, Any])
            clipstr (str)
        """
        ...

    def GetCompList(self) -> dict[Any, Any]:
        """
        Retrieves a table of all compositions currently present

        Returns:
            complist (dict[Any, Any])
        """
        ...

    def GetCurrentComp(self) -> Composition:
        """
        Returns the currently active composition

        Returns:
            comp (Composition)
        """
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

    def GetEnv(self, name: str) -> str:
        """
        Retrieve the value of an environment variable

        Args:
            name (str)

        Returns:
            value (str)
        """
        ...

    def GetFairlight(self) -> None:
        ...

    def GetGlobalPathMap(self, built_ins: bool | None = None, defaults: bool | None = None) -> dict[Any, Any]:
        """
        Returns a table of all global path maps

        Args:  built_ins - include built-in path maps (default: true)
        defaults  - include factory default path maps (default: true)
        Returns: Table of path strings, keyed by map name.

        Args:
            built_ins (Optional[bool])
            defaults (Optional[bool])

        Returns:
            map (dict[Any, Any])
        """
        ...

    def GetMainWindow(self) -> None:
        ...

    def GetMousePos(self) -> None:
        ...

    def GetNumRecentFiles(self) -> None:
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

    def GetPreviewList(self) -> dict[Any, Any]:
        """
        Retrieves a table of global previews

        Returns:
            previewlist (dict[Any, Any])
        """
        ...

    def GetRLMLicenseInfo(self) -> None:
        ...

    def GetRecentCompList(self) -> None:
        ...

    def GetRecentFileName(self) -> None:
        ...

    def GetRegAttrs(self, id: str, type: int | None = None) -> dict[Any, Any]:
        """
        Retrieve information about a registry ID

        Args:
            id (str)
            type (Optional[int])

        Returns:
            attrs (dict[Any, Any])
        """
        ...

    def GetRegList(self, typemask: int) -> dict[Any, Any]:
        """
        Retrieve a list of all registry objects known to the system

        Args:
            typemask (int)

        Returns:
            reglist (dict[Any, Any])
        """
        ...

    def GetRegSummary(self, typemask: int, hidden: bool | None = None) -> dict[Any, Any]:
        """
        Retrieve a list of basic info for all registry objects known to the system

        Args:
            typemask (int)
            hidden (Optional[bool])

        Returns:
            regattrs (dict[Any, Any])
        """
        ...

    def GetResolve(self) -> None:
        ...

    def GetToolIcon(self) -> None:
        ...

    def GetToolList(self) -> None:
        ...

    def GetVersion(self) -> None:
        ...

    def InstallFile(self) -> None:
        ...

    def IsNetworkAllowed(self) -> None:
        ...

    def IsUIVisible(self) -> None:
        ...

    def IsUtilityOpen(self, id: str) -> None:
        ...

    @overload
    def LoadComp(self, filename: str, quiet: bool | None = None, autoclose: bool | None = None, hidden: bool | None = None) -> Composition:
        """
        Loads an existing composition

        Args:
            filename (str)
            quiet (Optional[bool])
            autoclose (Optional[bool])
            hidden (Optional[bool])

        Returns:
            comp (Composition)
        """
        ...

    @overload
    def LoadComp(self, filename: str, options: dict[Any, Any]) -> Composition:
        """
        Loads an existing composition

        Args:
            filename (str)
            options (dict[Any, Any])

        Returns:
            comp (Composition)
        """
        ...

    @overload
    def LoadComp(self, savedcomp: MemBlock, options: dict[Any, Any]) -> Composition:
        """
        Loads an existing composition

        Args:
            savedcomp (MemBlock)
            options (dict[Any, Any])

        Returns:
            comp (Composition)
        """
        ...

    def LoadPrefs(self, filename: str | None = None, mastername: str | None = None) -> bool:
        """
        Reloads all current global preferences

        filename:    pathname to read the prefs file from
        masterprefs: pathname of overriding prefs file

        Args:
            filename (Optional[str])
            mastername (Optional[str])

        Returns:
            success (bool)
        """
        ...

    def LoadRecentComp(self, index: int, quiet: bool | None = None, autoclose: bool | None = None, hidden: bool | None = None) -> Composition:
        """
        Loads an composition from the recent file list

        Args:
            index (int)
            quiet (Optional[bool])
            autoclose (Optional[bool])
            hidden (Optional[bool])

        Returns:
            comp (Composition)
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

    def MapPathSegments(self, path: str) -> dict[Any, Any]:
        """
        Expands all path mappings in a multipath

        Returns a table of path strings with all mappings expanded. All paths of a multipath are returned.

        Args:
            path (str)

        Returns:
            mapped (dict[Any, Any])
        """
        ...

    def NewComp(self, quiet: bool | None = None, autoclose: bool | None = None, hidden: bool | None = None) -> Composition:
        """
        Creates a new composition

        Args:
            quiet (Optional[bool])
            autoclose (Optional[bool])
            hidden (Optional[bool])

        Returns:
            comp (Composition)
        """
        ...

    def NewFloatFrame(self) -> None:
        ...

    def NewImageView(self) -> None:
        ...

    def NewTabbedFrame(self) -> None:
        ...

    def OpenFile(self, filename: str, mode: int) -> File:
        """
        Open a file

        Arguments:

        filename: specifies the full path and name of the file to open

        mode: Specifies the mode(s) of file access required, from a combination of the following constants:
        FILE_MODE_READ        - Read access
        FILE_MODE_WRITE       - Write access
        FILE_MODE_UNBUFFERED  - Unbuffered access
        FILE_MODE_SHARED      - Shared access

        Args:
            filename (str)
            mode (int)

        Returns:
            file (File)
        """
        ...

    def OpenLibrary(self) -> None:
        ...

    def OpenLibraryStudio(self) -> None:
        ...

    def Paste(self) -> None:
        ...

    def PasteSettings(self) -> None:
        ...

    def Print(self) -> None:
        ...

    @overload
    def QueueComp(self, filename: str, start: int | None = None, end: int | None = None, group: str | None = None) -> RenderJob:
        """
        Queue a composition to be rendered locally

        Arguments:
        Filename - string containing the path to the composition or script to be queued
        Start    - (optional) first frame to render
        End      - (optional) last frame to render
        Group    - (optional) string containing the Slave group to render with

        Returns: The new RenderJob object, if successful, else nil

        Args:
            filename (str)
            start (Optional[int])
            end (Optional[int])
            group (Optional[str])

        Returns:
            job (RenderJob)
        """
        ...

    @overload
    def QueueComp(self, args: dict[Any, Any]) -> RenderJob:
        """
        Queue a composition to be rendered locally

        Arguments:
        Filename - string containing the path to the composition or script to be queued
        Start    - (optional) first frame to render
        End      - (optional) last frame to render
        Group    - (optional) string containing the Slave group to render with

        Returns: The new RenderJob object, if successful, else nil

        Args:
            args (dict[Any, Any])

        Returns:
            job (RenderJob)
        """
        ...

    def Quit(self, exitcode: int) -> None:
        """
        Quit Fusion

        The Quit() function will cause Fusion to exit, without saving changes.
        If no exitcode is specified, the Fusion process will return 0.

        Args:
            exitcode (int)
        """
        ...

    def RemoveConfig(self) -> None:
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
        Run a script

        Args:
            filename (str)
        """
        ...

    def SavePrefs(self, filename: str | None = None) -> None:
        """
        Saves all current global preferences

        filename: pathname to write the prefs file to

        Args:
            filename (Optional[str])
        """
        ...

    def SelectAll(self) -> None:
        ...

    def SetActiveFrameIndex(self) -> None:
        ...

    def SetActiveWndIndex(self) -> None:
        ...

    def SetBatch(self) -> None:
        ...

    @overload
    def SetClipboard(self) -> bool | dict[Any, Any]:
        """
        Sets the clipboard to contain the tool(s) specifed by a table or as ASCII text.

        Returns:
            success (bool)
            cliptbl (dict[Any, Any])
        """
        ...

    @overload
    def SetClipboard(self) -> bool | str:
        """
        Sets the clipboard to contain the tool(s) specifed by a table or as ASCII text.

        Returns:
            success (bool)
            clipstr (str)
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

    def SetFusionApp(self) -> None:
        ...

    def SetMasterApp(self) -> None:
        ...

    def SetOnlyActiveComp(self) -> None:
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

    def ShowAbout(self) -> None:
        """
        Display the About dialog
        """
        ...

    def ShowPrefs(self, pageid: str | None = None, showall: bool | None = None, comp: Composition | None = None) -> None:
        """
        Display the Preferences dialog

        Args:
            pageid (Optional[str])
            showall (Optional[bool])
            comp (Optional[Composition])
        """
        ...

    def ShowUI(self) -> None:
        ...

    def ShowWindow(self, mode: int) -> None:
        """
        Show or Hide main window

        Arguments:
        mode: Can be a combination of the below:
        SW_SHOW       - activates and displays the window
        SW_HIDE       - hides the window completely
        SW_MAXIMIZE   - maximize the window
        SW_MINIMIZE   - minimize the window
        SW_RESTORE    - restores the window to normal size/position

        Args:
            mode (int)
        """
        ...

    def Sleep(self, seconds: int) -> None:
        ...

    def Test(self) -> None:
        ...

    def ToggleBins(self) -> None:
        """
        Shows or hides the Bins window
        """
        ...

    def ToggleRenderManager(self) -> None:
        """
        Shows or hides the Render Manager
        """
        ...

    def ToggleUtility(self, id: str) -> None:
        """
        Shows or hides a Utility plugin

        Args:
            id (str)
        """
        ...

    def UpdateMenus(self) -> None:
        ...

    def _Memory_Purge(self, seconds: int) -> None:
        ...

    def _NewComp(self, quiet: bool | None = None, autoclose: bool | None = None, hidden: bool | None = None) -> Composition:
        """
        Creates a new composition

        Args:
            quiet (Optional[bool])
            autoclose (Optional[bool])
            hidden (Optional[bool])

        Returns:
            comp (Composition)
        """
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

        Set the content of an attributes

        Args:
            attributes (dict[Any, Any])
        """
        ...

