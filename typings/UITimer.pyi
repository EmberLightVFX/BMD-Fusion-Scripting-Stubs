from typing import Any

class _UITimer:

	#---Properties---#
	IsActive: Any
	"""
	Read Only
	"""
	SingleShot: Any
	"""
	Read/Write
	"""
	Interval: Any
	"""
	Read/Write
	"""
	RemainingTime: Any
	"""
	Read Only
	"""
	TimerID: Any
	"""
	Read Only
	"""
	TimerType: Any
	"""
	Read/Write
	"""

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGS_VersionString: str

	REGI_ClassType: int

	REGI_Priority: int

	REGB_ControlView: bool

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGB_Unpredictable: bool


	#---Methods---#
	def SetSingleShot(self) -> None:
		...
	def GetSingleShot(self) -> None:
		...
	def SetTimerType(self) -> None:
		...
	def GetTimerType(self) -> None:
		...
	def GetIsActive(self) -> None:
		...
	def GetTimerID(self) -> None:
		...
	def Stop(self) -> None:
		...
	def GetRemainingTime(self) -> None:
		...
	def Start(self) -> None:
		...
	def SetInterval(self) -> None:
		...
	def GetInterval(self) -> None:
		...
	def header_text(self):
		...

UITimer = _UITimer