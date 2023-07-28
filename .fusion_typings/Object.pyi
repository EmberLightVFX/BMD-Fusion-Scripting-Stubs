from typing import Any

from Registry import Registry_
from FusionDoc import FusionDoc_


class Object_:

	#---Properties---#
	RegNode: Registry_
	"""
	Read Only
	"""
	Comp: FusionDoc_
	"""
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
	def QueueAction(self) -> None:
		...
	def GetData(self, name: str = str()) -> int | str | bool | dict[Any, Any]:
		"""
		Get custom persistent data
		"""
		...
	def GetReg(self) -> None:
		...
	def GetID(self) -> None:
		...
	def GetComp(self) -> FusionDoc_:
		...
	def Comp(self) -> None:
		...
	def info_text(self) -> None:
		...
	def TriggerEvent(self) -> None:
		...
	def header_text(self) -> None:
		...
	def DoAction(self) -> None:
		...
	def Composition(self) -> None:
		...
	def SetData(self, name: str, value: int | str | bool | dict[Any, Any]) -> None:
		"""
		Set custom persistent data
		"""
		...

Object = Object_