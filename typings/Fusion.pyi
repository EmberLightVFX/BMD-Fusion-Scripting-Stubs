from typing import Any, overload

from QueueManager import _QueueManager
from Composition import _Composition
from FontList import _FontList
from ActionManager import _ActionManager
from HotkeyManager import _HotkeyManager
from UIManager import _UIManager
from MailMessage import _MailMessage
from Registry import _Registry
from RenderJob import _RenderJob
from MemBlock import _MemBlock
from _non_existing import _Bins, _CacheManager, _MenuManager, _File


class _Fusion:

	#---Properties---#
	QueueManager: _QueueManager
	"""
	The global render manager for this instance of Fusion

	Read Only
	"""
	BinManager: _Bins
	"""
	Bins

	Read Only
	"""
	CacheManager: _CacheManager
	"""
	The Global Cache Manager

	Read Only
	"""
	MouseX: Any
	"""
	Read Only
	"""
	RenderManager: _QueueManager
	"""
	The global render manager for this instance of Fusion

	Read Only
	"""
	MouseY: Any
	"""
	Read Only
	"""
	MenuManager: _MenuManager
	"""
	The Global Menu Manager

	Read Only
	"""
	CurrentComp: _Composition
	"""
	Represents the currently active composition

			The CurrentComp variable represents the currently active composition within Fusion.

	Read Only
	"""
	FileLogging: Any
	"""
	Read/Write
	"""
	FontManager: _FontList
	"""
	The Global Font Manager

	Read Only
	"""
	Build: int
	"""
	The build number of Fusion.


	Read Only
	"""
	ActionManager: _ActionManager
	"""
	The Global Action Manager

	Read Only
	"""
	HotkeyManager: _HotkeyManager
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
	UIManager: _UIManager
	"""
	Read Only
	"""
	Bins: _Bins
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
	def InstallFile(self):
		...
	def GetRLMLicenseInfo(self):
		...
	def GetCurrentComp(self) -> _Composition:
		"""
		Returns the currently active composition
		"""
		...
	def GetFairlight(self):
		...
	def GetResolve(self):
		...
	def RemoveConfig(self):
		...
	def AddConfig(self):
		...
	def GetToolIcon(self) -> None:
		...
	def SetFusionApp(self) -> None:
		...
	def MapPathSegments(self, path: str) -> dict[Any, Any]:
		"""
		Expands all path mappings in a multipath

		Returns a table of path strings with all mappings expanded. All paths of a multipath are returned.
		"""
		...
	def _Memory_Purge(self, seconds: int) -> None:
		...
	def EditScript(self) -> None:
		"""
		Edit Script
		"""
		...
	def GetRecentFileName(self):
		...
	def GetNumRecentFiles(self):
		...
	def CustomizeToolbars(self):
		...
	def ShowUI(self):
		...
	def IsUIVisible(self):
		...
	def SetActiveWndIndex(self):
		...
	def SetActiveFrameIndex(self):
		...
	def GetActiveWndIndex(self):
		...
	def GetActiveFrameIndex(self):
		...
	def GetRecentCompList(self):
		...
	def ClearRecentCompList(self):
		...
	def DeselectAll(self):
		...
	def GetPreviewList(self) -> dict[Any, Any]:
		"""
		Retrieves a table of global previews
		"""
		...
	def Delete(self):
		...
	def PasteSettings(self):
		...
	def Cut(self):
		...
	def SetOnlyActiveComp(self):
		...
	def NewFloatFrame(self):
		...
	def NewTabbedFrame(self):
		...
	def NewImageView(self):
		...
	def IsNetworkAllowed(self):
		...
	def AllowNetwork(self):
		...
	def CreateFloatingView(self):
		...
	def SetBatch(self):
		...
	def ClearFileLog(self):
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
	def Paste(self):
		...
	def SetClipboard(self) -> tuple[bool, str | bool, dict[Any, Any]]:
		"""
		Sets the clipboard to contain the tool(s) specifed by a table or as ASCII text.
		"""
		...
	def GetClipboard(self) -> tuple[dict[Any, Any], str]:
		"""
		Retrieves the tool(s) on the clipboard, as tables and as ASCII text.
		"""
		...
	def GetPrefs(self, prefname: str = str(), exclude_defaults: bool = bool()) -> dict[Any, Any]:
		"""
		Retrieve a table of preferences
		"""
		...
	def CreateMail(self) -> _MailMessage:
		"""
		Create an empty Mail message object
		"""
		...
	def GetRegList(self, typemask: int) -> dict[Any, Any]:
		"""
		Retrieve a list of all registry objects known to the system
		"""
		...
	def OpenFile(self, filename: str, mode: int) -> _File:
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
	def GetEnv(self, name: str) -> str:
		"""
		Retrieve the value of an environment variable
		"""
		...
	def SavePrefs(self, filename: str = str()) -> None:
		"""
		Saves all current global preferences

		filename: pathname to write the prefs file to
		"""
		...
	def LoadPrefs(self, filename: str = str(), mastername: str = str()) -> bool:
		"""
		Reloads all current global preferences

		filename:		pathname to read the prefs file from
		masterprefs: pathname of overriding prefs file
		"""
		...
	def FindReg(self, id: str, type: int = int()) -> _Registry:
		"""
		Find a registry object by ID
		"""
		...
	def GetRegAttrs(self, id: str, type: int = int()) -> dict[Any, Any]:
		"""
		Retrieve information about a registry ID
		"""
		...
	def GetCompList(self) -> dict[Any, Any]:
		"""
		Retrieves a table of all compositions currently present
		"""
		...
	def ShowAbout(self) -> None:
		"""
		Display the About dialog
		"""
		...
	@overload
	def QueueComp(self, filename: str, start: int = int(), end: int = int(), group: str = str()) -> _RenderJob:
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
	def QueueComp(self, args: dict[Any, Any]) -> _RenderJob:
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
	def LoadRecentComp(self, index: int, quiet: bool = bool(), autoclose: bool = bool(), hidden: bool = bool()) -> _Composition:
		"""
		Loads an composition from the recent file list
		"""
		...
	@overload
	def LoadComp(self, filename: str, quiet: bool = bool(), autoclose: bool = bool(), hidden: bool = bool()) -> _Composition:
		"""
		Loads an existing composition
		"""
		...
	@overload
	def LoadComp(self, filename: str, options: dict[Any, Any]) -> _Composition:
		"""
		Loads an existing composition
		"""
		...
	@overload
	def LoadComp(self, savedcomp: _MemBlock, options: dict[Any, Any]) -> _Composition:
		"""
		Loads an existing composition
		"""
		...
	def NewComp(self, quiet: bool = bool(), autoclose: bool = bool(), hidden: bool = bool()) -> _Composition:
		"""
		Creates a new composition
		"""
		...
	def _NewComp(self, quiet: bool = bool(), autoclose: bool = bool(), hidden: bool = bool()) -> _Composition:
		"""
		Creates a new composition
		"""
		...
	def OpenLibraryStudio(self):
		...
	def OpenLibrary(self):
		...
	def header_text(self):
		...
	def ToggleRenderManager(self) -> None:
		"""
		Shows or hides the Render Manager
		"""
		...
	def IsUtilityOpen(self, id: str) -> None:
		...
	def ToggleUtility(self, id: str) -> None:
		"""
		Shows or hides a Utility plugin
		"""
		...
	def GetMainWindow(self):
		...
	def GetCPULoad(self):
		...
	def GetAppInfo(self):
		...
	def GetMousePos(self):
		...
	def UpdateMenus(self):
		...
	def Test(self):
		...
	def Print(self):
		...
	def ToggleBins(self) -> None:
		"""
		Shows or hides the Bins window
		"""
		...
	def GetRegSummary(self, typemask: int, hidden: bool = bool()) -> dict[Any, Any]:
		"""
		Retrieve a list of basic info for all registry objects known to the system
		"""
		...
	def ShowPrefs(self, pageid: str = str(), showall: bool = bool(), comp: _Composition = _Composition()) -> None:
		"""
		Display the Preferences dialog
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
	def SetMasterApp(self) -> None:
		...
	def SetData(self, name: str, value: int | str | bool | dict[Any, Any]) -> None:
		"""
		Set custom persistent data
		"""
		...
	def SelectAll(self):
		...
	def RunScript(self, filename: str) -> None:
		"""
		Run a script
		"""
		...
	def ReverseMapPath(self, mapped: str) -> str:
		"""
		Collapses a path into best-matching path map

		Returns the path string relative to nearest applicable mapped path.
		"""
		...
	def Quit(self, exitcode: int) -> None:
		"""
		Quit Fusion

		The Quit() function will cause Fusion to exit, without saving changes.
		If no exitcode is specified, the Fusion process will return 0.
		"""
		...
	def GetData(self, name: str = str()) -> int | str | bool | dict[Any, Any]:
		"""
		Get custom persistent data
		"""
		...
	def Sleep(self, seconds: int) -> None:
		...
	def GetArgs(self) -> dict[Any, Any]:
		"""
		Get command line arguments
		"""
		...
	def Execute(self):
		...
	def GetGlobalPathMap(self, built_ins: bool = bool(), defaults: bool = bool()) -> dict[Any, Any]:
		"""
		Returns a table of all global path maps

		Args:	built_ins - include built-in path maps (default: true)
					 defaults	- include factory default path maps (default: true)
		Returns: Table of path strings, keyed by map name.
		"""
		...
	def DumpGLObjects(self, filename: str) -> bool:
		"""
		Dumps OpenGL Objects
		"""
		...
	def DeactivateLicense(self) -> None:
		"""
		Deactivate Fusion Studio on this machine
		"""
		...
	def MapPath(self, path: str) -> str:
		"""
		Expands path mappings in a path string

		Returns the path string with all mappings expanded. Only the first path of a multipath is returned.
		"""
		...
	def Copy(self):
		...
	def GetVersion(self):
		...
	def GetToolList(self) -> None:
		...

Fusion = _Fusion