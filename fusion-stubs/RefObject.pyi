from TagList import TagList
from _non_existing import Tag, void


class RefObject:

	#---Properties---#
	UseCount: int
	"""
	Read Only
	"""


	#---Methods---#
	def DecRef(self) -> None:
		...

	def IncRef(self) -> None:
		...

	def SetAttrsTagList(self, tags: TagList) -> bool:
		...

	def _GetAttr_ID(self, tag: Tag, def_: str) -> str:
		...

	def _GetAttr_Object(self, tag: Tag, def_: RefObject) -> RefObject:
		...

	def _GetAttr_Ptr(self, tag: Tag, def_: void) -> None:
		...

	def _GetAttr_String(self, tag: Tag, def_: str) -> str:
		...

	def _GetAttr_TagList(self, tag: Tag, def_: TagList) -> TagList:
		...

	def _GetAttr_bool(self, tag: Tag, def_: bool) -> bool:
		...

	def _GetAttr_float64(self, tag: Tag, def_: float) -> float:
		...

	def _GetAttr_int32(self, tag: Tag, def_: int) -> int:
		...

	def _GetAttr_uint32(self, tag: Tag, def_: int) -> int:
		...

