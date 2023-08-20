from typing import Any

from Tool import Tool_


class FlowView_:

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGB_ControlView: bool

	REGS_Name: str

	REGB_Unpredictable: bool

	REGS_UIName: str


	#---Methods---#
	def GetBookmarkList(self) -> list[str]:
		"""
		Returns a list of all bookmarks
		"""
		...
	def GetBookmark(self, name_or_index: int | str) -> dict[Any, Any]:
		"""
		Retrives bookmark information
		"""
		...
	def ManageBookmarks(self) -> None:
		"""
		Manage bookmarks
		"""
		...
	def GoToBookmark(self, index_or_name_or_bookmark: int | str | dict[Any, Any]) -> None:
		"""
		Jumps to a bookmark
		"""
		...
	def DeleteBookmark(self, index_or_name: int | str) -> None:
		"""
		Deletes an existing bookmark
		"""
		...
	def InsertBookmark(self, index: int = int(), name: str = str(), x: int = int(), y: int = int(), scale: int = int()) -> None:
		"""
		Adds a bookmark
		"""
		...
	def FlushSetPosQueue(self) -> None:
		"""
		Moves all tools queued for positioning with QueueSetPos
		"""
		...
	def GetScale(self) -> int:
		"""
		Returns the current scale of the contents
		"""
		...
	def SetPos(self, tool: Tool_, x: int, y: int) -> None:
		"""
		Moves a tool to a new position
		"""
		...
	def header_text(self) -> None:
		...
	def GetPosTable(self, tool: Tool_) -> dict[Any, Any]:
		"""
		Returns the position of a tool as a table

		Returns:
					 number x = table[1]
					 number y = table[2]
		"""
		...
	def GetPos(self, Tool: Tool_) -> tuple[int, int]:
		"""
		Returns the position of a tool
		"""
		...
	def Select(self, tool: Tool_, select: bool = bool()) -> None:
		"""
		Selects or deselects a tool
		"""
		...
	def FrameAll(self) -> None:
		...
	def SetScale(self, scale: int) -> None:
		"""
		Change the scale of the contents
		"""
		...
	def QueueSetPos(self, tool: Tool_, x: int, y: int) -> None:
		"""
		Queues the moving of a tool to a new position
		"""
		...
	def SetBookmarkList(self, bookmarks: dict[Any, Any]) -> None:
		"""
		Sets the complete list of bookmarks
		"""
		...

FlowView = FlowView_