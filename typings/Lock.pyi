class _Lock:

	#---Properties---#
	TypeNamePtr: str
	"""
	Read Only
	"""
	TypeName: str
	"""
	Read Only
	"""

	#---Methods---#
	def ReleaseLock(self) -> None:
		...
	def info_text(self):
		...
	def ObtainLock(self) -> None:
		...
	def header_text(self):
		...

Lock = _Lock