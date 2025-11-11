from TagList import TagList

class LayoutObj:

    #---Properties---#
    m_PosX: int

    m_PosY: int

    m_SizeX: int

    m_SizeY: int


    #---Methods---#
    def __new(self, tags: TagList) -> LayoutObj:
        """
        LayoutObj constructor

        Args:
            tags (TagList)

        Returns:
            LayoutObj
        """
        ...

