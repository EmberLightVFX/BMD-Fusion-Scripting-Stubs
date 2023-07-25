from typing import Any

class _BinItem:

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
	def Delete(self) -> None:
		"""
		Delete the BinItem
		"""
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
	def header_text(self):
		...

BinItem = _BinItem