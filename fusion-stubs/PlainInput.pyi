from typing import Any, overload

from Output import Output
from PlainOutput import PlainOutput

class PlainInput:

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
    @overload
    def ConnectTo(self) -> bool:
        """
        Connect the Input to an Output

        Returns:
            success (bool)
        """
        ...

    @overload
    def ConnectTo(self, out: Output) -> bool:
        """
        Connect the Input to an Output

        Args:
            out (Output)

        Returns:
            success (bool)
        """
        ...

    def GetConnectedOutput(self) -> PlainOutput | None:
        """
        Returns the output that this input is connected to

        Returns:
            out (PlainOutput | None)
        """
        ...

    def GetExpression(self) -> None:
        ...

    def GetKeyFrames(self) -> dict[Any, Any]:
        """
        Return a table of all keyframe times for this input

        Returns:
            keyframes (dict[Any, Any])
        """
        ...

    def HideViewControls(self, hide: bool) -> None:
        """
        Hides or shows the view controls for this input

        Args: Hide - 'true' (default) will hide the controls, 'false' will show them.
        Hides/Shows can be nested.

        Args:
            hide (bool)
        """
        ...

    def HideWindowControls(self, hide: bool) -> None:
        """
        Hides or shows the window controls for this input

        Args: Hide - 'true' (default) will hide the controls, 'false' will show them.
        Hides/Shows can be nested.

        Args:
            hide (bool)
        """
        ...

    def SetExpression(self) -> None:
        ...

    def ViewControlsVisible(self) -> bool:
        """
        Returns the visible state of the view controls for this input

        Returns:
            hidden (bool)
        """
        ...

    def WindowControlsVisible(self) -> bool:
        """
        Returns the visible state of the window controls for this input

        Returns:
            hidden (bool)
        """
        ...

