from typing import Any

class PlaybackManager:

	#---Properties---#
	CurrentTime: Any

	FPS: Any

	Gain: Any

	Gamma: Any

	LoopEnabled: Any

	LoopIn: Any

	LoopOut: Any

	PlaybackDevice: Any

	ShowChannel: Any

	ShowMetadata: Any

	SyncMode: Any


	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def ExitMode(self) -> None:
		...

	def GuideEnable(self) -> None:
		...

	def GuideIsEnabled(self) -> None:
		...

	def GuideSelect(self) -> None:
		...

	def IsPlaying(self) -> None:
		...

	def IsReverse(self) -> None:
		...

	def IsUsingDeckLink(self) -> None:
		...

	def ItemNext(self) -> None:
		...

	def ItemPrev(self) -> None:
		...

	def LoopSetShot(self) -> None:
		...

	def Play(self) -> None:
		...

	def ReelExit(self) -> None:
		...

	def SeekBy(self) -> None:
		...

	def SeekEnd(self) -> None:
		...

	def SeekNext(self) -> None:
		...

	def SeekPrev(self) -> None:
		...

	def SeekStart(self) -> None:
		...

	def SeekTo(self) -> None:
		...

	def Stop(self) -> None:
		...

	def TrimExit(self) -> None:
		...

	def TrimSetIn(self) -> None:
		...

	def TrimSetOut(self) -> None:
		...

	def UseDeckLink(self) -> None:
		...

