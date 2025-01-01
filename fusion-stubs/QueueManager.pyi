from typing import overload, Any

from RenderJob import RenderJob
from RenderNode import RenderNode


class QueueManager:

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
	def AddItem(self) -> None:
		...

	@overload
	def AddJob(self, filename: str, groups: str | None = None, frames: str | None = None, endscript: str | None = None) -> RenderJob:
		"""
		Adds a job to the list

		Arguments:
		Filename	Filename of comp or script to be queued
		Groups		RenderNode groups to assign the job to
		FrameRange	Range of frames to render
		EndScript	Script file to execute on completion
		Args		Table of named options, including:
		Filename, Groups, FrameRange, EndScript
		Start, End, QueuedBy, RenderStep, TimeOut

		Args:
			filename (str)
			groups (Optional[str])
			frames (Optional[str])
			endscript (Optional[str])

		Returns:
			job (RenderJob)
		"""
		...

	@overload
	def AddJob(self, args: dict[Any, Any]) -> RenderJob:
		"""
		Adds a job to the list

		Arguments:
		Filename	Filename of comp or script to be queued
		Groups		RenderNode groups to assign the job to
		FrameRange	Range of frames to render
		EndScript	Script file to execute on completion
		Args		Table of named options, including:
		Filename, Groups, FrameRange, EndScript
		Start, End, QueuedBy, RenderStep, TimeOut

		Args:
			args (dict[Any, Any])

		Returns:
			job (RenderJob)
		"""
		...

	def AddRenderNode(self, name: str, groups: str | None = None, unused: bool | None = None) -> RenderNode:
		"""
		Adds a RenderNode to the node list

		Arguments:
		Name   - the node's hostname or IP address
		Groups - (optional) the render groups to join (default "all")
		Unused - (optional) node will be added, but not used

		Args:
			name (str)
			groups (Optional[str])
			unused (Optional[bool])

		Returns:
			node (RenderNode)
		"""
		...

	def AddWatch(self) -> None:
		...

	def DeleteItem(self) -> None:
		...

	def GetGroupList(self) -> list[Any]:
		"""
		Get a list of all node groups

		Returns:
			groups (list[Any])
		"""
		...

	def GetID(self) -> None:
		...

	def GetItemList(self) -> None:
		...

	def GetJobFromID(self) -> None:
		...

	def GetJobList(self) -> list[Any]:
		"""
		Get the list of jobs to render

		Returns:
			jobs (list[Any])
		"""
		...

	def GetJobs(self) -> None:
		...

	def GetRenderNodeFromID(self) -> None:
		...

	def GetRenderNodeList(self) -> list[Any]:
		"""
		Get the list of available RenderNodes

		Returns:
			rendernodes (list[Any])
		"""
		...

	def GetRenderNodes(self) -> None:
		...

	def GetRootData(self) -> None:
		...

	def GetSchemaList(self) -> None:
		...

	def LoadQueue(self, filename: str) -> bool:
		"""
		Loads a list of jobs to do

		Args:
			filename (str)

		Returns:
			success (bool)
		"""
		...

	def LoadRenderNodeList(self, filename: str | None = None) -> bool:
		"""
		Loads a list of RenderNodes to use

		Arguments:
		filename - The file to load from (defaults to Queues:Slaves.slv)

		Args:
			filename (Optional[str])

		Returns:
			success (bool)
		"""
		...

	def Log(self, message: str) -> None:
		"""
		Writes a message to the Render Log

		Args:
			message (str)
		"""
		...

	def MoveJob(self, job: RenderJob, offset: int) -> None:
		"""
		Moves a job up or down the list

		Arguments:
		job    - the RenderJob to move
		offset - how far up or down the job list to move it
		(negative offsets move the job up)

		Args:
			job (RenderJob)
			offset (int)
		"""
		...

	def NetJoinRender(self) -> None:
		...

	def RemoveJob(self, job: RenderJob) -> None:
		"""
		Removes a job from the list

		Args:
			job (RenderJob)
		"""
		...

	@overload
	def RemoveRenderNode(self, node: RenderNode) -> None:
		"""
		Removes a RenderNode from the node list

		Arguments:
		node  - the node object, or its hostname or IP address

		Args:
			node (RenderNode)
		"""
		...

	@overload
	def RemoveRenderNode(self, node: str) -> None:
		"""
		Removes a RenderNode from the node list

		Arguments:
		node  - the node object, or its hostname or IP address

		Args:
			node (str)
		"""
		...

	def RemoveWatch(self) -> None:
		...

	def SaveQueue(self, filename: str) -> bool:
		"""
		Saves the current list of jobs

		Args:
			filename (str)

		Returns:
			success (bool)
		"""
		...

	def SaveRenderNodeList(self, filename: str | None = None) -> bool:
		"""
		Saves the current list of RenderNodes

		Arguments:
		filename - The file to save to (defaults to Queues:Slaves.slv)

		Args:
			filename (Optional[str])

		Returns:
			success (bool)
		"""
		...

	def ScanForRenderNodes(self) -> None:
		"""
		Scans local network for new RenderNodes
		"""
		...

	def Start(self) -> None:
		...

	def Stop(self) -> None:
		...

	def UpdateItem(self) -> None:
		...

