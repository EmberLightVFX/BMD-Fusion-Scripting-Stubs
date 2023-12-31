from typing import Any

class Parameter_:

	#---Properties---#
	Name: str
	"""
	Friendly name of this Parameter

	Read Only
	"""
	ID: str
	"""
	ID of this Parameter

	Read Only
	"""
	Metadata: Any
	"""
	Get or set metadata tables

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
	def SetData(self, name: str, value: int | str | bool | dict[Any, Any] | list[Any]) -> None:
		"""
		Set custom persistent data
		"""
		...
	def info_text(self) -> None:
		...
	def GetData(self, name: str = str()) -> int | str | bool | dict[Any, Any] | list[Any]:
		"""
		Get custom persistent data
		"""
		...
	def header_text(self) -> None:
		...
	def InterpolateWith(self, weight: float, param: Parameter_) -> Parameter_:
		...
	def Copy(self) -> Parameter_:
		...

Parameter = Parameter_