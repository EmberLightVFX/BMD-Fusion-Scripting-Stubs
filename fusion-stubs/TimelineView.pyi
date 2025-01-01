from typing import Any, overload

class TimelineView:

	#---Properties---#

	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGS_UIName: str

	REGB_Unpredictable: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def DeleteGuides(self, start: int | None = None, end: int | None = None) -> None:
		"""
		Deletes guides between start and end

		Args:
			start (Optional[int])
			end (Optional[int])
		"""
		...

	def GetClipboard(self) -> dict[Any, Any] | str:
		"""
		Retrieves the tool(s) on the clipboard, as tables and as ASCII text.

		Returns:
			clipboard (dict[Any, Any])
			clipboard (str)
		"""
		...

	def GetGuides(self, start: int | None = None, end: int | None = None) -> dict[Any, Any]:
		"""
		Returns a table of snapguide times & names

		Args:
			start (Optional[int])
			end (Optional[int])

		Returns:
			guides (dict[Any, Any])
		"""
		...

	def GoNextKeyTime(self) -> None:
		"""
		Jumps to next key frame of the active spline
		"""
		...

	def GoPrevKeyTime(self) -> None:
		"""
		Jumps to previous key frame of the active spline
		"""
		...

	def InZoomToRectMode(self) -> bool:
		"""
		Use TimeStretch

		Returns:
			zoomrectMode (bool)
		"""
		...

	def Paste(self, desttime: int, spline1: object, spline2___: object | None = None, points: dict[Any, Any] | None = None) -> bool:
		"""
		Paste points to given splines at given time from the Clipboard

		Args:
			desttime (int)
			spline1 (object)
			spline2... (Optional[object])
			points (Optional[dict[Any, Any]])

		Returns:
			success (bool)
		"""
		...

	def SetGuides(self, guides: dict[Any, Any] | None = None, rem_prev: bool | None = None) -> None:
		"""
		Sets snapguide

		Args:
			guides (Optional[dict[Any, Any]])
			rem_prev (Optional[bool])
		"""
		...

	def ShowSortMenu(self) -> None:
		"""
		Zoom to Rectangle
		"""
		...

	def ZoomFit(self) -> None:
		"""
		Changes scale to fit all displayed splines within the view
		"""
		...

	def ZoomIn(self) -> None:
		"""
		Increases the scale (zoom) of the view
		"""
		...

	def ZoomOut(self) -> None:
		"""
		Decreases the scale (zoom) of the view
		"""
		...

	@overload
	def ZoomRectangle(self) -> None:
		"""
		Fill the view with the specified rectangle
		"""
		...

	@overload
	def ZoomRectangle(self, x1: int, y1: int, x2: int, y2: int) -> None:
		"""
		Fill the view with the specified rectangle

		Args:
			x1 (int)
			y1 (int)
			x2 (int)
			y2 (int)
		"""
		...

	def ZoomToRect(self) -> None:
		"""
		Zoom to Rectangle
		"""
		...

