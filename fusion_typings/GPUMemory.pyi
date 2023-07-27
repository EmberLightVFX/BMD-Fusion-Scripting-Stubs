from Image import Image_


class GPUMemory_:

	#---Methods---#
	def header_text(self) -> None:
		...
	def info_text(self) -> None:
		...
	def Download(self, img: Image_) -> bool:
		...
	def GPUMemory(self) -> GPUMemory_:
		"""
		GPUMemory constructor
		"""
		...

GPUMemory = GPUMemory_