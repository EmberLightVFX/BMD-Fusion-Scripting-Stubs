from GammaTable GammaTable import _GammaTable GammaTable


class _GammaTable:

	#---Properties---#
	TypeNamePtr: str
	"""
	Read Only
	"""
	TypeName: str
	"""
	Read Only
	"""

	#---Methods---#
	def InitTableFlt(self, _gain: float, _gamma: float) -> None:
		...
	def info_text(self):
		...
	def GammaTable(self) -> _GammaTable GammaTable:
		"""
		GammaTable constructor
		"""
		...
	def InitNoTable(self, _gain: float, _gamma: float) -> None:
		...
	def Lookup(self, x: int) -> int:
		...
	def LookupFlt(self, x: float) -> float:
		...
	def InitTable(self, _gain: float, _gamma: float) -> None:
		...
	def header_text(self):
		...

GammaTable = _GammaTable