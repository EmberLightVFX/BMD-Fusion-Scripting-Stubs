from LayoutObj import LayoutObj


class ScriptLayoutManager:

	#---Methods---#
	def Layout(self, x: int, y: int, w: int, h: int) -> None:
		...

	def __new(self, root: LayoutObj) -> ScriptLayoutManager:
		"""
		ScriptLayoutManager constructor

		Args:
			root (LayoutObj)

		Returns:
			ScriptLayoutManager
		"""
		...

