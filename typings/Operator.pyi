from typing import Any, overload, Literal

from FusionDoc import _FusionDoc
from Composition import _Composition
from Parameter import _Parameter
from Output import _Output
from Input import _Input
from SubInputs import _SubInputs
from TagList import _TagList
from Request import _Request
from TimeRegion import _TimeRegion
from _non_existing import _Tool, _TimeStamp


class _Operator:

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
	ParentTool: _Tool
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
	Document: _FusionDoc
	"""
	Read Only
	"""
	Composition: _Composition
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
	def GetInput(self, id: str, time: int = int()) -> int | str | _Parameter:
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
	def FindMainOutput(self, index: int) -> _Output:
		"""
		Returns the tool's main (visible) output

		Arguments:
			index	- Output index value of 1 or greater
		"""
		...
	def FindMainInput(self, index: int) -> _Input:
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
	def FindInput(self, name: str) -> _Input:
		...
	def FindOutput(self, name: str) -> _Output:
		...
	def FindSubInputs(self, name: str) -> _SubInputs:
		...
	def GetNextKeyTime(self, t: _TimeStamp) -> _TimeStamp:
		...
	def AddOutput(self, name: str, id: str, tags: _TagList) -> _Output:
		...
	def AddSeparator(self, id: str, tags: _TagList) -> _Input:
		...
	def AddSpacer(self, id: str, tags: _TagList) -> _Input:
		...
	def AddSubInputs(self, subid: str, tags: _TagList) -> _SubInputs:
		...
	def GetData(self, name: str = str()) -> int | str | bool | dict[Any, Any]:
		"""
		Get custom persistent data
		"""
		...
	def BeginControlNest(self, name: str, id: str, expand: bool, tags: _TagList) -> _Input:
		...
	def GetPrevKeyTime(self, t: _TimeStamp) -> _TimeStamp:
		...
	def SetData(self, name: str, value: int | str | bool | dict[Any, Any]) -> None:
		"""
		Set custom persistent data
		"""
		...
	def GetSourceTool(self, name: str) -> _Operator:
		...
	def GetKeyFrames(self) -> dict[Any, Any]:
		"""
		Return a table of all keyframe times for this tool
		"""
		...
	def IsGPUEnabled(self, req: _Request) -> bool:
		...
	def RemoveControlPage(self, name: str) -> bool:
		...
	def SetProgress(self, prog: float) -> bool:
		...
	def ConnectInput(self, input: str, target: _Tool | _Output | None) -> bool:
		"""
		Connect or disconnect an Input

		Arguments:
			input	- ID of the input to be connected/disconnected
			target	- Tool or Output to connect the Input to, or nil to disconnect
		"""
		...
	def info_text(self):
		...
	def SetRegion(self, tr: _TimeRegion) -> None:
		...
	def _AddInput(self, name: str, id: str, tags: _TagList) -> _Input:
		...
	def StartUndo(self, name: str) -> None:
		...
	def GetRegion(self) -> _TimeRegion:
		...
	def UpdateControls(self) -> None:
		...
	def EndControlNest(self) -> None:
		...
	def AddControlPage(self, name: str, tags: _TagList) -> int:
		...
	def _CloneInput(self, from_: _Input, id: str, tags: _TagList) -> _Input:
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
	def SetInput(self, id: str, value: int | str | _Parameter, time: int) -> None:
		"""
		Sets the value of an input at a given time

		Arguments:
			inputID	- ID of input
			value	- number, string or Parameter object to set
			time	- keyframe to set (not required for non-animated inputs)
		"""
		...

Operator = _Operator