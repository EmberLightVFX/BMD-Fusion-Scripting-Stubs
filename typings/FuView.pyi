from typing import Any

class _FuView:

	#---Properties---#
	ID: Any
	"""
	ID of this View

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
	def ShowTabs(self) -> None:
		"""
		Show tabs for this view
		"""
		...
	def AddView(self, View_ID: str, Side:_left: str, right, above, below) -> None:
		"""
		Add a new view to one side
		"""
		...
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
	def header_text(self):
		...

FuView = _FuView