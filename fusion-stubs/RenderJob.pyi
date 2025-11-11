from typing import Any

from RenderNode import RenderNode

class RenderJob:

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
    def ClearCompletedFrames(self) -> None:
        """
        Clears the list of completed frames, restarting the render
        """
        ...

    def GetFailedSlaves(self) -> list[Any]:
        """
        Lists all slaves that failed this job

        Returns:
            failedslaves (list[Any])
        """
        ...

    def GetFrames(self) -> str:
        """
        Returns the total set of frames to be rendered

        Returns a string of frame numbers in the form '1..10,15,20'

        Returns:
            frames (str)
        """
        ...

    def GetRenderReport(self) -> None:
        ...

    def GetSlaveList(self) -> dict[Any, Any]:
        """
        Gets a table of slaves assigned to this job

        Returns:
            slaves (dict[Any, Any])
        """
        ...

    def GetUnrenderedFrames(self) -> str:
        """
        Returns the remaining frames to be rendered

        Returns a string of frame numbers in the form '1..10,15,20'

        Returns:
            frames (str)
        """
        ...

    def IsRendering(self) -> bool:
        """
        Returns true if job is currently rendering

        Returns:
            rendering (bool)
        """
        ...

    def RetryRenderNode(self, node: RenderNode | None = None) -> None:
        """
        Attempts to reuse slaves that have previously failed

        Arguments:
        node - the RenderNode object to retry
        If 'node' is not specified, all failed RenderNodes are retried

        Args:
            node (Optional[RenderNode])
        """
        ...

    def SetFrames(self, frames: str) -> None:
        """
        Specifies the set of frames to render

        Arguments:
        frames - a list in the form '1..10,15,20'

        Args:
            frames (str)
        """
        ...

    def _Heartbeat(self) -> None:
        ...

