from Image import Image
from Tool import Tool

class Preview:

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
    def Close(self) -> None:
        """
        Closes the current clip
        """
        ...

    def Create(self, tool: Tool, filename: str | None = None) -> bool:
        """
        Renders a new preview clip

        Args:
            tool (Tool)
            filename (Optional[str])

        Returns:
            success (bool)
        """
        ...

    def DisplayImage(self, img: Image) -> bool:
        """
        Displays an Image object

        Args:
            img (Image)

        Returns:
            success (bool)
        """
        ...

    def IsPlaying(self) -> bool:
        """
        Indicates if the preview is currently playing

        Returns:
            playing (bool)
        """
        ...

    def Open(self, filename: str) -> bool:
        """
        Opens a filename for seeking and playback

        Args:
            filename (str)

        Returns:
            success (bool)
        """
        ...

    def Play(self, reverse: bool | None = None) -> None:
        """
        Plays the current clip

        Args:
            reverse (Optional[bool])
        """
        ...

    def Seek(self, frame: int) -> None:
        """
        Seeks to specified frame

        Args:
            frame (int)
        """
        ...

    def Stop(self) -> None:
        """
        Stops playback
        """
        ...

    def ViewOn(self, tool: Tool) -> bool:
        """
        Attaches a Preview to a Tool to display its output

        Args:
            tool (Tool)

        Returns:
            success (bool)
        """
        ...

