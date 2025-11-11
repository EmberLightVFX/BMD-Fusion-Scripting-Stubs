from typing import Any

from _non_existing import TimeStamp
from TimeExtent import TimeExtent

class TimeRegion:

    #---Properties---#
    End: int
    """
    Read Only
    """

    Start: int
    """
    Read Only
    """


    #---Registry---#
    REGI_ClassType: int

    REGB_ControlView: bool

    REGB_Hide: bool

    REGS_ID: str

    REGS_Name: str

    REGI_Priority: int

    REGB_SupportsDoD: bool

    REGB_Unpredictable: bool

    REGI_Version: int

    REGS_VersionString: str


    #---Methods---#
    def FromFrameString(self, frames: str) -> None:
        """
        Reads a string description

        Args:
            frames (str)
        """
        ...

    def FromTable(self, frames: dict[Any, Any]) -> None:
        """
        Reads a table of {start, end} pairs

        Args:
            frames (dict[Any, Any])
        """
        ...

    def ToFrameString(self) -> str:
        """
        Returns a string description

        Returns:
            frames (str)
        """
        ...

    def ToTable(self) -> dict[Any, Any]:
        """
        Returns a table of {start, end} pairs

        Returns:
            frames (dict[Any, Any])
        """
        ...

    def FromString(self, str: str) -> None:
        ...

    def IsEmpty(self) -> bool:
        ...

    def IsWithin(self, t: TimeStamp) -> bool:
        ...

    def ToString(self) -> str:
        ...

    def _IntersectExt(self, ext: TimeExtent) -> None:
        ...

    def _IntersectRgn(self, rgn: TimeRegion) -> None:
        ...

    def _UnionExt(self, ext: TimeExtent) -> None:
        ...

    def _UnionRgn(self, rgn: TimeRegion) -> None:
        ...

    def _newDef(self) -> TimeRegion:
        ...

    def _newNums(self, s: float, e: float, l: float) -> TimeRegion:
        ...

    def _newString(self, str: str) -> TimeRegion:
        ...

    def _newTR(self, tr: TimeRegion) -> TimeRegion:
        ...

