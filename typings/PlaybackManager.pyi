from typing import Any

class _PlaybackManager:

	#---Properties---#
	LoopOut: Any
	"""
	Read/Write
	"""
	LoopIn: Any
	"""
	Read/Write
	"""
	ShowMetadata: Any
	"""
	Read/Write
	"""
	Gamma: Any
	"""
	Read/Write
	"""
	LoopMode: Any
	PlaybackDevice: Any
	"""
	Read/Write
	"""
	SyncMode: Any
	"""
	Read/Write
	"""
	ShowChannel: Any
	"""
	Read/Write
	"""
	Gain: Any
	"""
	Read/Write
	"""
	CurrentTime: Any
	"""
	Read/Write
	"""
	FPS: Any
	"""
	Read/Write
	"""
	LoopEnabled: Any
	"""
	Read/Write
	"""

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_VersionString: str

	REGS_ID: str

	REGB_ControlView: bool

	REGI_Priority: int


	#---Methods---#
	def GuideEnable(self):
		...
	def GuideIsEnabled(self):
		...
	def UseDeckLink(self):
		...
	def IsUsingDeckLink(self):
		...
	def ExitMode(self):
		...
	def ItemPrev(self):
		...
	def ItemNext(self):
		...
	def ReelExit(self):
		...
	def TrimExit(self):
		...
	def LoopSetShot(self):
		...
	def TrimSetOut(self):
		...
	def TrimSetIn(self):
		...
	def header_text(self):
		...
	def IsReverse(self):
		...
	def IsPlaying(self):
		...
	def Stop(self):
		...
	def SeekEnd(self):
		...
	def SeekPrev(self):
		...
	def SeekNext(self):
		...
	def SeekStart(self):
		...
	def SeekTo(self):
		...
	def SeekBy(self):
		...
	def Play(self):
		...
	def GuideSelect(self):
		...

PlaybackManager = _PlaybackManager