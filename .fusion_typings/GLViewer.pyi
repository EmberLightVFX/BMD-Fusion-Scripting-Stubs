from typing import Any

class GLViewer_:

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
	def IsLUTEnabled(self) -> None:
		...
	def EnableLUT(self, enable: bool = bool()) -> None:
		...
	def IsCheckerEnabled(self) -> None:
		...
	def EnableChecker(self, enable: bool = bool()) -> None:
		"""
		Enables or disables drawing a checker underlay
		"""
		...
	def SaveFile(self, filename: str) -> None:
		"""
		Save the currently displayed parameter
		"""
		...
	def LoadFile(self, filename: str) -> None:
		"""
		Load and display the contents of a file
		"""
		...
	def AreGuidesShown(self) -> bool:
		"""
		Returns true if image guides are being displayed on the view
		"""
		...
	def header_text(self) -> None:
		...
	def AreControlsShown(self) -> bool:
		"""
		Returns true if controls are being displayed on the view
		"""
		...
	def ShowControls(self, enable: bool) -> None:
		"""
		Shows or hides controls on the view
		"""
		...
	def GetRotTable(self) -> dict[Any, Any]:
		"""
		Get the rotation angles of the view as a table

		Returns:
					 x = table[1]
					 y = table[2]
					 z = table[3]
		"""
		...
	def GetRot(self) -> tuple[int, int, int]:
		"""
		Get the rotation angles of the view
		"""
		...
	def GetAlphaOverlayColor(self) -> int:
		"""
		Return which alpha overlay is being used

		0 = None, 1 = Red, 2 = Green, 3 = Yellow, 4 = Blue, 5 = Cyan, 6 = Magenta, 7 = White.
		"""
		...
	def ResetView(self) -> None:
		"""
		Resets the display to default position etc
		"""
		...
	def GetChannel(self) -> int:
		"""
		Return which channel is shown
		"""
		...
	def SetChannel(self, channel: int, toggle: bool) -> None:
		"""
		Select which channel to show

		When "toggle" is true, the first SetChannel(CHAN_Z) call will set the viewer to Z, while the second SetChannel(CHAN_Z) call will set the viewer to CHAN_COLOR
		"""
		...
	def Redraw(self) -> None:
		"""
		Refreshes the viewer
		"""
		...
	def ShowGuides(self, enable: bool) -> None:
		"""
		Shows or hides guides on the view
		"""
		...
	def SetAlphaOverlayColor(self, color: int) -> None:
		"""
		Select which alpha overlay to use

		0 = None, 1 = Red, 2 = Green, 3 = Yellow, 4 = Blue, 5 = Cyan, 6 = Magenta, 7 = White.
		"""
		...
	def SetRot(self, x: int, y: int, z: int) -> None:
		"""
		Set the rotation of the view
		"""
		...
	def GetPosTable(self) -> dict[Any, Any]:
		"""
		Get the position of the viewer as a table

		Returns:
					 x = table[1]
					 y = table[2]
					 z = table[3]
		"""
		...
	def GetPos(self) -> tuple[int, int, int]:
		"""
		Get the position of the viewer
		"""
		...
	def SetPos(self, x: int, y: int, z: int = int()) -> bool:
		"""
		Set the position of the viewer
		"""
		...
	def SetAspectCorrection(self, enable: bool) -> None:
		"""
		Enables or disables aspect correction
		"""
		...
	def SetScale(self, scale: int) -> None:
		"""
		Set the scale (zoom) of the view
Scale of 0 indicates Fit to View
		"""
		...
	def GetAspectCorrection(self) -> bool:
		"""
		Returns true if the viewer is correcting the aspect of images
		"""
		...
	def GetScale(self) -> int:
		"""
		Get the scale (zoom) of the view
		"""
		...

GLViewer = GLViewer_