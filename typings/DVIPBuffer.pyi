from DVIPBuffer DVIPBufferRequest req import _DVIPBuffer DVIPBufferRequest req
from Image image import _Image image
from boolean writable import _boolean writable


class _DVIPBuffer:

	#---Methods---#
	def info_text(self):
		...
	def DVIPBuffer(self) -> tuple[_DVIPBuffer DVIPBufferRequest req, _Image image, _boolean writable]:
		"""
		DVIPBuffer constructor
		"""
		...
	def header_text(self):
		...

DVIPBuffer = _DVIPBuffer