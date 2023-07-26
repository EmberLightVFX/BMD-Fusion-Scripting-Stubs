from typing import Literal

from Image import _Image


class _OCLMemory:

	#---Methods---#
	def OCLMemory(self) -> _OCLMemory:
		"""
		OCLMemory constructor
		"""
		...
	def info_text(self):
		...
	def ObtainCLObject(self, wait: bool) -> bool:
		...
	def header_text(self):
		...
	def Release(self) -> bool:
		...
	def Download(self, img: _Image) -> bool:
		...
	def ReleaseCLObject(self) -> bool:
		...

OCLMemory = _OCLMemory