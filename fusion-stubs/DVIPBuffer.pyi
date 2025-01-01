from Request import Request
from Image import Image


class DVIPBuffer:

	#---Methods---#
	def __new(self, req: Request, image: Image, writable: bool) -> DVIPBuffer:
		"""
		DVIPBuffer constructor

		Args:
			req (Request)
			image (Image)
			writable (bool)

		Returns:
			DVIPBuffer
		"""
		...

