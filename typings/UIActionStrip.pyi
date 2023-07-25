from typing import Any

class _UIActionStrip:

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
	def AddEdit(self):
		...
	def AddButton(self):
		...
	def FindZone(self):
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
	def SetZonesPerSide(self) -> None:
		...
	def GetZonesPerSide(self) -> None:
		...
	def header_text(self):
		...
	def SetTarget(self):
		...
	def AddPopup(self):
		...
	def AddSlider(self):
		...

UIActionStrip = _UIActionStrip