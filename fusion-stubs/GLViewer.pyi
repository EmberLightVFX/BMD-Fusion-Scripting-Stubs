from typing import Any

class GLViewer:

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
	def AreControlsShown(self) -> bool:
		"""
		Returns true if controls are being displayed on the view

		Returns:
			enabled (bool)
		"""
		...

	def AreGuidesShown(self) -> bool:
		"""
		Returns true if image guides are being displayed on the view

		Returns:
			enabled (bool)
		"""
		...

	def EnableChecker(self, enable: bool | None = None) -> None:
		"""
		Enables or disables drawing a checker underlay

		Args:
			enable (Optional[bool])
		"""
		...

	def EnableLUT(self, enable: bool | None = None) -> None:
		...

	def GetAlphaOverlayColor(self) -> int:
		"""
		Return which alpha overlay is being used

		0 = None, 1 = Red, 2 = Green, 3 = Yellow, 4 = Blue, 5 = Cyan, 6 = Magenta, 7 = White.

		Returns:
			color (int)
		"""
		...

	def GetAspectCorrection(self) -> bool:
		"""
		Returns true if the viewer is correcting the aspect of images

		Returns:
			enabled (bool)
		"""
		...

	def GetChannel(self) -> int:
		"""
		Return which channel is shown

		Returns:
			channel (int)
		"""
		...

	def GetPos(self) -> int | int | int:
		"""
		Get the position of the viewer

		Returns:
			x (int)
			y (int)
			z (int)
		"""
		...

	def GetPosTable(self) -> dict[Any, Any]:
		"""
		Get the position of the viewer as a table

		Returns:
		x = table[1]
		y = table[2]
		z = table[3]

		Returns:
			pos (dict[Any, Any])
		"""
		...

	def GetRot(self) -> int | int | int:
		"""
		Get the rotation angles of the view

		Returns:
			x (int)
			y (int)
			z (int)
		"""
		...

	def GetRotTable(self) -> dict[Any, Any]:
		"""
		Get the rotation angles of the view as a table

		Returns:
		x = table[1]
		y = table[2]
		z = table[3]

		Returns:
			rot (dict[Any, Any])
		"""
		...

	def GetScale(self) -> int:
		"""
		Get the scale (zoom) of the view

		Returns:
			scale (int)
		"""
		...

	def IsCheckerEnabled(self) -> None:
		...

	def IsLUTEnabled(self) -> None:
		...

	def LoadFile(self, filename: str) -> None:
		"""
		Load and display the contents of a file

		Args:
			filename (str)
		"""
		...

	def Redraw(self) -> None:
		"""
		Refreshes the viewer
		"""
		...

	def ResetView(self) -> None:
		"""
		Resets the display to default position etc
		"""
		...

	def SaveFile(self, filename: str) -> None:
		"""
		Save the currently displayed parameter

		Args:
			filename (str)
		"""
		...

	def SetAlphaOverlayColor(self, color: int) -> None:
		"""
		Select which alpha overlay to use

		0 = None, 1 = Red, 2 = Green, 3 = Yellow, 4 = Blue, 5 = Cyan, 6 = Magenta, 7 = White.

		Args:
			color (int)
		"""
		...

	def SetAspectCorrection(self, enable: bool) -> None:
		"""
		Enables or disables aspect correction

		Args:
			enable (bool)
		"""
		...

	def SetChannel(self, channel: int, toggle: bool) -> None:
		"""
		Select which channel to show

		When "toggle" is true, the first SetChannel(CHAN_Z) call will set the viewer to Z, while the second SetChannel(CHAN_Z) call will set the viewer to CHAN_COLOR

		Args:
			channel (int)
			toggle (bool)
		"""
		...

	def SetPos(self, x: int, y: int, z: int | None = None) -> bool:
		"""
		Set the position of the viewer

		Args:
			x (int)
			y (int)
			z (Optional[int])

		Returns:
			success (bool)
		"""
		...

	def SetRot(self, x: int, y: int, z: int) -> None:
		"""
		Set the rotation of the view

		Args:
			x (int)
			y (int)
			z (int)
		"""
		...

	def SetScale(self, scale: int) -> None:
		"""
		Set the scale (zoom) of the view
		Scale of 0 indicates Fit to View

		Args:
			scale (int)
		"""
		...

	def ShowControls(self, enable: bool) -> None:
		"""
		Shows or hides controls on the view

		Args:
			enable (bool)
		"""
		...

	def ShowGuides(self, enable: bool) -> None:
		"""
		Shows or hides guides on the view

		Args:
			enable (bool)
		"""
		...

