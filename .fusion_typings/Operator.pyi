from typing import Any, overload

from Composition import Composition_
from FusionDoc import FusionDoc_
from Tool import Tool_
from TagList import TagList_
from Output import Output_
from Input import Input_
from SubInputs import SubInputs_
from PlainInput import PlainInput_
from Parameter import Parameter_
from TimeRegion import TimeRegion_
from Request import Request_
from _non_existing import TimeStamp_


class Operator_:

	#---Properties---#
	Comments: dict[int, str]
	"""
	Access the nodes comments field.

	Access using Comments[frame/TIME_UNDEFINED]

	Read/Write
	"""
	Composition: Composition_
	"""
	The composition that this tool belongs to

	Read Only
	"""
	Document: FusionDoc_
	"""
	Read Only
	"""
	FillColor: dict[Any, Any]
	"""
	Examples: tool.FillColor = { R=0.5, G=0.3, B=0.2}
					tool.FillColor = nil

	Read/Write
	"""
	ID: str
	"""
	The ID name of the node

	Read Only
	"""
	IsBeingLoaded: bool
	"""
	Read Only
	"""
	Name: str
	"""
	Friendly name of this tool

	Read Only
	"""
	Override: int
	"""
	Read/Write
	"""
	ParentTool: Tool_
	"""
	The parent tool of this tool

	Read Only
	"""
	ProgressCount: int
	"""
	Read/Write
	"""
	ProgressScale: int
	"""
	Read/Write
	"""
	Status: str
	"""
	Read Only
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
	UserControls: dict[Any, Any]
	"""
	Table of user-control definitions

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
	def AddControlPage(self, name: str, tags: TagList_) -> int:
		...
	def AddModifier(self, input: str, modifier: str) -> bool:
		"""
		Creates a modifier and connects it to an input

		Arguments:
			input	- ID of the input to be connected to
			modifier	- ID of the modifier to be created
		"""
		...
	def AddOutput(self, name: str, id: str, tags: TagList_) -> Output_:
		...
	def AddSeparator(self, id: str, tags: TagList_) -> Input_:
		...
	def AddSpacer(self, id: str, tags: TagList_) -> Input_:
		...
	def AddSubInputs(self, subid: str, tags: TagList_) -> SubInputs_:
		...
	def BeginControlNest(self, name: str, id: str, expand: bool, tags: TagList_) -> Input_:
		...
	def ConnectInput(self, input: str, target: Tool_ | Output_ | None) -> bool:
		"""
		Connect or disconnect an Input

		Arguments:
			input	- ID of the input to be connected/disconnected
			target	- Tool or Output to connect the Input to, or nil to disconnect
		"""
		...
	def Delete(self) -> None:
		"""
		Delete this tool
		"""
		...
	def EndControlNest(self) -> None:
		...
	def EndUndo(self, keep: bool) -> None:
		...
	def FindInput(self, name: str) -> Input_:
		...
	def FindMainInput(self, index: int) -> PlainInput_:
		"""
		Returns the tool's main (visible) input

		Arguments:
			index	- Input index value of 1 or greater
		"""
		...
	def FindMainOutput(self, index: int) -> Output_:
		"""
		Returns the tool's main (visible) output

		Arguments:
			index	- Output index value of 1 or greater
		"""
		...
	def FindOutput(self, name: str) -> Output_:
		...
	def FindSubInputs(self, name: str) -> SubInputs_:
		...
	@overload
	def GetAttrs(self, attribute_name: str) -> int | str | bool | dict[Any, Any] | list[Any]:
		"""
		Returns the content of an attributes

		You can get all attributes by not passing anything
		"""
		...
	@overload
	def GetAttrs(self) -> dict[Any, Any]:
		"""
		Returns the content of an attributes

		You can get all attributes by not passing anything
		"""
		...
	def GetChildrenList(self, selected: bool = bool(), regid: str = str()) -> list[Tool_]:
		"""
		Returns a list of all children tools, or selected children tools

		Arguments:
			 selected - pass 'true' to get only selected tools
			 RegID		- pass a Registry ID string to get only tools of that type
		"""
		...
	def GetControlPageNames(self) -> dict[Any, Any]:
		"""
		Returns a table of control page names

		Returns: table of control page names, indexed by page number
		"""
		...
	def GetCurrentSettings(self) -> int:
		"""
		Returns the index of the tool's current settings slot
		"""
		...
	def GetData(self, name: str = str()) -> int | str | bool | dict[Any, Any] | list[Any]:
		"""
		Get custom persistent data
		"""
		...
	def GetInput(self, id: str, time: int = int()) -> int | str | Parameter_:
		"""
		Fetches the value of an input at a given time

		Arguments:
			id	- ID of input
			time	- keyframe to fetch (not required for non-animated inputs)
		"""
		...
	def GetInputList(self, type: str = str()) -> dict[Any, Tool_]:
		"""
		Return a table of all inputs on this tool
		"""
		...
	def GetKeyFrames(self) -> dict[Any, Any]:
		"""
		Return a table of all keyframe times for this tool
		"""
		...
	def GetNextKeyTime(self, t: TimeStamp_) -> TimeStamp_:
		...
	def GetOutputList(self, type: str = str()) -> dict[Any, Tool_]:
		"""
		Return a table of all outputs on this tool
		"""
		...
	def GetPrevKeyTime(self, t: TimeStamp_) -> TimeStamp_:
		...
	def GetRegion(self) -> TimeRegion_:
		...
	def GetSourceTool(self, name: str) -> Operator_:
		...
	def IsGPUEnabled(self, req: Request_) -> bool:
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
	def Refresh(self) -> Tool_:
		"""
		Refreshes the tool, showing updated user controls

		Returns: handle to the new (refreshed) tool
		"""
		...
	def RemoveControlPage(self, name: str) -> bool:
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
	def SetAttrs(self, attributes: dict[Any, Any]) -> None:
		"""
		Set the content of an attributes
		"""
		...
	def SetCurrentSettings(self) -> int:
		"""
		Sets the tool's current settings slot
		"""
		...
	def SetData(self, name: str, value: int | str | bool | dict[Any, Any] | list[Any]) -> None:
		"""
		Set custom persistent data
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
	def SetProgress(self, prog: float) -> bool:
		...
	def SetRegion(self, tr: TimeRegion_) -> None:
		...
	def ShowControlPage(self, name: str) -> None:
		"""
		Makes the specified control page visible

		Arguments:
			name	- Control page to show
		"""
		...
	def StartUndo(self, name: str) -> None:
		...
	def UpdateControls(self) -> None:
		...
	def _AddInput(self, name: str, id: str, tags: TagList_) -> Input_:
		...
	def _CloneInput(self, from_: Input_, id: str, tags: TagList_) -> Input_:
		...
	def __getitem__(self, key: str) -> int | str | bool | dict[Any, Any] | list[Any]:
		...
	def header_text(self) -> None:
		...
	def info_text(self) -> None:
		...

Operator = Operator_