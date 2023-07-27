from Image import _Image


class _GPUMemory:

	#---Methods---#
	def header_text(self):
		...
	def info_text(self):
		...
	def Download(self, img: _Image) -> bool:
		...
	def GPUMemory(self) -> _GPUMemory:
		"""
		GPUMemory constructor
		"""
		...

GPUMemory = _GPUMemory