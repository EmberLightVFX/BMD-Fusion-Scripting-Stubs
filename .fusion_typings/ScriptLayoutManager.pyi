from LayoutObj import LayoutObj_


class ScriptLayoutManager_:

	#---Methods---#
	def header_text(self) -> None:
		...
	def info_text(self) -> None:
		...
	def Layout(self, x: int, y: int, w: int, h: int) -> None:
		...
	def ScriptLayoutManager(self, root: LayoutObj_) -> ScriptLayoutManager_:
		"""
		ScriptLayoutManager constructor
		"""
		...

ScriptLayoutManager = ScriptLayoutManager_