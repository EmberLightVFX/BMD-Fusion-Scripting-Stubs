from typing import overload, Any

from Composition import Composition
from Request import Request
from SubInputs import SubInputs
from Tool import Tool
from Parameter import Parameter
from TagList import TagList
from Output import Output
from TimeRegion import TimeRegion
from PlainInput import PlainInput
from FusionDoc import FusionDoc
from Input import Input
from _non_existing import TimeStamp


class Operator:

	#---Properties---#
	Composition: Composition
	"""
	The composition that this tool belongs to

	Read Only
	"""

	FillColor: dict[Any, Any]
	"""
	Examples: tool.FillColor = { R=0.5, G=0.3, B=0.2}
	tool.FillColor = nil

	"""

	ID: str
	"""
	Registry ID of this tool

	Read Only
	"""

	Name: str
	"""
	Friendly name of this tool

	Read Only
	"""

	ParentTool: Tool
	"""
	The parent tool of this tool

	Read Only
	"""

	TextColor: dict[Any, Any]
	"""
	Color of a tool's icon text in the Flow view

	Examples: tool.TextColor = { R=0.5, G=0.3, B=0.2}
	tool.TextColor = nil

	"""

	TileColor: dict[Any, Any]
	"""
	Color of a tool's icon in the Flow view

	Examples: tool.TileColor = { R=0.5, G=0.3, B=0.2}
	tool.TileColor = nil

	"""

	UserControls: dict[Any, Any]
	"""
	Table of user-control definitions

	"""

	Document: FusionDoc
	"""
	Read Only
	"""

	IsBeingLoaded: bool
	"""
	Read Only
	"""

	Override: int

	ProgressCount: int

	ProgressScale: int

	Status: str
	"""
	Read Only
	"""

	Comments: dict[int,str]
	"""
	Access the nodes comments field.

	Access using Comments[frame/TIME_UNDEFINED]

	"""

	ID: str
	"""
	The ID name of the node

	Read Only
	"""


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
	def AddModifier(self, input: str, modifier: str) -> bool:
		"""
		Creates a modifier and connects it to an input

		Arguments:
		input	- ID of the input to be connected to
		modifier	- ID of the modifier to be created

		Args:
			input (str)
			modifier (str)

		Returns:
			success (bool)
		"""
		...

	def ConnectInput(self, input: str, target: Tool | Output | None) -> bool:
		"""
		Connect or disconnect an Input

		Arguments:
		input	- ID of the input to be connected/disconnected
		target	- Tool or Output to connect the Input to, or nil to disconnect

		Args:
			input (str)
			target ((Tool_or_Output_or_nil))

		Returns:
			success (bool)
		"""
		...

	def Delete(self) -> None:
		"""
		Delete this tool
		"""
		...

	def FindMainInput(self, index: int) -> PlainInput:
		"""
		Returns the tool's main (visible) input

		Arguments:
		index	- Input index value of 1 or greater

		Args:
			index (int)

		Returns:
			inp (PlainInput)
		"""
		...

	def FindMainOutput(self, index: int) -> Output:
		"""
		Returns the tool's main (visible) output

		Arguments:
		index	- Output index value of 1 or greater

		Args:
			index (int)

		Returns:
			out (Output)
		"""
		...

	def GetChildrenList(self, selected: bool | None = None, regid: str | None = None) -> list[Tool]:
		"""
		Returns a list of all children tools, or selected children tools

		Arguments:
		selected - pass 'true' to get only selected tools
		RegID    - pass a Registry ID string to get only tools of that type

		Args:
			selected (Optional[bool])
			regid (Optional[str])

		Returns:
			tools (list[Tool])
		"""
		...

	def GetControlPageNames(self) -> dict[Any, Any]:
		"""
		Returns a table of control page names

		Returns: table of control page names, indexed by page number

		Returns:
			names (dict[Any, Any])
		"""
		...

	def GetCurrentSettings(self) -> int:
		"""
		Returns the index of the tool's current settings slot

		Returns:
			index (int)
		"""
		...

	def GetData(self, name: str | None = None) -> (int|str|bool|dict[Any, Any]):
		"""
		Get custom persistent data

		Args:
			name (Optional[str])

		Returns:
			value ((number_or_string_or_boolean_or_table))
		"""
		...

	def GetInput(self, id: str, time: int | None = None) -> (int|str|Parameter):
		"""
		Fetches the value of an input at a given time

		Arguments:
		id	- ID of input
		time	- keyframe to fetch (not required for non-animated inputs)

		Args:
			id (str)
			time (Optional[int])

		Returns:
			value ((number_or_string_or_Parameter))
		"""
		...

	def GetInputList(self, type: str | None = None) -> dict[Any, Tool]:
		"""
		Return a table of all inputs on this tool

		Args:
			type (Optional[str])

		Returns:
			inputs (dict[Any, Tool])
		"""
		...

	def GetKeyFrames(self) -> dict[Any, Any]:
		"""
		Return a table of all keyframe times for this tool

		Returns:
			keyframes (dict[Any, Any])
		"""
		...

	def GetOutputList(self, type: str | None = None) -> dict[Any, Tool]:
		"""
		Return a table of all outputs on this tool

		Args:
			type (Optional[str])

		Returns:
			outputs (dict[Any, Tool])
		"""
		...

	@overload
	def LoadSettings(self, filename: str) -> bool:
		"""
		Load the tools's settings from a file or table

		Args:
			filename (str)

		Returns:
			success (bool)
		"""
		...

	@overload
	def LoadSettings(self, settings: dict[Any, Any]) -> bool:
		"""
		Load the tools's settings from a file or table

		Args:
			settings (dict[Any, Any])

		Returns:
			success (bool)
		"""
		...

	def Refresh(self) -> None:
		"""
		Refreshes the tool, showing updated user controls

		Returns: handle to the new (refreshed) tool
		"""
		...

	def ResetEnabledRegion(self) -> None:
		"""
		Sets the tool's enabled region trimming
		"""
		...

	@overload
	def SaveSettings(self, filename: str) -> bool:
		"""
		Save the tool's current settings to a file or table

		Args:
			filename (str)

		Returns:
			success (bool)
		"""
		...

	@overload
	def SaveSettings(self, customdata: bool) -> dict[Any, Any]:
		"""
		Save the tool's current settings to a file or table

		Args:
			customdata (bool)

		Returns:
			settings (dict[Any, Any])
		"""
		...

	def SetCurrentSettings(self) -> int:
		"""
		Sets the tool's current settings slot

		Returns:
			index (int)
		"""
		...

	def SetData(self, name: str, value: int | str | bool | dict[Any, Any]) -> None:
		"""
		Set custom persistent data

		Args:
			name (str)
			value ((number_or_string_or_boolean_or_table))
		"""
		...

	def SetInput(self, id: str, value: int | str | Parameter, time: int) -> None:
		"""
		Sets the value of an input at a given time

		Arguments:
		inputID	- ID of input
		value	- number, string or Parameter object to set
		time	- keyframe to set (not required for non-animated inputs)

		Args:
			id (str)
			value ((number_or_string_or_Parameter))
			time (int)
		"""
		...

	def ShowControlPage(self, name: str) -> None:
		"""
		Makes the specified control page visible

		Arguments:
		name	- Control page to show

		Args:
			name (str)
		"""
		...

	def AddControlPage(self, name: str, tags: TagList) -> int:
		...

	def AddOutput(self, name: str, id: str, tags: TagList) -> Output:
		...

	def AddSeparator(self, id: str, tags: TagList) -> Input:
		...

	def AddSpacer(self, id: str, tags: TagList) -> Input:
		...

	def AddSubInputs(self, subid: str, tags: TagList) -> SubInputs:
		...

	def BeginControlNest(self, name: str, id: str, expand: bool, tags: TagList) -> Input:
		...

	def EndControlNest(self) -> None:
		...

	def EndUndo(self, keep: bool) -> None:
		...

	def FindInput(self, name: str) -> Input:
		...

	def FindOutput(self, name: str) -> Output:
		...

	def FindSubInputs(self, name: str) -> SubInputs:
		...

	def GetNextKeyTime(self, t: TimeStamp) -> TimeStamp:
		...

	def GetPrevKeyTime(self, t: TimeStamp) -> TimeStamp:
		...

	def GetRegion(self) -> TimeRegion:
		...

	def GetSourceTool(self, name: str) -> Operator:
		...

	def IsGPUEnabled(self, req: Request) -> bool:
		...

	def RemoveControlPage(self, name: str) -> bool:
		...

	def SetProgress(self, prog: float) -> bool:
		...

	def SetRegion(self, tr: TimeRegion) -> None:
		...

	def StartUndo(self, name: str) -> None:
		...

	def UpdateControls(self) -> None:
		...

	def _AddInput(self, name: str, id: str, tags: TagList) -> Input:
		...

	def _CloneInput(self, from_: Input, id: str, tags: TagList) -> Input:
		...

	@overload
	def GetAttrs(self, attribute_name: str) -> (int|str|bool|dict[Any, Any]):
		"""
		Returns the content of an attributes

		You can get all attributes by not passing anything

		Args:
			attribute_name (Optional[str])

		Returns:
			attribute_value (number_or_string_or_boolean_or_table)
		"""
		...

	@overload
	def GetAttrs(self) -> dict[Any, Any]:
		"""
		Returns the content of an attributes

		You can get all attributes by not passing anything

		Returns:
			all_attributes (dict[Any, Any])
		"""
		...

	def SetAttrs(self, attributes: dict[Any, Any]) -> None:
		"""
		Set the content of an attributes

		Args:
			attributes (dict[Any, Any])
		"""
		...

	def __getitem__(self, key: str) -> (int|str|bool|dict[Any, Any]):
		...

