from typing import Any, overload

from Composition import _Composition
from FusionDoc import _FusionDoc
from Tool import _Tool
from Output import _Output
from Input import _Input
from Request import _Request
from TimeRegion import _TimeRegion
from TagList import _TagList
from Operator import _Operator
from TimeStamp import _TimeStamp
from SubInputs import _SubInputs
from Parameter import _Parameter


class _Operator:

	#---Properties---#
	Composition: _Composition
	"""
	The composition that this tool belongs to

	Read Only
	"""
	ProgressScale: int
	"""
	Read/Write
	"""
	ProgressCount: int
	"""
	Read/Write
	"""
	Status: str
	"""
	Read Only
	"""
	Document: _FusionDoc
	"""
	Read Only
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
	ID: str
	"""
	Registry ID of this tool

	Read Only
	"""
	IsBeingLoaded: bool
	"""
	Read Only
	"""
	TileColor: dict[Any, Any]
	"""
	Color of a tool's icon in the Flow view

			Examples: tool.TileColor = { R=0.5, G=0.3, B=0.2}
							tool.TileColor = nil

	Read/Write
	"""
	Override: int
	"""
	Read/Write
	"""
	Name: str
	"""
	Friendly name of this tool

	Read Only
	"""

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
	def IsGPUEnabled(self, req: _Request) -> bool:
		...
	def RemoveControlPage(self, name: str) -> bool:
		...
	def header_text(self):
		...
	def SetRegion(self, tr: _TimeRegion) -> None:
		...
	def GetKeyFrames(self) -> dict[Any, Any]:
		"""
		Return a table of all keyframe times for this tool
		"""
		...
	def UpdateControls(self) -> None:
		...
	def _CloneInput(self, from: _Input, id: str, tags: _TagList) -> _Input:
		...
	def info_text(self):
		...
	def EndUndo(self, keep: bool) -> None:
		...
	def StartUndo(self, name: str) -> None:
		...
	def AddControlPage(self, name: str, tags: _TagList) -> int:
		...
	def _AddInput(self, name: str, id: str, tags: _TagList) -> _Input:
		...
	def SetProgress(self, prog: float) -> bool:
		...
	def GetSourceTool(self, name: str) -> _Operator:
		...
	def GetRegion(self) -> _TimeRegion:
		...
	def GetPrevKeyTime(self, t: _TimeStamp) -> _TimeStamp:
		...
	def GetNextKeyTime(self, t: _TimeStamp) -> _TimeStamp:
		...
	def FindSubInputs(self, name: str) -> _SubInputs:
		...
	def GetData(self, name: str = str()) -> int | str | bool | dict[Any, Any]:
		"""
		Get custom persistent data
		"""
		...
	def SetData(self, name: str, value: int | str | bool | dict[Any, Any]) -> None:
		"""
		Set custom persistent data
		"""
		...
	def GetInput(self, id: str, time: int = int()) -> int | str | _Parameter:
		"""
		Fetches the value of an input at a given time

		Arguments:
			id	- ID of input
			time	- keyframe to fetch (not required for non-animated inputs)
		"""
		...
	def AddSpacer(self, id: str, tags: _TagList) -> _Input:
		...
	def AddSeparator(self, id: str, tags: _TagList) -> _Input:
		...
	def AddSubInputs(self, subid: str, tags: _TagList) -> _SubInputs:
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
	def ConnectInput(self, input: str, target: _Tool | _Output | None) -> bool:
		"""
		Connect or disconnect an Input

		Arguments:
			input	- ID of the input to be connected/disconnected
			target	- Tool or Output to connect the Input to, or nil to disconnect
		"""
		...
	def BeginControlNest(self, name: str, id: str, expand: bool, tags: _TagList) -> _Input:
		...
	def AddOutput(self, name: str, id: str, tags: _TagList) -> _Output:
		...
	def SetCurrentSettings(self) -> int:
		"""
		Sets the tool's current settings slot
		"""
		...
	def EndControlNest(self) -> None:
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
	def FindInput(self, name: str) -> _Input:
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
	def FindOutput(self, name: str) -> _Output:
		...

Operator = _Operator