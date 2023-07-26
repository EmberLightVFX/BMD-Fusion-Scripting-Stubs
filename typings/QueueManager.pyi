from typing import Any, overload, Literal

from RenderJob import _RenderJob
from RenderNode import _RenderNode


class _QueueManager:

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
	def header_text(self):
		...
	def Stop(self):
		...
	def Start(self):
		...
	def RemoveJob(self, job: _RenderJob) -> None:
		"""
		Removes a job from the list
		"""
		...
	def NetJoinRender(self):
		...
	def UpdateItem(self):
		...
	def DeleteItem(self):
		...
	def AddItem(self):
		...
	def GetRootData(self):
		...
	def GetSchemaList(self):
		...
	def GetItemList(self):
		...
	def GetRenderNodeFromID(self):
		...
	def GetJobFromID(self):
		...
	def SaveRenderNodeList(self, filename: str = str()) -> bool:
		"""
		Saves the current list of RenderNodes

		Arguments:
			 filename - The file to save to (defaults to Queues:Slaves.slv)
		"""
		...
	def LoadRenderNodeList(self, filename: str = str()) -> bool:
		"""
		Loads a list of RenderNodes to use

		Arguments:
			 filename - The file to load from (defaults to Queues:Slaves.slv)
		"""
		...
	def GetJobs(self):
		...
	def GetRenderNodes(self):
		...
	def RemoveWatch(self):
		...
	def AddWatch(self):
		...
	def GetID(self):
		...
	def ScanForRenderNodes(self) -> None:
		"""
		Scans local network for new RenderNodes
		"""
		...
	def AddRenderNode(self, name: str, groups: str = str(), unused: bool = bool()) -> _RenderNode:
		"""
		Adds a RenderNode to the node list

		Arguments:
			 Name	 - the node's hostname or IP address
			 Groups - (optional) the render groups to join (default "all")
			 Unused - (optional) node will be added, but not used
		"""
		...
	@overload
	def RemoveRenderNode(self, node: _RenderNode) -> None:
		"""
		Removes a RenderNode from the node list

		Arguments:
			 node	- the node object, or its hostname or IP address
		"""
		...
	@overload
	def RemoveRenderNode(self, node: str) -> None:
		"""
		Removes a RenderNode from the node list

		Arguments:
			 node	- the node object, or its hostname or IP address
		"""
		...
	def Log(self, message: str) -> None:
		"""
		Writes a message to the Render Log
		"""
		...
	def MoveJob(self, job: _RenderJob, offset: int) -> None:
		"""
		Moves a job up or down the list

		Arguments:
				job		- the RenderJob to move
				offset - how far up or down the job list to move it
								 (negative offsets move the job up)
		"""
		...
	@overload
	def AddJob(self, filename: str, groups: str = str(), frames: str = str(), endscript: str = str()) -> _RenderJob:
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
		"""
		...
	@overload
	def AddJob(self, args: dict[Any, Any]) -> _RenderJob:
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
		"""
		...
	def SaveQueue(self, filename: str) -> bool:
		"""
		Saves the current list of jobs
		"""
		...
	def LoadQueue(self, filename: str) -> bool:
		"""
		Loads a list of jobs to do
		"""
		...
	def GetGroupList(self) -> dict[Any, Any]:
		"""
		Get a list of all node groups
		"""
		...
	def GetJobList(self) -> dict[Any, Any]:
		"""
		Get the list of jobs to render
		"""
		...
	def GetRenderNodeList(self) -> dict[Any, Any]:
		"""
		Get the list of available RenderNodes
		"""
		...

QueueManager = _QueueManager