from typing import Any

class UITimer_:

	#---Properties---#
	Interval: Any
	"""
	Read/Write
	"""
	IsActive: Any
	"""
	Read Only
	"""
	SingleShot: Any
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
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def GetIsActive(self) -> None:
		...
	def GetTimerID(self) -> None:
		...
	def GetRemainingTime(self) -> None:
		...
	def SetInterval(self) -> None:
		...
	def GetInterval(self) -> None:
		...
	def SetSingleShot(self) -> None:
		...
	def GetSingleShot(self) -> None:
		...
	def Stop(self) -> None:
		...
	def header_text(self) -> None:
		...
	def SetTimerType(self) -> None:
		...
	def GetTimerType(self) -> None:
		...
	def Start(self) -> None:
		...

UITimer = UITimer_