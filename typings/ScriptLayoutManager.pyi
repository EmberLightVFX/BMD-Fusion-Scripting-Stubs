from LayoutObj import _LayoutObj


class _ScriptLayoutManager:

	#---Methods---#
	def header_text(self):
		...
	def info_text(self):
		...
	def Layout(self, x: int, y: int, w: int, h: int) -> None:
		...
	def ScriptLayoutManager(self, root: _LayoutObj) -> _ScriptLayoutManager:
		"""
		ScriptLayoutManager constructor
		"""
		...

ScriptLayoutManager = _ScriptLayoutManager