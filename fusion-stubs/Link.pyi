from typing import Any

from Operator import Operator
from Tool import Tool

class Link:

    #---Properties---#
    ID: str
    """
    ID of this Link

    Read Only
    """

    Name: str
    """
    Friendly name of this Link

    Read Only
    """

    Owner: Operator
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
    def GetData(self, name: str | None = None) -> (int|str|bool|dict[Any, Any]):
        """
        Get custom persistent data

        Args:
            name (Optional[str])

        Returns:
            value ((number_or_string_or_boolean_or_table))
        """
        ...

    def GetDefaultLayer(self) -> str:
        """
        Obtains the default layer name

        Returns:
            defaultlayer (str)
        """
        ...

    def GetLayerList(self) -> dict[Any, Any]:
        """
        Returns available layers

        Returns:
            layers (dict[Any, Any])
        """
        ...

    def GetTool(self) -> Tool:
        """
        Returns the Tool object that owns this Link

        Returns:
            tool (Tool)
        """
        ...

    def HasLayer(self, layername: str) -> bool:
        """
        Checks if a layer is available

        Args:
            layername (str)

        Returns:
            available (bool)
        """
        ...

    def SetData(self, name: str, value: int | str | bool | dict[Any, Any]) -> None:
        """
        Set custom persistent data

        Args:
            name (str)
            value ((number_or_string_or_boolean_or_table))
        """
        ...

    def IsConnected(self) -> bool:
        ...

