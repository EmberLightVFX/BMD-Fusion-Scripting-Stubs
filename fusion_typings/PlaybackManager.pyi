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
	def LoopSetShot(self) -> None:
		...
	def TrimSetOut(self) -> None:
		...
	def TrimSetIn(self) -> None:
		...
	def IsReverse(self) -> None:
		...
	def IsPlaying(self) -> None:
		...
	def Stop(self) -> None:
		...
	def SeekEnd(self) -> None:
		...
	def header_text(self) -> None:
		...
	def SeekNext(self) -> None:
		...
	def SeekStart(self) -> None:
		...
	def SeekTo(self) -> None:
		...
	def SeekBy(self) -> None:
		...
	def Play(self) -> None:
		...
	def GuideSelect(self) -> None:
		...
	def GuideEnable(self) -> None:
		...
	def GuideIsEnabled(self) -> None:
		...
	def UseDeckLink(self) -> None:
		...
	def IsUsingDeckLink(self) -> None:
		...
	def ExitMode(self) -> None:
		...
	def ItemPrev(self) -> None:
		...
	def ItemNext(self) -> None:
		...
	def ReelExit(self) -> None:
		...
	def TrimExit(self) -> None:
		...
	def SeekPrev(self) -> None:
		...

PlaybackManager = PlaybackManager_