from typing import Any

from Tool import Tool

class FuFrame:

    #---Properties---#
    Composition: Any
    """
    Represents this frame window's Composition

    The Composition variable represents the Composition object that thisframe window is displaying.

    Read Only
    """

    ConsoleView: Any
    """
    Represents this frame window's console

    The ConsoleView variable represents the FuView object used to displayany scripting message, and to allow script commands to be entered.

    Read Only
    """

    CurrentView: Any
    """
    Represents the currently active view for this frame window

    The CurrentView variable represents the currently active view for this frame window.

    Read Only
    """

    FlowView: Any
    """
    Represents this frame window's Flow view

    The FlowView variable represents the FuView object used to displaythe various tool connections for the frame's Composition.

    Read Only
    """

    InfoView: Any
    """
    Represents this frame window's Info view

    The InfoView variable represents the FuView object used to displayany general notes for the frame's Composition.

    Read Only
    """

    LeftView: Any
    """
    Represents this frame window's left display view

    The LeftView variable represents the left-hand GLView object used todisplay images, 3D scenes and other parameters output by a tool.

    Read Only
    """

    ModifierView: Any
    """
    Represents this frame window's Modifier controls view

    Read Only
    """

    RightView: Any
    """
    Represents this frame window's right display view

    The RightView variable represents the right-hand GLView object used todisplay images, 3D scenes and other parameters output by a tool.

    Read Only
    """

    SplineView: Any
    """
    Represents this frame window's spline editor view

    Read Only
    """

    TimeRulerView: Any
    """
    Represents this frame window's time ruler

    Read Only
    """

    TimelineView: Any
    """
    Represents this frame window's Timeline view

    Read Only
    """

    ToolView: Any
    """
    Represents this frame window's Tool controls view

    Read Only
    """

    TransportView: Any
    """
    Represents this frame window's transport controls view

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
    def GetPreviewList(self, include_globals: bool | None = None) -> dict[Any, Any]:
        """
        Retrieves a table of previews

        Args:
            include_globals (Optional[bool])

        Returns:
            previews (dict[Any, Any])
        """
        ...

    def GetViewList(self) -> dict[Any, Any]:
        """
        Returns the list of views within this frame

        where 'table' is a table of the FuView objects in the frame,
        and entries are named by the view's ID string.

        Returns:
            views (dict[Any, Any])
        """
        ...

    def SwitchView(self, id: str) -> None:
        """
        Displays a given view within this frame

        where 'id' is the ID of one of the views in the frame.
        e.g. 'FlowView', 'ConsoleView', 'TimelineView', 'SplineEditorView'

        Args:
            id (str)
        """
        ...

    def ViewOn(self, tool: Tool | None = None, view: int | None = None) -> None:
        """
        Displays a tool on a numbered view

        where 'view' is a number from 0..9.
        If 'tool' is omitted, the currently active tool is used.
        If 'tool' is nil, the view is cleared.
        If no arguments are supplied, all views are cleared.

        Args:
            tool (Optional[Tool])
            view (Optional[int])
        """
        ...

