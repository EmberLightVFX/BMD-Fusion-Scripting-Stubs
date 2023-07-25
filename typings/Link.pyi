from typing import Any

from Operator import _Operator
from Tool import _Tool


class _Link:

	#---Properties---#
	Owner: _Operator
	"""
	Read Only
	"""
	ID: str
	"""
	ID of this Link

	Read Only
	"""
	Name: str
	"""
	Friendly name of this Link

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
	def GetData(self, name: str = str()) -> int | str | bool | dict[Any, Any]:
		"""
		Get custom persistent data
		"""
		...
	def GetTool(self) -> _Tool:
		"""
		Returns the Tool object that owns this Link
		"""
		...
	def header_text(self):
		...

Link = _Link