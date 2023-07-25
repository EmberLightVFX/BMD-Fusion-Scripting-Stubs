from ExtRef ExtRefvoid ptr import _ExtRef ExtRefvoid ptr
from TagList tags import _TagList tags


class _ExtRef:

	#---Methods---#
	def info_text(self):
		...
	def ExtRef(self) -> tuple[_ExtRef ExtRefvoid ptr, _TagList tags]:
		"""
		ExtRef constructor
		"""
		...
	def header_text(self):
		...

ExtRef = _ExtRef