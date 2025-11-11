from Matrix4 import Matrix4
from Vector3f import Vector3f
from Vector4f import Vector4f

class Vector4:

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
    def Cross(self, vec: Vector4) -> Vector4:
        ...

    def Distance(self, vec: Vector4) -> float:
        ...

    def Dot3(self, vec: Vector4) -> Vector4:
        ...

    def Dot4(self, vec: Vector4) -> Vector4:
        ...

    def Length(self) -> float:
        ...

    def Normalize(self) -> None:
        ...

    def Scale(self, x: float, y: float, z: float, w: float) -> Vector4:
        ...

    def Set(self, x: float, y: float, z: float, w: float) -> None:
        ...

    def _LerpNum(self, vec: Vector4, t: float) -> Vector4:
        ...

    def _LerpVec4(self, vec: Vector4, t: Vector4) -> Vector4:
        ...

    def __add(self, vec: Vector4) -> Vector4:
        ...

    def __div(self, v: float) -> Vector4:
        ...

    def __eq(self, vec: Vector4) -> bool:
        ...

    def __sub(self, vec: Vector4) -> Vector4:
        ...

    def __unm(self) -> Vector4:
        ...

    def _mulMat4(self, mat: Matrix4) -> Vector4:
        ...

    def _mulNum(self, v: float) -> Vector4:
        ...

    def _newNums(self, x: float, y: float, z: float, w: float) -> Vector4:
        ...

    def _newVec3f(self, vec: Vector3f) -> Vector4:
        ...

    def _newVec4(self, vec: Vector4) -> Vector4:
        ...

    def _newVec4f(self, vec: Vector4f) -> Vector4:
        ...

