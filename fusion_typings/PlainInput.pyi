from typing import Any, overload

from Output import Output_


class PlainInput_:

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
	def GetKeyFrames(self) -> dict[Any, Any]:
		"""
		Return a table of all keyframe times for this input
		"""
		...
	def header_text(self):
		...
	@overload
	def ConnectTo(self) -> bool:
		"""
		Connect the Input to an Output
		"""
		...
	@overload
	def ConnectTo(self, out: Output_) -> bool:
		"""
		Connect the Input to an Output
		"""
		...
	def GetConnectedOutput(self) -> Output_:
		"""
		Returns the output that this input is connected to
		"""
		...

PlainInput = PlainInput_