from Image import Image_
from TagList import TagList_
from Matrix4 import Matrix4_
from Vector3f import Vector3f_
from _non_existing import ViewShadeNodeGroup_


class ViewShadeNode_:

	#---Properties---#
	NumUniforms: int
	"""
	Read Only
	"""
	NumResources: int
	"""
	Read Only
	"""

	#---Methods---#
	def info_text(self):
		...
	def _SetParamBool(self, idx: int, val: bool) -> None:
		...
	def ViewShadeNode(self, group: ViewShadeNodeGroup_, name: str, params: str, code: str) -> ViewShadeNode_:
		"""
		ViewShadeNode constructor
		"""
		...
	def _SetParamImg(self, idx: int, img: Image_, _chan: int, tags: TagList_) -> None:
		...
	def _SetParamMat4(self, idx: int, mat: Matrix4_) -> None:
		...
	def _SetParamVec3f(self, idx: int, vec: Vector3f_) -> None:
		...
	def _SetParamNums1(self, idx: int, x: float) -> None:
		...
	def header_text(self):
		...
	def _SetParamNums2(self, idx: int, x: float, y: float) -> None:
		...
	def _SetParamNums4(self, idx: int, x: float, y: float, z: float, w: float) -> None:
		...
	def _SetParamNums3(self, idx: int, x: float, y: float, z: float) -> None:
		...

ViewShadeNode = ViewShadeNode_