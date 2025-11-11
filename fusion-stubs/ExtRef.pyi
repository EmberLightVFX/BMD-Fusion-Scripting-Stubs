from _non_existing import void
from TagList import TagList

class ExtRef:

    #---Methods---#
    def __new(self, ptr: void, tags: TagList) -> ExtRef:
        """
        ExtRef constructor

        Args:
            ptr (void)
            tags (TagList)

        Returns:
            ExtRef
        """
        ...

