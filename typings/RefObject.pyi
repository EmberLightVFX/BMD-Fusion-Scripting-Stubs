from typing import Literal

from TagList import _TagList
from _non_existing import _Tag, _void


class _RefObject:

	#---Properties---#
	UseCount: int
	"""
	Read Only
	"""

	#---Methods---#
	def info_text(self):
		...
	def header_text(self):
		...
	def IncRef(self) -> None:
		...
	def DecRef(self) -> None:
		...
	def SetAttrsTagList(self, tags: _TagList) -> bool:
		...
	def _GetAttr_int32(self, tag: _Tag, def_: int) -> int:
		...
	def _GetAttr_uint32(self, tag: _Tag, def_: int) -> int:
		...
	def _GetAttr_float64(self, tag: _Tag, def_: float) -> float:
		...
	def _GetAttr_Ptr(self, tag: _Tag, def_: _void) -> None:
		...
	def _GetAttr_String(self, tag: _Tag, def_: str) -> str:
		...
	def _GetAttr_ID(self, tag: _Tag, def_: str) -> str:
		...
	def _GetAttr_bool(self, tag: _Tag, def_: bool) -> bool:
		...
	def _GetAttr_Object(self, tag: _Tag, def_: _RefObject) -> _RefObject:
		...
	def _GetAttr_TagList(self, tag: _Tag, def_: _TagList) -> _TagList:
		...

RefObject = _RefObject