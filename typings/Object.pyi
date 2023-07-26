from typing import Any, Literal

from Registry import _Registry
from FusionDoc import _FusionDoc


class _Object:

	#---Properties---#
	RegNode: _Registry
	"""
	Read Only
	"""
	Comp: _FusionDoc
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
	def QueueAction(self):
		...
	def GetData(self, name: str = str()) -> int | str | bool | dict[Any, Any]:
		"""
		Get custom persistent data
		"""
		...
	def GetReg(self):
		...
	def GetID(self):
		...
	def GetComp(self) -> _FusionDoc:
		...
	def Comp(self):
		...
	def info_text(self):
		...
	def TriggerEvent(self):
		...
	def header_text(self):
		...
	def DoAction(self):
		...
	def Composition(self):
		...
	def SetData(self, name: str, value: int | str | bool | dict[Any, Any]) -> None:
		"""
		Set custom persistent data
		"""
		...

Object = _Object