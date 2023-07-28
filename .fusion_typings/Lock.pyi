class Lock_:

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
	def header_text(self) -> None:
		...
	def info_text(self) -> None:
		...
	def ObtainLock(self) -> None:
		...
	def ReleaseLock(self) -> None:
		...

Lock = Lock_