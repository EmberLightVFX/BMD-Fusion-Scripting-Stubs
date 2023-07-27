from typing import Any

class _Parameter:

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
	def SetData(self, name: str, value: int | str | bool | dict[Any, Any]) -> None:
		"""
		Set custom persistent data
		"""
		...
	def info_text(self):
		...
	def GetData(self, name: str = str()) -> int | str | bool | dict[Any, Any]:
		"""
		Get custom persistent data
		"""
		...
	def header_text(self):
		...
	def InterpolateWith(self, weight: float, param: _Parameter) -> _Parameter:
		...
	def Copy(self) -> _Parameter:
		...

Parameter = _Parameter