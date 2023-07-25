from typing import Any

from RenderNode import _RenderNode


class _RenderJob:

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
	def _Heartbeat(self):
		...
	def SetFrames(self, frames: str) -> None:
		"""
		Specifies the set of frames to render

		Arguments:
				frames - a list in the form '1..10,15,20'
		"""
		...
	def RetryRenderNode(self, node: _RenderNode = _RenderNode()) -> None:
		"""
		Attempts to reuse slaves that have previously failed

		Arguments:
				node - the RenderNode object to retry
		If 'node' is not specified, all failed RenderNodes are retried
		"""
		...
	def ClearCompletedFrames(self) -> None:
		"""
		Clears the list of completed frames, restarting the render
		"""
		...
	def GetUnrenderedFrames(self) -> str:
		"""
		Returns the remaining frames to be rendered

		Returns a string of frame numbers in the form '1..10,15,20'
		"""
		...
	def GetFrames(self) -> str:
		"""
		Returns the total set of frames to be rendered

		Returns a string of frame numbers in the form '1..10,15,20'
		"""
		...
	def GetRenderReport(self):
		...
	def GetFailedSlaves(self) -> dict[Any, Any]:
		"""
		Lists all slaves that failed this job
		"""
		...
	def GetSlaveList(self) -> dict[Any, Any]:
		"""
		Gets a table of slaves assigned to this job
		"""
		...
	def IsRendering(self) -> bool:
		"""
		Returns true if job is currently rendering
		"""
		...
	def header_text(self):
		...

RenderJob = _RenderJob