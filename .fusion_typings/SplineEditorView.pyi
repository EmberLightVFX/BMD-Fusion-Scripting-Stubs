from typing import Any, overload

from _non_existing import object_


class SplineEditorView_:

	#---Properties---#
	ZoomY: Any
	ZoomX: Any

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGB_ControlView: bool

	REGS_Name: str

	REGB_Unpredictable: bool

	REGS_UIName: str


	#---Methods---#
	def ZoomToRect(self) -> None:
		"""
		Zoom to Rectangle
		"""
		...
	def ZoomOut(self) -> None:
		"""
		Decreases the scale (zoom) of the view
		"""
		...
	def Paste(self, desttime: int, spline1: object_, spline2___: object_ = object_(), points: dict[Any, Any] = dict[Any, Any]()) -> bool:
		"""
		Paste points to given splines at given time from the Clipboard
		"""
		...
	def GetClipboard(self) -> tuple[dict[Any, Any], str]:
		"""
		Retrieves the tool(s) on the clipboard, as tables and as ASCII text.
		"""
		...
	def SetGuides(self, guides: dict[Any, Any] = dict[Any, Any](), rem_prev: bool = bool()) -> None:
		"""
		Sets snapguide
		"""
		...
	def DeleteGuides(self, start: int = int(), end: int = int()) -> None:
		"""
		Deletes guides between start and end
		"""
		...
	def GetGuides(self, start: int = int(), end: int = int()) -> dict[Any, Any]:
		"""
		Returns a table of snapguide times & names
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
		"""
		...
	def header_text(self) -> None:
		...
	def InZoomToRectMode(self) -> bool:
		"""
		Use TimeStretch
		"""
		...
	def ZoomIn(self) -> None:
		"""
		Increases the scale (zoom) of the view
		"""
		...
	def ZoomFit(self) -> None:
		"""
		Changes scale to fit all displayed splines within the view
		"""
		...

SplineEditorView = SplineEditorView_