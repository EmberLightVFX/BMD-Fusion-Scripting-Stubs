from Point import Point


class PolyLine:

	#---Methods---#
	def CalcLength(self) -> None:
		...

	def GetCount(self) -> int:
		...

	def GetPoint(self, index: int) -> Point:
		...

	def GetPointOnPath(self, distance: float) -> Point:
		...

	def IsClosed(self) -> bool:
		...

