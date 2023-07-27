from typing import Any

from RenderNode import RenderNode_


class RenderJob_:

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
	def GetSlaveList(self) -> dict[Any, Any]:
		"""
		Gets a table of slaves assigned to this job
		"""
		...
	def GetRenderReport(self):
		...
	def RetryRenderNode(self, node: RenderNode_ = RenderNode_()) -> None:
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
	def _Heartbeat(self):
		...
	def GetUnrenderedFrames(self) -> str:
		"""
		Returns the remaining frames to be rendered

		Returns a string of frame numbers in the form '1..10,15,20'
		"""
		...
	def IsRendering(self) -> bool:
		"""
		Returns true if job is currently rendering
		"""
		...
	def header_text(self):
		...
	def GetFrames(self) -> str:
		"""
		Returns the total set of frames to be rendered

		Returns a string of frame numbers in the form '1..10,15,20'
		"""
		...
	def SetFrames(self, frames: str) -> None:
		"""
		Specifies the set of frames to render

		Arguments:
				frames - a list in the form '1..10,15,20'
		"""
		...
	def GetFailedSlaves(self) -> dict[Any, Any]:
		"""
		Lists all slaves that failed this job
		"""
		...

RenderJob = RenderJob_