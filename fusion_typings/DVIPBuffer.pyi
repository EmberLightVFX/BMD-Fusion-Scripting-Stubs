from Request import _Request
from Image import _Image


class _DVIPBuffer:

	#---Methods---#
	def header_text(self):
		...
	def info_text(self):
		...
	def DVIPBuffer(self, req: _Request, image: _Image, writable: bool) -> _DVIPBuffer:
		"""
		DVIPBuffer constructor
		"""
		...

DVIPBuffer = _DVIPBuffer