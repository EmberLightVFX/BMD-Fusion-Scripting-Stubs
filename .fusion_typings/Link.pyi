from typing import Any

from Operator import Operator_
from Tool import Tool_


class Link_:

	#---Properties---#
	Owner: Operator_
	"""
	Read Only
	"""
	Name: str
	"""
	Friendly name of this Link

	Read Only
	"""
	ID: str
	"""
	ID of this Link

	Read Only
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
	def header_text(self) -> None:
		...
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
	def GetTool(self) -> Tool_:
		"""
		Returns the Tool object that owns this Link
		"""
		...

Link = Link_