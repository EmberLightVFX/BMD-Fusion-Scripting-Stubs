from typing import Any, Literal

class FuView_:

	#---Properties---#
	ID: Any
	"""
	ID of this View

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
	def Undock(self) -> None:
		"""
		Undock this view
		"""
		...
	def Remove(self) -> None:
		"""
		Remove this view
		"""
		...
	def Refresh(self) -> None:
		"""
		Redraw this view
		"""
		...
	def header_text(self) -> None:
		...
	def ShowTabs(self) -> None:
		"""
		Show tabs for this view
		"""
		...
	def AddView(self, View_ID: str, Side: Literal["left", "right", "above", "below"]) -> None:
		"""
		Add a new view to one side
		"""
		...

FuView = FuView_