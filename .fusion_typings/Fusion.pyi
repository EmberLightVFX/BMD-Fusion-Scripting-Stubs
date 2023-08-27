from typing import Any, overload

from QueueManager import QueueManager_
from Composition import Composition_
from FontList import FontList_
from ActionManager import ActionManager_
from HotkeyManager import HotkeyManager_
from UIManager import UIManager_
from MailMessage import MailMessage_
from Registry import Registry_
from MemBlock import MemBlock_
from RenderJob import RenderJob_
from _non_existing import Bins_, CacheManager_, MenuManager_, File_


class Fusion_:

	#---Properties---#
	QueueManager: QueueManager_
	"""
	The global render manager for this instance of Fusion

	Read Only
	"""
	BinManager: Bins_
	"""
	Bins

	Read Only
	"""
	CacheManager: CacheManager_
	"""
	The Global Cache Manager

	Read Only
	"""
	MouseX: Any
	"""
	Read Only
	"""
	RenderManager: QueueManager_
	"""
	The global render manager for this instance of Fusion

	Read Only
	"""
	MouseY: Any
	"""
	Read Only
	"""
	MenuManager: MenuManager_
	"""
	The Global Menu Manager

	Read Only
	"""
	CurrentComp: Composition_
	"""
	Represents the currently active composition

	The CurrentComp variable represents the currently active composition within Fusion.

	Read Only
	"""
	FileLogging: Any
	"""
	Read/Write
	"""
	FontManager: FontList_
	"""
	The Global Font Manager

	Read Only
	"""
	Build: int
	"""
	The build number of Fusion.


	Read Only
	"""
	ActionManager: ActionManager_
	"""
	The Global Action Manager

	Read Only
	"""
	HotkeyManager: HotkeyManager_
	"""
	The Global Hotkey Manager

	Read Only
	"""
	Version: int
	"""
	The version number of Fusion.


	Read Only
	"""
	CurrentFrame: Any
	"""
	Read Only
	"""
	UIManager: UIManager_
	"""
	Read Only
	"""
	Bins: Bins_
	"""
	Bins

	Read Only
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
	def CreateMail(self) -> MailMessage_:
		"""
		Create an empty Mail message object
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
		"""
		...
	def EditScript(self) -> None:
		"""
		Edit Script
		"""
		...
	def Execute(self) -> None:
		...
	def FindReg(self, id: str, type: int = int()) -> Registry_:
		"""
		Find a registry object by ID
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
	def GetCPULoad(self) -> None:
		...
	def GetClipboard(self) -> tuple[dict[Any, Any], str]:
		"""
		Retrieves the tool(s) on the clipboard, as tables and as ASCII text.
		"""
		...
	def GetCompList(self) -> dict[Any, Any]:
		"""
		Retrieves a table of all compositions currently present
		"""
		...
	def GetCurrentComp(self) -> Composition_:
		"""
		Returns the currently active composition
		"""
		...
	def GetData(self, name: str = str()) -> int | str | bool | dict[Any, Any] | list[Any]:
		"""
		Get custom persistent data
		"""
		...
	def GetEnv(self, name: str) -> str:
		"""
		Retrieve the value of an environment variable
		"""
		...
	def GetFairlight(self) -> None:
		...
	def GetGlobalPathMap(self, built_ins: bool = bool(), defaults: bool = bool()) -> dict[Any, Any]:
		"""
		Returns a table of all global path maps

		Args:	built_ins - include built-in path maps (default: true)
					 defaults	- include factory default path maps (default: true)
		Returns: Table of path strings, keyed by map name.
		"""
		...
	def GetMainWindow(self) -> None:
		...
	def GetMousePos(self) -> None:
		...
	def GetNumRecentFiles(self) -> None:
		...
	def GetPrefs(self, prefname: str = str(), exclude_defaults: bool = bool()) -> dict[Any, Any]:
		"""
		Retrieve a table of preferences
		"""
		...
	def GetPreviewList(self) -> dict[Any, Any]:
		"""
		Retrieves a table of global previews
		"""
		...
	def GetRLMLicenseInfo(self) -> None:
		...
	def GetRecentCompList(self) -> None:
		...
	def GetRecentFileName(self) -> None:
		...
	def GetRegAttrs(self, id: str, type: int = int()) -> dict[Any, Any]:
		"""
		Retrieve information about a registry ID
		"""
		...
	def GetRegList(self, typemask: int) -> dict[Any, Any]:
		"""
		Retrieve a list of all registry objects known to the system
		"""
		...
	def GetRegSummary(self, typemask: int, hidden: bool = bool()) -> dict[Any, Any]:
		"""
		Retrieve a list of basic info for all registry objects known to the system
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
	def LoadComp(self, filename: str, quiet: bool = bool(), autoclose: bool = bool(), hidden: bool = bool()) -> Composition_:
		"""
		Loads an existing composition
		"""
		...
	@overload
	def LoadComp(self, filename: str, options: dict[Any, Any]) -> Composition_:
		"""
		Loads an existing composition
		"""
		...
	@overload
	def LoadComp(self, savedcomp: MemBlock_, options: dict[Any, Any]) -> Composition_:
		"""
		Loads an existing composition
		"""
		...
	def LoadPrefs(self, filename: str = str(), mastername: str = str()) -> bool:
		"""
		Reloads all current global preferences

		filename:		pathname to read the prefs file from
		masterprefs: pathname of overriding prefs file
		"""
		...
	def LoadRecentComp(self, index: int, quiet: bool = bool(), autoclose: bool = bool(), hidden: bool = bool()) -> Composition_:
		"""
		Loads an composition from the recent file list
		"""
		...
	def MapPath(self, path: str) -> str:
		"""
		Expands path mappings in a path string

		Returns the path string with all mappings expanded. Only the first path of a multipath is returned.
		"""
		...
	def MapPathSegments(self, path: str) -> dict[Any, Any]:
		"""
		Expands all path mappings in a multipath

		Returns a table of path strings with all mappings expanded. All paths of a multipath are returned.
		"""
		...
	def NewComp(self, quiet: bool = bool(), autoclose: bool = bool(), hidden: bool = bool()) -> Composition_:
		"""
		Creates a new composition
		"""
		...
	def NewFloatFrame(self) -> None:
		...
	def NewImageView(self) -> None:
		...
	def NewTabbedFrame(self) -> None:
		...
	def OpenFile(self, filename: str, mode: int) -> File_:
		"""
		Open a file

		Arguments:

			filename: specifies the full path and name of the file to open

			mode: Specifies the mode(s) of file access required, from a combination of the following constants:
				FILE_MODE_READ				- Read access
				FILE_MODE_WRITE			 - Write access
				FILE_MODE_UNBUFFERED	- Unbuffered access
				FILE_MODE_SHARED			- Shared access
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
	def QueueComp(self, filename: str, start: int = int(), end: int = int(), group: str = str()) -> RenderJob_:
		"""
		Queue a composition to be rendered locally

		Arguments:
			 Filename - string containing the path to the composition or script to be queued
			 Start		- (optional) first frame to render
			 End			- (optional) last frame to render
			 Group		- (optional) string containing the Slave group to render with

		Returns: The new RenderJob object, if successful, else nil
		"""
		...
	@overload
	def QueueComp(self, args: dict[Any, Any]) -> RenderJob_:
		"""
		Queue a composition to be rendered locally

		Arguments:
			 Filename - string containing the path to the composition or script to be queued
			 Start		- (optional) first frame to render
			 End			- (optional) last frame to render
			 Group		- (optional) string containing the Slave group to render with

		Returns: The new RenderJob object, if successful, else nil
		"""
		...
	def Quit(self, exitcode: int) -> None:
		"""
		Quit Fusion

		The Quit() function will cause Fusion to exit, without saving changes.
		If no exitcode is specified, the Fusion process will return 0.
		"""
		...
	def RemoveConfig(self) -> None:
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
	def SavePrefs(self, filename: str = str()) -> None:
		"""
		Saves all current global preferences

		filename: pathname to write the prefs file to
		"""
		...
	def SelectAll(self) -> None:
		...
	def SetActiveFrameIndex(self) -> None:
		...
	def SetActiveWndIndex(self) -> None:
		...
	def SetAttrs(self, attributes: dict[Any, Any]) -> None:
		"""
		Set the content of an attributes
		"""
		...
	def SetBatch(self) -> None:
		...
	@overload
	def SetClipboard(self) -> tuple[bool, dict[Any, Any]]:
		"""
		Sets the clipboard to contain the tool(s) specifed by a table or as ASCII text.
		"""
		...
	@overload
	def SetClipboard(self) -> tuple[bool, str]:
		"""
		Sets the clipboard to contain the tool(s) specifed by a table or as ASCII text.
		"""
		...
	def SetData(self, name: str, value: int | str | bool | dict[Any, Any] | list[Any]) -> None:
		"""
		Set custom persistent data
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
		"""
		...
	@overload
	def SetPrefs(self, prefs: dict[Any, Any]) -> None:
		"""
		Set preferences from a table of attributes
		"""
		...
	def ShowAbout(self) -> None:
		"""
		Display the About dialog
		"""
		...
	def ShowPrefs(self, pageid: str = str(), showall: bool = bool(), comp: Composition_ = Composition_()) -> None:
		"""
		Display the Preferences dialog
		"""
		...
	def ShowUI(self) -> None:
		...
	def ShowWindow(self, mode: int) -> None:
		"""
		Show or Hide main window

		Arguments:
			mode: Can be a combination of the below:
				SW_SHOW			 - activates and displays the window
				SW_HIDE			 - hides the window completely
				SW_MAXIMIZE	 - maximize the window
				SW_MINIMIZE	 - minimize the window
				SW_RESTORE		- restores the window to normal size/position
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
		"""
		...
	def UpdateMenus(self) -> None:
		...
	def _Memory_Purge(self, seconds: int) -> None:
		...
	def _NewComp(self, quiet: bool = bool(), autoclose: bool = bool(), hidden: bool = bool()) -> Composition_:
		"""
		Creates a new composition
		"""
		...
	def header_text(self) -> None:
		...

Fusion = Fusion_