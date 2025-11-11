from Matrix4 import Matrix4

class Vector3f:

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
    def Equals(self, vec: Vector3f) -> bool:
        ...

    def IsNaN(self) -> bool:
        ...

    def IsNormalized(self) -> bool:
        ...

    def IsZero(self, num: float) -> bool:
        ...

    def Length(self) -> float:
        ...

    def LengthSquared(self) -> float:
        ...

    def Normalize(self) -> None:
        ...

    def Project(self, vec: Vector3f) -> None:
        ...

    def __add(self, vec: Vector3f) -> Vector3f:
        ...

    def __div(self, num: float) -> Vector3f:
        ...

    def __eq(self, vec: Vector3f) -> bool:
        ...

    def __pow(self, vec: Vector3f) -> Vector3f:
        ...

    def __sub(self, vec: Vector3f) -> Vector3f:
        ...

    def __unm(self) -> Vector3f:
        ...

    def _mulMat4(self, mat: Matrix4) -> Vector3f:
        ...

    def _mulNum(self, num: float) -> Vector3f:
        ...

    def _newNums(self, x: float, y: float, z: float) -> Vector3f:
        ...

    def _newVec3f(self, vec: Vector3f) -> Vector3f:
        ...

