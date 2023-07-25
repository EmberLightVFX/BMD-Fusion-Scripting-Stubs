from typing import Any

from Parameter import _Parameter


class _Parameter:

	#---Properties---#
	Metadata: Any
	"""
	Get or set metadata tables

	Read/Write
	"""
	ID: str
	"""
	ID of this Parameter

	Read Only
	"""
	Name: str
	"""
	Friendly name of this Parameter

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
	def SetData(self, name: str, value: int | str | bool | dict[Any, Any]) -> None:
		"""
		Set custom persistent data
		"""
		...
	def info_text(self):
		...
	def Copy(self) -> _Parameter:
		...
	def InterpolateWith(self, weight: float, param: _Parameter) -> _Parameter:
		...
	def GetData(self, name: str = str()) -> int | str | bool | dict[Any, Any]:
		"""
		Get custom persistent data
		"""
		...
	def header_text(self):
		...

Parameter = _Parameter