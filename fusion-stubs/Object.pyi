from typing import Any

from Registry import Registry
from FusionDoc import FusionDoc


class Object:

	#---Properties---#
	Comp: FusionDoc
	"""
	Read Only
	"""

	RegNode: Registry
	"""
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
	def Comp(self) -> None:
		...

	def Composition(self) -> None:
		...

	def DoAction(self) -> None:
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

	def GetID(self) -> None:
		...

	def GetReg(self) -> None:
		...

	def QueueAction(self) -> None:
		...

	def SetData(self, name: str, value: int | str | bool | dict[Any, Any]) -> None:
		"""
		Set custom persistent data

		Args:
			name (str)
			value ((number_or_string_or_boolean_or_table))
		"""
		...

	def TriggerEvent(self) -> None:
		...

	def GetComp(self) -> FusionDoc:
		...

