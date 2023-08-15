from typing import Any, overload

from RenderJob import RenderJob_
from RenderNode import RenderNode_


class QueueManager_:

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
	def header_text(self) -> None:
		...
	def Stop(self) -> None:
		...
	def Start(self) -> None:
		...
	def RemoveJob(self, job: RenderJob_) -> None:
		"""
		Removes a job from the list
		"""
		...
	def NetJoinRender(self) -> None:
		...
	def UpdateItem(self) -> None:
		...
	def DeleteItem(self) -> None:
		...
	def AddItem(self) -> None:
		...
	def GetRootData(self) -> None:
		...
	def GetSchemaList(self) -> None:
		...
	def GetItemList(self) -> None:
		...
	def GetRenderNodeFromID(self) -> None:
		...
	def GetJobFromID(self) -> None:
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
	def GetJobs(self) -> None:
		...
	def GetRenderNodes(self) -> None:
		...
	def RemoveWatch(self) -> None:
		...
	def AddWatch(self) -> None:
		...
	def GetID(self) -> None:
		...
	def ScanForRenderNodes(self) -> None:
		"""
		Scans local network for new RenderNodes
		"""
		...
	def AddRenderNode(self, name: str, groups: str = str(), unused: bool = bool()) -> RenderNode_:
		"""
		Adds a RenderNode to the node list

		Arguments:
			 Name	 - the node's hostname or IP address
			 Groups - (optional) the render groups to join (default "all")
			 Unused - (optional) node will be added, but not used
		"""
		...
	@overload
	def RemoveRenderNode(self, node: RenderNode_) -> None:
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
	def MoveJob(self, job: RenderJob_, offset: int) -> None:
		"""
		Moves a job up or down the list

		Arguments:
				job		- the RenderJob to move
				offset - how far up or down the job list to move it
								 (negative offsets move the job up)
		"""
		...
	@overload
	def AddJob(self, filename: str, groups: str = str(), frames: str = str(), endscript: str = str()) -> RenderJob_:
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
	def AddJob(self, args: dict[Any, Any]) -> RenderJob_:
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
	def GetGroupList(self) -> list[Any]:
		"""
		Get a list of all node groups
		"""
		...
	def GetJobList(self) -> list[Any]:
		"""
		Get the list of jobs to render
		"""
		...
	def GetRenderNodeList(self) -> list[Any]:
		"""
		Get the list of available RenderNodes
		"""
		...

QueueManager = QueueManager_