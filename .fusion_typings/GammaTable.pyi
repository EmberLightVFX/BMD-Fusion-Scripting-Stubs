class GammaTable_:

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
	def info_text(self) -> None:
		...
	def InitTableFlt(self, _gain: float, _gamma: float) -> None:
		...
	def InitNoTable(self, _gain: float, _gamma: float) -> None:
		...
	def header_text(self) -> None:
		...
	def Lookup(self, x: int) -> int:
		...
	def LookupFlt(self, x: float) -> float:
		...
	def GammaTable(self) -> GammaTable_:
		"""
		GammaTable constructor
		"""
		...

GammaTable = GammaTable_