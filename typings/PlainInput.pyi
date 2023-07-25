from typing import Any, overload

from Output import _Output


class _PlainInput:

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_VersionString: str

	REGS_ID: str

	REGB_ControlView: bool

	REGI_Priority: int


	#---Methods---#
	def GetKeyFrames(self) -> dict[Any, Any]:
		"""
		Return a table of all keyframe times for this input
		"""
		...
	def GetExpression(self):
		...
	def SetExpression(self):
		...
	def WindowControlsVisible(self) -> bool:
		"""
		Returns the visible state of the window controls for this input
		"""
		...
	def HideWindowControls(self, hide: bool) -> None:
		"""
		Hides or shows the window controls for this input

		Args: Hide - 'true' (default) will hide the controls, 'false' will show them.
					Hides/Shows can be nested.
		"""
		...
	def ViewControlsVisible(self) -> bool:
		"""
		Returns the visible state of the view controls for this input
		"""
		...
	def HideViewControls(self, hide: bool) -> None:
		"""
		Hides or shows the view controls for this input

		Args: Hide - 'true' (default) will hide the controls, 'false' will show them.
					Hides/Shows can be nested.
		"""
		...
	def GetConnectedOutput(self) -> _Output:
		"""
		Returns the output that this input is connected to
		"""
		...
	@overload
	def ConnectTo(self) -> bool:
		"""
		Connect the Input to an Output
		"""
		...
	@overload
	def ConnectTo(self, out: _Output) -> bool:
		"""
		Connect the Input to an Output
		"""
		...
	def header_text(self):
		...

PlainInput = _PlainInput