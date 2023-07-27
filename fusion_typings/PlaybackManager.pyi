from typing import Any

class PlaybackManager_:

	#---Properties---#
	PlaybackDevice: Any
	"""
	Read/Write
	"""
	LoopEnabled: Any
	"""
	Read/Write
	"""
	LoopOut: Any
	"""
	Read/Write
	"""
	LoopIn: Any
	"""
	Read/Write
	"""
	LoopMode: Any
	ShowMetadata: Any
	"""
	Read/Write
	"""
	Gamma: Any
	"""
	Read/Write
	"""
	SyncMode: Any
	"""
	Read/Write
	"""
	CurrentTime: Any
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
	FPS: Any
	"""
	Read/Write
	"""

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def LoopSetShot(self):
		...
	def TrimSetOut(self):
		...
	def TrimSetIn(self):
		...
	def IsReverse(self):
		...
	def IsPlaying(self):
		...
	def Stop(self):
		...
	def SeekEnd(self):
		...
	def header_text(self):
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
	def SeekPrev(self):
		...

PlaybackManager = PlaybackManager_