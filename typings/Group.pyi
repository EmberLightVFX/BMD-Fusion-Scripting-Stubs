from typing import Literal

from TagList import _TagList


class _Group:

	#---Methods---#
	def header_text(self):
		...
	def info_text(self):
		...
	def Group(self, tags: _TagList) -> _Group:
		"""
		Group constructor
		"""
		...

Group = _Group