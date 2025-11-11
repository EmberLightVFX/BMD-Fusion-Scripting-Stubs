from typing import Any

from Tool import Tool

class FlowView:

    #---Registry---#
    REGI_ClassType: int

    REGB_ControlView: bool

    REGB_Hide: bool

    REGS_ID: str

    REGS_Name: str

    REGI_Priority: int

    REGB_SupportsDoD: bool

    REGS_UIName: str

    REGB_Unpredictable: bool

    REGI_Version: int

    REGS_VersionString: str


    #---Methods---#
    def DeleteBookmark(self, index_or_name: int | str) -> None:
        """
        Deletes an existing bookmark

        Args:
            index|name (number_or_string)
        """
        ...

    def FlushSetPosQueue(self) -> None:
        """
        Moves all tools queued for positioning with QueueSetPos
        """
        ...

    def FrameAll(self) -> None:
        ...

    def GetBookmark(self, name_or_index: int | str) -> dict[Any, Any]:
        """
        Retrives bookmark information

        Args:
            name|index (number_or_string)

        Returns:
            bookmark (dict[Any, Any])
        """
        ...

    def GetBookmarkList(self) -> list[str]:
        """
        Returns a list of all bookmarks

        Returns:
            bookmarks (list[str])
        """
        ...

    def GetPos(self, Tool: Tool) -> int | int:
        """
        Returns the position of a tool

        Args:
            Tool (Tool)

        Returns:
            x (int)
            y (int)
        """
        ...

    def GetPosTable(self, tool: Tool) -> dict[Any, Any]:
        """
        Returns the position of a tool as a table

        Returns:
        number x = table[1]
        number y = table[2]

        Args:
            tool (Tool)

        Returns:
            pos (dict[Any, Any])
        """
        ...

    def GetScale(self) -> int:
        """
        Returns the current scale of the contents

        Returns:
            scale (int)
        """
        ...

    def GoToBookmark(self, index_or_name_or_bookmark: int | str | dict[Any, Any]) -> None:
        """
        Jumps to a bookmark

        Args:
            index|name|bookmark (number_or_string_or_table)
        """
        ...

    def InsertBookmark(self, index: int | None = None, name: str | None = None, x: int | None = None, y: int | None = None, scale: int | None = None) -> None:
        """
        Adds a bookmark

        Args:
            index (Optional[int])
            name (Optional[str])
            x (Optional[int])
            y (Optional[int])
            scale (Optional[int])
        """
        ...

    def ManageBookmarks(self) -> None:
        """
        Manage bookmarks
        """
        ...

    def QueueSetPos(self, tool: Tool, x: int, y: int) -> None:
        """
        Queues the moving of a tool to a new position

        Args:
            tool (Tool)
            x (int)
            y (int)
        """
        ...

    def Select(self, tool: Tool, select: bool | None = None) -> None:
        """
        Selects or deselects a tool

        Args:
            tool (Tool)
            select (Optional[bool])
        """
        ...

    def SetBookmarkList(self, bookmarks: dict[Any, Any]) -> None:
        """
        Sets the complete list of bookmarks

        Args:
            bookmarks (dict[Any, Any])
        """
        ...

    def SetPos(self, tool: Tool, x: int, y: int) -> None:
        """
        Moves a tool to a new position

        Args:
            tool (Tool)
            x (int)
            y (int)
        """
        ...

    def SetScale(self, scale: int) -> None:
        """
        Change the scale of the contents

        Args:
            scale (int)
        """
        ...

