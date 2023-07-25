from Image import _Image
from Tool import _Tool


class _Preview:

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
	def Open(self, filename: str) -> bool:
		"""
		Opens a filename for seeking and playback
		"""
		...
	def Close(self) -> None:
		"""
		Closes the current clip
		"""
		...
	def IsPlaying(self) -> bool:
		"""
		Indicates if the preview is currently playing
		"""
		...
	def Stop(self) -> None:
		"""
		Stops playback
		"""
		...
	def Seek(self, frame: int) -> None:
		"""
		Seeks to specified frame
		"""
		...
	def DisplayImage(self, img: _Image) -> bool:
		"""
		Displays an Image object
		"""
		...
	def ViewOn(self, tool: _Tool) -> bool:
		"""
		Attaches a Preview to a Tool to display its output
		"""
		...
	def Create(self, tool: _Tool, filename: str = str()) -> bool:
		"""
		Renders a new preview clip
		"""
		...
	def Play(self, reverse: bool = bool()) -> None:
		"""
		Plays the current clip
		"""
		...
	def header_text(self):
		...

Preview = _Preview