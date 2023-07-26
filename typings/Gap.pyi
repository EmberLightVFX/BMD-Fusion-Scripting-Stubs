from typing import Literal

from TagList import _TagList


class _Gap:

	#---Methods---#
	def header_text(self):
		...
	def info_text(self):
		...
	def Gap(self, tags: _TagList) -> _Gap:
		"""
		Gap constructor
		"""
		...

Gap = _Gap