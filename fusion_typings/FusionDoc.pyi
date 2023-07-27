from _non_existing import _TimeStamp


class _FusionDoc:

	#---Properties---#
	GlobalEnd: _TimeStamp
	"""
	Read Only
	"""
	GlobalStart: _TimeStamp
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
	RenderEnd: _TimeStamp
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
	AudioOffset: _TimeStamp
	"""
	Read Only
	"""
	RenderStart: _TimeStamp
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
	CurrentTime: _TimeStamp
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
	LastFrameRendered: _TimeStamp
	"""
	Read Only
	"""
	Modified: bool
	"""
	Read Only
	"""

	#---Methods---#
	def header_text(self):
		...
	def info_text(self):
		...
	def StartUndo(self, name: str) -> None:
		...
	def EndUndo(self, keep: bool) -> None:
		...

FusionDoc = _FusionDoc