from typing import Literal

class _GammaTable:

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
	def InitTable(self, _gain: float, _gamma: float) -> None:
		...
	def info_text(self):
		...
	def InitTableFlt(self, _gain: float, _gamma: float) -> None:
		...
	def InitNoTable(self, _gain: float, _gamma: float) -> None:
		...
	def header_text(self):
		...
	def Lookup(self, x: int) -> int:
		...
	def LookupFlt(self, x: float) -> float:
		...
	def GammaTable(self) -> _GammaTable:
		"""
		GammaTable constructor
		"""
		...

GammaTable = _GammaTable