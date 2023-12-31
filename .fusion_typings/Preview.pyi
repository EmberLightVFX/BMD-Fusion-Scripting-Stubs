from Tool import Tool_
from Image import Image_


class Preview_:

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
	def Play(self, reverse: bool = bool()) -> None:
		"""
		Plays the current clip
		"""
		...
	def Create(self, tool: Tool_, filename: str = str()) -> bool:
		"""
		Renders a new preview clip
		"""
		...
	def Seek(self, frame: int) -> None:
		"""
		Seeks to specified frame
		"""
		...
	def Close(self) -> None:
		"""
		Closes the current clip
		"""
		...
	def ViewOn(self, tool: Tool_) -> bool:
		"""
		Attaches a Preview to a Tool to display its output
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
	def header_text(self) -> None:
		...
	def DisplayImage(self, img: Image_) -> bool:
		"""
		Displays an Image object
		"""
		...
	def Open(self, filename: str) -> bool:
		"""
		Opens a filename for seeking and playback
		"""
		...

Preview = Preview_