from Request import Request_
from Image import Image_


class DVIPBuffer_:

	#---Methods---#
	def header_text(self) -> None:
		...
	def info_text(self) -> None:
		...
	def DVIPBuffer(self, req: Request_, image: Image_, writable: bool) -> DVIPBuffer_:
		"""
		DVIPBuffer constructor
		"""
		...

DVIPBuffer = DVIPBuffer_