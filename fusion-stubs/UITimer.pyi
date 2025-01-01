from typing import Any

class UITimer:

	#---Properties---#
	Interval: Any

	IsActive: Any
	"""
	Read Only
	"""

	RemainingTime: Any
	"""
	Read Only
	"""

	SingleShot: Any

	TimerID: Any
	"""
	Read Only
	"""

	TimerType: Any


	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGB_Utility_Toggle: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def GetInterval(self) -> None:
		...

	def GetIsActive(self) -> None:
		...

	def GetRemainingTime(self) -> None:
		...

	def GetSingleShot(self) -> None:
		...

	def GetTimerID(self) -> None:
		...

	def GetTimerType(self) -> None:
		...

	def SetInterval(self) -> None:
		...

	def SetSingleShot(self) -> None:
		...

	def SetTimerType(self) -> None:
		...

	def Start(self) -> None:
		...

	def Stop(self) -> None:
		...

