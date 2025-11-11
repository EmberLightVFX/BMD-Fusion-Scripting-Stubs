from typing import Any

from Parameter import Parameter
from Tool import Tool

class PlainOutput:

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
    def ClearDiskCache(self, start: int, end: int) -> bool:
        """
        Clears frames from the disk cache

        Start..End: Frame range to clear from the cache (inclusive)

        Args:
            start (int)
            end (int)

        Returns:
            success (bool)
        """
        ...

    def EnableDiskCache(self, enable: bool | None = None, path: str | None = None, lockcache: bool | None = None, lockbranch: bool | None = None, delete: bool | None = None, prerender: bool | None = None, usenetwork: bool | None = None) -> bool | str:
        """
        Controls disk-based caching

        Args:
        Enable:     Enables or disables the cache
        Path:       Path to create the cache at
        LockCache:  Preserves the cache despite upstream changes (default false)
        LockBranch: Locks all upstream tools (default false)
        Delete:     Deletes the cache at <Path> (default false)
        PreRender:  Do a render now to create the cache (default true)
        UseNetwork: Use Network Rendering when PreRendering (default false)

        Args:
            enable (Optional[bool])
            path (Optional[str])
            lockcache (Optional[bool])
            lockbranch (Optional[bool])
            delete (Optional[bool])
            prerender (Optional[bool])
            usenetwork (Optional[bool])

        Returns:
            success (bool)
            path (str)
        """
        ...

    def GetConnectedInputs(self) -> None:
        ...

    def GetDoD(self, time: int | None = None, layer: str | None = None, flags: int | None = None, proxy: int | None = None) -> list[int] | None:
        """
        Returns the Domain of Definition at the given time

        Args:
        time:     The frame to fetch the DoD for (default is the current time).
        layer:    The layer to fetch the DoD for (default is the default layer).
        reqflags: Quality flags (default is final quality).
        proxy:    Proxy level (default is no proxy).

        Returns:
        may be nil, or a table containing { left,bottom,right,top } coords.

        Args:
            time (Optional[int])
            layer (Optional[str])
            flags (Optional[int])
            proxy (Optional[int])

        Returns:
            dod (list[int] | None)
        """
        ...

    def GetValue(self, time: int | None = None, layer: str | None = None, flags: int | None = None, proxy: int | None = None) -> Parameter | dict[Any, Any]:
        """
        Returns the value at the given time

        Args:
        time:     The frame to fetch the value for (default is the current time).
        layer:    The layer to fetch the value for (default is the default layer).
        reqflags: Quality flags (default is final quality).
        proxy:    Proxy level (default is no proxy).

        Returns:
        value may be nil, or a number of different types:
        Number - returns a number
        Point  - returns a table with X and Y members
        Text   - returns a string
        Clip   - returns the filename string
        Image  - returns an Image object
        attrs is a table with the following entries:
        Valid    - table with Start and End entries
        DataType - string ID for the parameter type
        TimeCost - time take to render this parameter
        DoD      - table of { left,bottom,right,top } coords

        Args:
            time (Optional[int])
            layer (Optional[str])
            flags (Optional[int])
            proxy (Optional[int])

        Returns:
            value (Parameter)
            attrs (dict[Any, Any])
        """
        ...

    def ShowDiskCacheDlg(self) -> bool:
        """
        Displays Cache-To-Disk dialog for user interaction

        Returns: boolean ok - true if user clicked OK/Pre-Render, false for Cancel

        Returns:
            success (bool)
        """
        ...

    def GetTool(self) -> Tool:
        """
        Get the tool that the output is pointing to

        You can get all attributes by not passing anything

        Returns:
            tool (Tool)
        """
        ...

