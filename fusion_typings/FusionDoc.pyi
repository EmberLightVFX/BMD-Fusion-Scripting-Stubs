from _non_existing import TimeStamp_


class FusionDoc_:

	#---Properties---#
	GlobalEnd: TimeStamp_
	"""
	Read Only
	"""
	GlobalStart: TimeStamp_
	"""
	Read Only
	"""
	Name: str
	"""
	Read Only
	"""
	HiQ: bool
	"""
	Read Only
	"""
	Filename: str
	"""
	Read Only
	"""
	LastFrameTime: float
	"""
	Read Only
	"""
	Locked: bool
	"""
	Read Only
	"""
	Proxy: bool
	"""
	Read Only
	"""
	TimeRemaining: float
	"""
	Read Only
	"""
	RenderEnd: TimeStamp_
	"""
	Read Only
	"""
	Rendering: bool
	"""
	Read Only
	"""
	AudioFilename: str
	"""
	Read Only
	"""
	RenderStep: int
	"""
	Read Only
	"""
	AudioOffset: TimeStamp_
	"""
	Read Only
	"""
	RenderStart: TimeStamp_
	"""
	Read Only
	"""
	AverageFrameTime: float
	"""
	Read Only
	"""
	RenderFlags: int
	"""
	Read Only
	"""
	CurrentTime: TimeStamp_
	"""
	Read Only
	"""
	ProxyScale: int
	"""
	Read Only
	"""
	ElapsedTime: float
	"""
	Read Only
	"""
	LastFrameRendered: TimeStamp_
	"""
	Read Only
	"""
	Modified: bool
	"""
	Read Only
	"""

	#---Methods---#
	def header_text(self) -> None:
		...
	def info_text(self) -> None:
		...
	def StartUndo(self, name: str) -> None:
		...
	def EndUndo(self, keep: bool) -> None:
		...

FusionDoc = FusionDoc_