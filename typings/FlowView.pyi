from typing import Any

from object import _object


class _FlowView:

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGS_VersionString: str

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_UIName: str

	REGS_ID: str

	REGB_ControlView: bool

	REGI_Priority: int


	#---Methods---#
	def GetPos(self, Tool: _object) -> tuple[int, int]:
		"""
		Returns the position of a tool
		"""
		...
	def Select(self, tool: _object, select: bool = bool()) -> None:
		"""
		Selects or deselects a tool
		"""
		...
	def FrameAll(self):
		...
	def SetScale(self, scale: int) -> None:
		"""
		Change the scale of the contents
		"""
		...
	def GetScale(self) -> int:
		"""
		Returns the current scale of the contents
		"""
		...
	def header_text(self):
		...
	def SetBookmarkList(self, bookmarks: dict[Any, Any]) -> None:
		"""
		Sets the complete list of bookmarks
		"""
		...
	def GetBookmarkList(self) -> dict[Any, Any]:
		"""
		Returns a list of all bookmarks
		"""
		...
	def GetBookmark(self, name|index: int | str) -> dict[Any, Any]:
		"""
		Retrives bookmark information
		"""
		...
	def ManageBookmarks(self) -> None:
		"""
		Manage bookmarks
		"""
		...
	def GoToBookmark(self, index|name|bookmark: int | str | dict[Any, Any]) -> None:
		"""
		Jumps to a bookmark
		"""
		...
	def DeleteBookmark(self, index|name: int | str) -> None:
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
	def QueueSetPos(self, tool: _object, x: int, y: int) -> None:
		"""
		Queues the moving of a tool to a new position
		"""
		...
	def SetPos(self, tool: _object, x: int, y: int) -> None:
		"""
		Moves a tool to a new position
		"""
		...
	def GetPosTable(self, tool: _object) -> dict[Any, Any]:
		"""
		Returns the position of a tool as a table

		Returns:
					 number x = table[1]
					 number y = table[2]
		"""
		...

FlowView = _FlowView