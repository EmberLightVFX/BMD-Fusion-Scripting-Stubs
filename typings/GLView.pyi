from typing import Any, overload, Literal

from GLViewer import _GLViewer


class _GLView:

	#---Properties---#
	CurrentViewer: _GLViewer
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
	@overload
	def LoadPrefs(self) -> None:
		"""
		Saves the current view prefs to a named configuration
		"""
		...
	@overload
	def LoadPrefs(self, configname: str) -> None:
		"""
		Saves the current view prefs to a named configuration
		"""
		...
	def ShowLUTEditor(self) -> None:
		"""
		Pops up the Editor window for the current Monitor LUT
		"""
		...
	def IsLUTEnabled(self) -> bool:
		"""
		Returns true if the current Monitor LUT is enabled
		"""
		...
	def EnableLUT(self, enable: bool = bool()) -> None:
		"""
		Enables or disables the current Monitor LUT
		"""
		...
	def AddToolAction(self):
		...
	def header_text(self):
		...
	def IsWipeEnabled(self):
		...
	def WipeEnable(self):
		...
	def GetStereoMethod(self) -> str:
		"""
		Returns the method and options being used for stereo display

		method can be 'Quad Buffer', 'Anaglyph', 'Crosseyed', 'Interlaced', 'Checkerboard', 'Left Eye Only' or 'Right'
		If method is 'Anaglyph':
			option1 can be 'Red/Cyan', 'Red/Green',	'Red/Blue', 'Amber/Blue' or 'Green/Magenta'
			option2 can be 'Monochrome', 'Half-color',	'Color', 'Optimised' or 'Dubois'
		"""
		...
	def SetStereoMethod(self, method: str, option1, option2) -> None:
		"""
		Sets the method for stereo display

		method can be one of the following strings:
			'Quad Buffer'	Enable OpenGL quad-buffered stereo mode
			'Anaglyph'		Tint and combine views for anaglyph glasses
				option1 can be 'Red/Cyan', 'Red/Green',	'Red/Blue', 'Amber/Blue' or 'Green/Magenta'
				option2 can be 'Monochrome', 'Half-color',	'Color', 'Optimised' or 'Dubois' (forces 'Red/Cyan')
			'Crosseyed'		Display views side-by-side for crosseyed viewing
			'Interlaced'		Display views on alternate scanlines
			'Checkerboard'		Stereo support for checkerboard DLPs
				option1 is the value for gamma correction of the polariser screen
			'Left Eye Only'	Display left eye view only
			'Right Eye Only'	Display right eye view only
		"""
		...
	def GetStereoSource(self) -> tuple[bool, bool, str]:
		"""
		Returns the source being used for stereo display

		ABsource is true if the A & B buffers are used for left & right
		stacked is true if the two halves of the image are used
		stackmethod will be 'Horizontal' or 'Vertical'
		"""
		...
	def SetStereoSource(self, ABsource: bool, stacked: bool, stackmethod: str = str()) -> None:
		"""
		Sets the source for the left & right stereo images

		Pass true for ABsource to use the A and B buffers for left & right views.
		Pass true for stacked to use the two halves of the image for left & right views.
		stackmethod may be 'Horizontal' or 'Vertical' for side-by-side or over-under images, respectively.
		"""
		...
	def IsStereoSwapped(self) -> bool:
		"""
		Indicates if the left & right stereo eyes are currently swapped
		"""
		...
	@overload
	def SwapStereo(self) -> None:
		"""
		Swaps left & right stereo eye views
		"""
		...
	@overload
	def SwapStereo(self, enable: bool = bool()) -> None:
		"""
		Swaps left & right stereo eye views
		"""
		...
	def IsStereoEnabled(self) -> bool:
		"""
		Indicates if stereo display is currently enabled
		"""
		...
	def EnableStereo(self, enable: bool = bool()) -> None:
		"""
		Enables or disables 3D stereo display
		"""
		...
	def GetViewerList(self) -> dict[Any, Any]:
		"""
		Returns a list of available viewers
		"""
		...
	def GetSplitTable(self) -> dict[Any, Any]:
		"""
		Get the split position of the view as a table

		Returns:
			 x = table[1]
			 y = table[2]
			 angle = table[3]
		"""
		...
	def GetSplit(self) -> tuple[int, int, int]:
		"""
		Get the split position of the view
		"""
		...
	def SetSplit(self, x: int, y: int, angle: int) -> None:
		"""
		Set the split position of the view
		"""
		...
	def DisableCurrentTools(self) -> None:
		"""
		Pass-through the currently selected tools
		"""
		...
	def SetPos(self, x: int, y: int, z: int = int()) -> bool:
		"""
		Set the position of the display
		"""
		...
	def ShowingSubView(self) -> bool:
		"""
		Returns true if the inset SubView is currently being displayed
		"""
		...
	def ShowSubView(self, enable: bool = bool()) -> None:
		"""
		Enables the inset SubView display
		"""
		...
	def ShowingQuadView(self) -> bool:
		"""
		Returns true if the view is split into four
		"""
		...
	def ShowQuadView(self, enable: bool = bool()) -> None:
		"""
		Splits the view into four subviews
		"""
		...
	def GetLocked(self) -> bool:
		"""
		Returns true if the display is locked
		"""
		...
	def SetLocked(self, enable: bool = bool()) -> None:
		"""
		Lock or unlock the display
		"""
		...
	def GetRotTable(self) -> dict[Any, Any]:
		"""
		Returns the x,y,z rotation of the display in degrees as a table

		Returns:
					 x = table[1]
					 y = table[2]
					 z = table[3]
		"""
		...
	def GetRot(self) -> tuple[int, int, int]:
		"""
		Returns the x,y,z rotation of the display in degrees
		"""
		...
	def SetRot(self, x: int, y: int, z: int) -> None:
		"""
		Set the x,y,z rotation of the display in degrees
		"""
		...
	def ResetView(self) -> None:
		"""
		Resets the display to default position etc
		"""
		...
	def GetScaleFit(self) -> bool:
		"""
		Indicates if the display is set to scale-to-fit
		"""
		...
	def GetPreview(self, buffer: int = int()) -> None:
		"""
		Returns the buffer's Preview

		where 'buffer' is one of the following numbers:
			 0 = A
			 1 = B
			 2 = A|B split
		If 'buffer' is not specified, the current Preview is returned.
		"""
		...
	def GetBuffer(self) -> int:
		"""
		Returns which buffer is shown

		where 'buffer' is one of the following numbers:
			 0 = A
			 1 = B
			 2 = A|B split
		"""
		...
	def SetBuffer(self, buffer: int, toggle: bool = bool()) -> None:
		"""
		Show a particular buffer

		where 'buffer' is one of the following numbers:
			 0 = A
			 1 = B
			 2 = A|B split
		"""
		...
	def DisableSelectedTools(self) -> None:
		"""
		Pass-through the selected tools
		"""
		...
	def SwapSubView(self) -> bool:
		"""
		Swaps the SubView with the Main View
		"""
		...
	def GetPosTable(self) -> dict[Any, Any]:
		"""
		Returns the position of the display as a table

		Returns:
					 x = table[1]
					 y = table[2]
					 z = table[3]
		"""
		...
	def GetPrefs(self) -> dict[Any, Any]:
		"""
		Retrieve a table of preferences for this view

		Returns a table of Preference attributes
		"""
		...
	def GetPos(self) -> tuple[int, int, int]:
		"""
		Returns the position of the display
		"""
		...
	def LoadLUTFile(self, pathname: str) -> bool:
		"""
		Loads a LUT file, setting or LUT plugin ID into the Monitor LUT
		"""
		...
	def SetScale(self, scale: int) -> None:
		"""
		Set the scale of the display
		"""
		...
	def GetScale(self) -> int:
		"""
		Returns the scale of the display
		"""
		...
	@overload
	def SavePrefs(self) -> None:
		"""
		Saves the current view prefs to a named configuration
		"""
		...
	@overload
	def SavePrefs(self, configname: str) -> None:
		"""
		Saves the current view prefs to a named configuration
		"""
		...

GLView = _GLView