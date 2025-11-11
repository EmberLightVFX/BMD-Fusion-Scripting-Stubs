from typing import Any

from _non_existing import time

class MediaIn:

    #---Registry---#
    REGS_Category: str

    REGI_ClassType: int

    REGB_ControlView: bool

    REGS_FileName: str

    REGS_HelpTopic: str

    REGB_Hide: bool

    REGS_ID: str

    REGS_Name: str

    REGI_Priority: int

    REGB_SupportsDoD: bool

    REGB_Unpredictable: bool

    REGI_Version: int

    REGS_VersionString: str


    #---Methods---#
    def GetMarkers(self, timestamp: time | None = None) -> list:
        """
        Returns a table of media markers.

        This returns a list of media markers, each with a table/dict of attributes.

        Args:
            timestamp (Optional[time])

        Returns:
            marker data (list)
        """
        ...

    def SetMarker(self, timestamp: int, marker_data: dict[Any, Any]) -> None:
        """
        Creates or changes a media marker.

        This will add or overwrite a media marker. Pass a table/dict of attributes, or nil to delete the marker.

        Args:
            timestamp (int)
            marker data (dict[Any, Any])
        """
        ...

