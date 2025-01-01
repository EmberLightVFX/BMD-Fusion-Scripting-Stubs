from Image import Image
from Request import Request


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

