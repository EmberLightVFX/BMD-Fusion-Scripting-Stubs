from typing import Any

class UIActionStrip_:

	#---Properties---#
	ZonesPerSide: Any
	"""
	Read/Write
	"""
	ActionFlags: Any
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
	def AddPopup(self) -> None:
		...
	def AddSlider(self) -> None:
		...
	def AddEdit(self) -> None:
		...
	def AddButton(self) -> None:
		...
	def FindZone(self) -> None:
		...
	def GetNextID(self) -> None:
		...
	def Remove(self) -> None:
		...
	def EndZone(self) -> None:
		...
	def BeginZone(self) -> None:
		...
	def SetActionFlags(self) -> None:
		...
	def GetActionFlags(self) -> None:
		...
	def Update(self) -> None:
		...
	def header_text(self) -> None:
		...
	def GetZonesPerSide(self) -> None:
		...
	def SetZonesPerSide(self) -> None:
		...
	def SetTarget(self) -> None:
		...

UIActionStrip = UIActionStrip_