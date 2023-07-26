from typing import Literal

from Image import _Image
from TagList import _TagList
from Matrix4 import _Matrix4
from Vector3f import _Vector3f
from _non_existing import _ViewShadeNodeGroup


class _ViewShadeNode:

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
	def ViewShadeNode(self, group: _ViewShadeNodeGroup, name: str, params: str, code: str) -> _ViewShadeNode:
		"""
		ViewShadeNode constructor
		"""
		...
	def _SetParamImg(self, idx: int, img: _Image, _chan: int, tags: _TagList) -> None:
		...
	def _SetParamMat4(self, idx: int, mat: _Matrix4) -> None:
		...
	def _SetParamVec3f(self, idx: int, vec: _Vector3f) -> None:
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

ViewShadeNode = _ViewShadeNode