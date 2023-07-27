from typing import Any, overload

from Tool import Tool_
from FusionDoc import FusionDoc_
from Composition import Composition_
from Parameter import Parameter_
from Output import Output_
from Input import Input_
from SubInputs import SubInputs_
from TagList import TagList_
from Request import Request_
from TimeRegion import TimeRegion_
from _non_existing import TimeStamp_


class Operator_:

	#---Properties---#
	Status: str
	"""
	Read Only
	"""
	ProgressScale: int
	"""
	Read/Write
	"""
	Name: str
	"""
	Friendly name of this tool

	Read Only
	"""
	ProgressCount: int
	"""
	Read/Write
	"""
	ParentTool: Tool_
	"""
	The parent tool of this tool

	Read Only
	"""
	UserControls: dict[Any, Any]
	"""
	Table of user-control definitions

	Read/Write
	"""
	FillColor: dict[Any, Any]
	"""
			Examples: tool.FillColor = { R=0.5, G=0.3, B=0.2}
							tool.FillColor = nil

	Read/Write
	"""
	TextColor: dict[Any, Any]
	"""
	Color of a tool's icon text in the Flow view

			Examples: tool.TextColor = { R=0.5, G=0.3, B=0.2}
							tool.TextColor = nil

	Read/Write
	"""
	TileColor: dict[Any, Any]
	"""
	Color of a tool's icon in the Flow view

			Examples: tool.TileColor = { R=0.5, G=0.3, B=0.2}
							tool.TileColor = nil

	Read/Write
	"""
	IsBeingLoaded: bool
	"""
	Read Only
	"""
	ID: str
	"""
	Registry ID of this tool

	Read Only
	"""
	Document: FusionDoc_
	"""
	Read Only
	"""
	Composition: Composition_
	"""
	The composition that this tool belongs to

	Read Only
	"""
	Override: int
	"""
	Read/Write
	"""

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
	def GetInput(self, id: str, time: int = int()) -> int | str | Parameter_:
		"""
		Fetches the value of an input at a given time

		Arguments:
			id	- ID of input
			time	- keyframe to fetch (not required for non-animated inputs)
		"""
		...
	def GetChildrenList(self, selected: bool = bool(), regid: str = str()) -> dict[Any, Any]:
		"""
		Returns a list of all children tools, or selected children tools

		Arguments:
			 selected - pass 'true' to get only selected tools
			 RegID		- pass a Registry ID string to get only tools of that type
		"""
		...
	def GetOutputList(self, type: str = str()) -> dict[Any, Any]:
		"""
		Return a table of all outputs on this tool
		"""
		...
	def GetInputList(self, type: str = str()) -> dict[Any, Any]:
		"""
		Return a table of all inputs on this tool
		"""
		...
	def Delete(self) -> None:
		"""
		Delete this tool
		"""
		...
	def AddModifier(self, input: str, modifier: str) -> bool:
		"""
		Creates a modifier and connects it to an input

		Arguments:
			input	- ID of the input to be connected to
			modifier	- ID of the modifier to be created
		"""
		...
	def FindMainOutput(self, index: int) -> Output_:
		"""
		Returns the tool's main (visible) output

		Arguments:
			index	- Output index value of 1 or greater
		"""
		...
	def FindMainInput(self, index: int) -> Input_:
		"""
		Returns the tool's main (visible) input

		Arguments:
			index	- Input index value of 1 or greater
		"""
		...
	def Refresh(self) -> None:
		"""
		Refreshes the tool, showing updated user controls

		Returns: handle to the new (refreshed) tool
		"""
		...
	def ShowControlPage(self, name: str) -> None:
		"""
		Makes the specified control page visible

		Arguments:
			name	- Control page to show
		"""
		...
	def GetControlPageNames(self) -> dict[Any, Any]:
		"""
		Returns a table of control page names

		Returns: table of control page names, indexed by page number
		"""
		...
	def EndUndo(self, keep: bool) -> None:
		...
	def header_text(self):
		...
	def FindInput(self, name: str) -> Input_:
		...
	def FindOutput(self, name: str) -> Output_:
		...
	def FindSubInputs(self, name: str) -> SubInputs_:
		...
	def GetNextKeyTime(self, t: TimeStamp_) -> TimeStamp_:
		...
	def AddOutput(self, name: str, id: str, tags: TagList_) -> Output_:
		...
	def AddSeparator(self, id: str, tags: TagList_) -> Input_:
		...
	def AddSpacer(self, id: str, tags: TagList_) -> Input_:
		...
	def AddSubInputs(self, subid: str, tags: TagList_) -> SubInputs_:
		...
	def GetData(self, name: str = str()) -> int | str | bool | dict[Any, Any]:
		"""
		Get custom persistent data
		"""
		...
	def BeginControlNest(self, name: str, id: str, expand: bool, tags: TagList_) -> Input_:
		...
	def GetPrevKeyTime(self, t: TimeStamp_) -> TimeStamp_:
		...
	def SetData(self, name: str, value: int | str | bool | dict[Any, Any]) -> None:
		"""
		Set custom persistent data
		"""
		...
	def GetSourceTool(self, name: str) -> Operator_:
		...
	def GetKeyFrames(self) -> dict[Any, Any]:
		"""
		Return a table of all keyframe times for this tool
		"""
		...
	def IsGPUEnabled(self, req: Request_) -> bool:
		...
	def RemoveControlPage(self, name: str) -> bool:
		...
	def SetProgress(self, prog: float) -> bool:
		...
	def ConnectInput(self, input: str, target: Tool_ | Output_ | None) -> bool:
		"""
		Connect or disconnect an Input

		Arguments:
			input	- ID of the input to be connected/disconnected
			target	- Tool or Output to connect the Input to, or nil to disconnect
		"""
		...
	def info_text(self):
		...
	def SetRegion(self, tr: TimeRegion_) -> None:
		...
	def _AddInput(self, name: str, id: str, tags: TagList_) -> Input_:
		...
	def StartUndo(self, name: str) -> None:
		...
	def GetRegion(self) -> TimeRegion_:
		...
	def UpdateControls(self) -> None:
		...
	def EndControlNest(self) -> None:
		...
	def AddControlPage(self, name: str, tags: TagList_) -> int:
		...
	def _CloneInput(self, from_: Input_, id: str, tags: TagList_) -> Input_:
		...
	def SetCurrentSettings(self) -> int:
		"""
		Sets the tool's current settings slot
		"""
		...
	def GetCurrentSettings(self) -> int:
		"""
		Returns the index of the tool's current settings slot
		"""
		...
	@overload
	def SaveSettings(self, filename: str) -> bool:
		"""
		Save the tool's current settings to a file or table
		"""
		...
	@overload
	def SaveSettings(self, customdata: bool) -> dict[Any, Any]:
		"""
		Save the tool's current settings to a file or table
		"""
		...
	@overload
	def LoadSettings(self, filename: str) -> bool:
		"""
		Load the tools's settings from a file or table
		"""
		...
	@overload
	def LoadSettings(self, settings: dict[Any, Any]) -> bool:
		"""
		Load the tools's settings from a file or table
		"""
		...
	def SetInput(self, id: str, value: int | str | Parameter_, time: int) -> None:
		"""
		Sets the value of an input at a given time

		Arguments:
			inputID	- ID of input
			value	- number, string or Parameter object to set
			time	- keyframe to set (not required for non-animated inputs)
		"""
		...

Operator = Operator_