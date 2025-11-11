from TagList import TagList

class ScriptObject:

    #---Properties---#
    TypeName: str
    """
    Read Only
    """

    TypeNamePtr: str
    """
    Read Only
    """


    #---Methods---#
    def _SetAttrs(self, tags: TagList) -> bool:
        ...

