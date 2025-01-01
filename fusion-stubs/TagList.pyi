from RefObject import RefObject
from _non_existing import Tag, void


class TagList:

	#---Methods---#
	def _Get_ID(self, tag: Tag, def_: str) -> str:
		...

	def _Get_Object(self, tag: Tag, def_: RefObject) -> RefObject:
		...

	def _Get_Ptr(self, tag: Tag, def_: void) -> None:
		...

	def _Get_String(self, tag: Tag, def_: str) -> str:
		...

	def _Get_TagList(self, tag: Tag, def_: TagList) -> TagList:
		...

	def _Get_float64(self, tag: Tag, def_: float) -> float:
		...

	def _Get_int32(self, tag: Tag, def_: int) -> int:
		...

	def _Get_uint32(self, tag: Tag, def_: int) -> int:
		...

	def _Set_ID(self, tag: Tag, val: str, addnew: bool) -> None:
		...

	def _Set_Object(self, tag: Tag, val: RefObject, addnew: bool) -> None:
		...

	def _Set_Ptr(self, tag: Tag, val: void, addnew: bool) -> None:
		...

	def _Set_PtrRaw(self, tag: Tag, val: void, addnew: bool) -> None:
		...

	def _Set_String(self, tag: Tag, val: str, addnew: bool) -> None:
		...

	def _Set_TagList(self, tag: Tag, val: TagList, addnew: bool) -> None:
		...

	def _Set_float64(self, tag: Tag, val: float, addnew: bool) -> None:
		...

	def _Set_int32(self, tag: Tag, val: int, addnew: bool) -> None:
		...

	def _Set_uint32(self, tag: Tag, val: int, addnew: bool) -> None:
		...

	def __new(self) -> TagList:
		"""
		TagList constructor

		Returns:
			TagList
		"""
		...

