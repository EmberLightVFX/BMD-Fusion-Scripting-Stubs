from typing import Any, overload

from object import _object


class _SplineEditorView:

	#---Properties---#
	ZoomX: Any
	ZoomY: Any

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGS_VersionString: str

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_UIName: str

	REGS_ID: str

	REGB_ControlView: bool

	REGI_Priority: int


	#---Methods---#
	def ZoomToRect(self) -> None:
		"""
		Zoom to Rectangle
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
	def Paste(self, desttime: int, spline1: _object, spline2...: _object = _object(), points: dict[Any, Any] = dict[Any, Any]()) -> bool:
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
	def ZoomFit(self) -> None:
		"""
		Changes scale to fit all displayed splines within the view
		"""
		...
	def InZoomToRectMode(self) -> bool:
		"""
		Use TimeStretch
		"""
		...
	def header_text(self):
		...

SplineEditorView = _SplineEditorView