from typing import Literal

class _Lock:

	#---Properties---#
	TypeName: str
	"""
	Read Only
	"""
	TypeNamePtr: str
	"""
	Read Only
	"""

	#---Methods---#
	def header_text(self):
		...
	def info_text(self):
		...
	def ObtainLock(self) -> None:
		...
	def ReleaseLock(self) -> None:
		...

Lock = _Lock