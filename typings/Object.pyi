from typing import Any

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
	def GetReg(self):
		...
	def GetID(self):
		...
	def Comp(self):
		...
	def DoAction(self):
		...
	def Composition(self):
		...
	def GetComp(self) -> _FusionDoc:
		...
	def info_text(self):
		...
	def header_text(self):
		...
	def QueueAction(self):
		...
	def TriggerEvent(self):
		...
	def GetData(self, name: str = str()) -> int | str | bool | dict[Any, Any]:
		"""
		Get custom persistent data
		"""
		...

Object = _Object