from Image import Image_


class OCLMemory_:

	#---Methods---#
	def OCLMemory(self) -> OCLMemory_:
		"""
		OCLMemory constructor
		"""
		...
	def info_text(self) -> None:
		...
	def ObtainCLObject(self, wait: bool) -> bool:
		...
	def header_text(self) -> None:
		...
	def Release(self) -> bool:
		...
	def Download(self, img: Image_) -> bool:
		...
	def ReleaseCLObject(self) -> bool:
		...

OCLMemory = OCLMemory_