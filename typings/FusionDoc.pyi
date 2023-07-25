from TimeStamp import _TimeStamp


class _FusionDoc:

	#---Properties---#
	LastFrameTime: float
	"""
	Read Only
	"""
	Locked: bool
	"""
	Read Only
	"""
	Modified: bool
	"""
	Read Only
	"""
	ProxyScale: int
	"""
	Read Only
	"""
	Proxy: bool
	"""
	Read Only
	"""
	RenderEnd: _TimeStamp
	"""
	Read Only
	"""
	RenderFlags: int
	"""
	Read Only
	"""
	Name: str
	"""
	Read Only
	"""
	AudioOffset: _TimeStamp
	"""
	Read Only
	"""
	RenderStep: int
	"""
	Read Only
	"""
	AverageFrameTime: float
	"""
	Read Only
	"""
	Rendering: bool
	"""
	Read Only
	"""
	CurrentTime: _TimeStamp
	"""
	Read Only
	"""
	TimeRemaining: float
	"""
	Read Only
	"""
	ElapsedTime: float
	"""
	Read Only
	"""
	RenderStart: _TimeStamp
	"""
	Read Only
	"""
	AudioFilename: str
	"""
	Read Only
	"""
	GlobalStart: _TimeStamp
	"""
	Read Only
	"""
	Filename: str
	"""
	Read Only
	"""
	HiQ: bool
	"""
	Read Only
	"""
	GlobalEnd: _TimeStamp
	"""
	Read Only
	"""
	LastFrameRendered: _TimeStamp
	"""
	Read Only
	"""

	#---Methods---#
	def StartUndo(self, name: str) -> None:
		...
	def info_text(self):
		...
	def EndUndo(self, keep: bool) -> None:
		...
	def header_text(self):
		...

FusionDoc = _FusionDoc