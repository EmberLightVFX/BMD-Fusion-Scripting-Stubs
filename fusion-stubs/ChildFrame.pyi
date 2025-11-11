from typing import Any

from FuView import FuView

class ChildFrame:

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
    def ActivateFrame(self) -> None:
        """
        Activates this frame window
        """
        ...

    def ActivateNextFrame(self) -> None:
        """
        Activates the next frame window
        """
        ...

    def ActivatePrevFrame(self) -> None:
        """
        Activates the previous frame window
        """
        ...

    def GetControlViewList(self) -> list[FuView]:
        """
        Returns the list of views from the Controls tabs

        where 'table' is a table of the FuView objects in the Controls view tabs,and entries are named by the view's ID string.

        Returns:
            views (list[FuView])
        """
        ...

    def GetMainViewList(self) -> list[FuView]:
        """
        Returns the list of views from the Main tabs

        where 'views' is a table of the FuView objects in the Main view tabs,and entries are named by the view's ID string.

        Returns:
            views (list[FuView])
        """
        ...

    def GetViewLayout(self) -> dict[Any, Any]:
        """
        Retrieves the current view layout

        Returns a table describing the current view layout

        Returns:
            layout (dict[Any, Any])
        """
        ...

    def LoadLayout(self) -> None:
        ...

    def ResetLayout(self) -> None:
        ...

    def SaveLayout(self) -> None:
        ...

    def SetScreenLayout(self) -> None:
        ...

    def SetViewLayout(self, layout: dict[Any, Any]) -> bool:
        """
        Sets the current view layout from a table

        Args:  table describing the view layout

        Args:
            layout (dict[Any, Any])

        Returns:
            success (bool)
        """
        ...

    def SwitchControlView(self, id: str) -> None:
        """
        Displays a given view from the Control tabs

        where 'id' is the ID of one of the views in the Controls tab list.
        e.g. 'ControlView', 'ModifierView'

        Args:
            id (str)
        """
        ...

    def SwitchLayout(self) -> None:
        ...

    def SwitchMainView(self, id: str) -> None:
        """
        Displays a given view from the Main tabs

        where 'id' is the ID of one of the views in the Main tab list.
        e.g. 'FlowView', 'ConsoleView', 'TimelineView', 'SplineEditorView'

        Args:
            id (str)
        """
        ...

