from TagList import TagList_
from _non_existing import Tag_, void_


class RefObject_:

	#---Properties---#
	UseCount: int
	"""
	Read Only
	"""

	#---Methods---#
	def info_text(self) -> None:
		...
	def header_text(self) -> None:
		...
	def IncRef(self) -> None:
		...
	def DecRef(self) -> None:
		...
	def SetAttrsTagList(self, tags: TagList_) -> bool:
		...
	def _GetAttr_int32(self, tag: Tag_, def_: int) -> int:
		...
	def _GetAttr_uint32(self, tag: Tag_, def_: int) -> int:
		...
	def _GetAttr_float64(self, tag: Tag_, def_: float) -> float:
		...
	def _GetAttr_Ptr(self, tag: Tag_, def_: void_) -> None:
		...
	def _GetAttr_String(self, tag: Tag_, def_: str) -> str:
		...
	def _GetAttr_ID(self, tag: Tag_, def_: str) -> str:
		...
	def _GetAttr_bool(self, tag: Tag_, def_: bool) -> bool:
		...
	def _GetAttr_Object(self, tag: Tag_, def_: RefObject_) -> RefObject_:
		...
	def _GetAttr_TagList(self, tag: Tag_, def_: TagList_) -> TagList_:
		...

RefObject = RefObject_