from _non_existing import ViewShadeNodeGroup
from Image import Image
from Matrix4 import Matrix4
from TagList import TagList
from Vector3f import Vector3f

class ViewShadeNode:

    #---Properties---#
    NumResources: int
    """
    Read Only
    """

    NumUniforms: int
    """
    Read Only
    """


    #---Methods---#
    def _SetParamBool(self, idx: int, val: bool) -> None:
        ...

    def _SetParamImg(self, idx: int, img: Image, _chan: int, tags: TagList) -> None:
        ...

    def _SetParamMat4(self, idx: int, mat: Matrix4) -> None:
        ...

    def _SetParamNums1(self, idx: int, x: float) -> None:
        ...

    def _SetParamNums2(self, idx: int, x: float, y: float) -> None:
        ...

    def _SetParamNums3(self, idx: int, x: float, y: float, z: float) -> None:
        ...

    def _SetParamNums4(self, idx: int, x: float, y: float, z: float, w: float) -> None:
        ...

    def _SetParamVec3f(self, idx: int, vec: Vector3f) -> None:
        ...

    def __new(self, group: ViewShadeNodeGroup, name: str, params: str, code: str) -> ViewShadeNode:
        """
        ViewShadeNode constructor

        Args:
            group (ViewShadeNodeGroup)
            name (str)
            params (str)
            code (str)

        Returns:
            ViewShadeNode
        """
        ...

