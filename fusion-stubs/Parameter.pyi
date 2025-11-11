from typing import Any

class Parameter:

    #---Properties---#
    ID: str
    """
    ID of this Parameter

    Read Only
    """

    Metadata: Any

    Name: str
    """
    Friendly name of this Parameter

    Read Only
    """

    Value: type
    """
    Value of this Parameter

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

    def SetData(self, name: str, value: int | str | bool | dict[Any, Any]) -> None:
        """
        Set custom persistent data

        Args:
            name (str)
            value ((number_or_string_or_boolean_or_table))
        """
        ...

    def Copy(self) -> Parameter:
        ...

    def InterpolateWith(self, weight: float, param: Parameter) -> Parameter:
        ...

