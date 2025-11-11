from typing import Any

class Registry:

    #---Properties---#
    ID: str
    """
    ID of this Registry node

    Read Only
    """

    Name: str
    """
    Friendly name of this Registry node

    Read Only
    """

    Parent: Registry
    """
    Parent of this Registry node

    Read Only
    """

    m_ClassFlags: int

    m_ClassType: int

    m_EnvID: int

    m_ID: str
    """
    Read Only
    """

    m_Name: str
    """
    Read Only
    """

    m_Parent: Registry
    """
    Read Only
    """

    m_RegFlags: int


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
    def IsClassType(self) -> bool:
        """
        Returns whether a tool's ID or any of its parent's IDs is a particular Registry ID

        Returns:
            matched (bool)
        """
        ...

    def IsRegClassType(self) -> bool:
        """
        Returns whether a tool is a particular Registry ClassType

        Returns:
            matched (bool)
        """
        ...

    def New(self, object_saved_settings: dict[Any, Any] | None = None) -> object:
        """
        Returns a new instance of this class type

        Args:
            object saved settings (Optional[dict[Any, Any]])

        Returns:
            instance (object)
        """
        ...

    def GetParent(self) -> Registry:
        ...

