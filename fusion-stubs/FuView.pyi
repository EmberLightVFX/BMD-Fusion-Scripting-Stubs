from typing import Any, Literal

class FuView:

    #---Properties---#
    ID: Any


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
    def AddView(self, View_ID: str, Side: Literal["left", "right", "above", "below"]) -> None:
        """
        Add a new view to one side

        Args:
            View ID (str)
            Side: left, right, above, below (str)
        """
        ...

    def Refresh(self) -> None:
        """
        Redraw this view
        """
        ...

    def Remove(self) -> None:
        """
        Remove this view
        """
        ...

    def ShowTabs(self) -> None:
        """
        Show tabs for this view
        """
        ...

    def Undock(self) -> None:
        """
        Undock this view
        """
        ...

