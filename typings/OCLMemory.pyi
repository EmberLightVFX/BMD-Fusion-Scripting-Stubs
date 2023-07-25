from Image import _Image
from OCLMemory OCLMemory import _OCLMemory OCLMemory


class _OCLMemory:

	#---Methods---#
	def Download(self, img: _Image) -> bool:
		...
	def info_text(self):
		...
	def ObtainCLObject(self, wait: bool) -> bool:
		...
	def Release(self) -> bool:
		...
	def header_text(self):
		...
	def ReleaseCLObject(self) -> bool:
		...
	def OCLMemory(self) -> _OCLMemory OCLMemory:
		"""
		OCLMemory constructor
		"""
		...

OCLMemory = _OCLMemory