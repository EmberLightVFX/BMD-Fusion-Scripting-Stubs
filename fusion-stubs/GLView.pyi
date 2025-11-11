from typing import Any, overload

from GLViewer import GLViewer

class GLView:

    #---Properties---#
    CurrentViewer: GLViewer


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
    def AddToolAction(self) -> None:
        ...

    def DisableCurrentTools(self) -> None:
        """
        Pass-through the currently selected tools
        """
        ...

    def DisableSelectedTools(self) -> None:
        """
        Pass-through the selected tools
        """
        ...

    def EnableLUT(self, enable: bool | None = None) -> None:
        """
        Enables or disables the current Monitor LUT

        Args:
            enable (Optional[bool])
        """
        ...

    def EnableStereo(self, enable: bool | None = None) -> None:
        """
        Enables or disables 3D stereo display

        Args:
            enable (Optional[bool])
        """
        ...

    def GetBuffer(self) -> int:
        """
        Returns which buffer is shown

        where 'buffer' is one of the following numbers:
        0 = A
        1 = B
        2 = A|B split

        Returns:
            buffer (int)
        """
        ...

    def GetLocked(self) -> bool:
        """
        Returns true if the display is locked

        Returns:
            enabled (bool)
        """
        ...

    def GetPos(self) -> int | int | int:
        """
        Returns the position of the display

        Returns:
            x (int)
            y (int)
            z (int)
        """
        ...

    def GetPosTable(self) -> dict[Any, Any]:
        """
        Returns the position of the display as a table

        Returns:
        x = table[1]
        y = table[2]
        z = table[3]

        Returns:
            pos (dict[Any, Any])
        """
        ...

    def GetPrefs(self) -> dict[Any, Any]:
        """
        Retrieve a table of preferences for this view

        Returns a table of Preference attributes

        Returns:
            prefs (dict[Any, Any])
        """
        ...

    def GetPreview(self, buffer: int | None = None) -> None:
        """
        Returns the buffer's Preview

        where 'buffer' is one of the following numbers:
        0 = A
        1 = B
        2 = A|B split
        If 'buffer' is not specified, the current Preview is returned.

        Args:
            buffer (Optional[int])
        """
        ...

    def GetRot(self) -> int | int | int:
        """
        Returns the x,y,z rotation of the display in degrees

        Returns:
            x (int)
            y (int)
            z (int)
        """
        ...

    def GetRotTable(self) -> dict[Any, Any]:
        """
        Returns the x,y,z rotation of the display in degrees as a table

        Returns:
        x = table[1]
        y = table[2]
        z = table[3]

        Returns:
            rot (dict[Any, Any])
        """
        ...

    def GetScale(self) -> int:
        """
        Returns the scale of the display

        Returns:
            scale (int)
        """
        ...

    def GetScaleFit(self) -> bool:
        """
        Indicates if the display is set to scale-to-fit

        Returns:
            fit (bool)
        """
        ...

    def GetSplit(self) -> int | int | int:
        """
        Get the split position of the view

        Returns:
            x (int)
            y (int)
            angle (int)
        """
        ...

    def GetSplitTable(self) -> dict[Any, Any]:
        """
        Get the split position of the view as a table

        Returns:
        x = table[1]
        y = table[2]
        angle = table[3]

        Returns:
            split (dict[Any, Any])
        """
        ...

    def GetStereoMethod(self) -> str | None | None:
        """
        Returns the method and options being used for stereo display

        method can be 'Quad Buffer', 'Anaglyph', 'Crosseyed', 'Interlaced', 'Checkerboard', 'Left Eye Only' or 'Right'
        If method is 'Anaglyph':
        option1 can be 'Red/Cyan', 'Red/Green',	'Red/Blue', 'Amber/Blue' or 'Green/Magenta'
        option2 can be 'Monochrome', 'Half-color',	'Color', 'Optimised' or 'Dubois'

        Returns:
            method (str)
            option1
            option2
        """
        ...

    def GetStereoSource(self) -> bool | bool | str:
        """
        Returns the source being used for stereo display

        ABsource is true if the A & B buffers are used for left & right
        stacked is true if the two halves of the image are used
        stackmethod will be 'Horizontal' or 'Vertical'

        Returns:
            ABsource (bool)
            stacked (bool)
            stackmethod (str)
        """
        ...

    def GetViewerList(self) -> list[Any]:
        """
        Returns a list of available viewers

        Returns:
            viewers (list[Any])
        """
        ...

    def IsLUTEnabled(self) -> bool:
        """
        Returns true if the current Monitor LUT is enabled

        Returns:
            enabled (bool)
        """
        ...

    def IsStereoEnabled(self) -> bool:
        """
        Indicates if stereo display is currently enabled

        Returns:
            enabled (bool)
        """
        ...

    def IsStereoSwapped(self) -> bool:
        """
        Indicates if the left & right stereo eyes are currently swapped

        Returns:
            enable (bool)
        """
        ...

    def IsWipeEnabled(self) -> None:
        ...

    def LoadLUTFile(self, pathname: str) -> bool:
        """
        Loads a LUT file, setting or LUT plugin ID into the Monitor LUT

        Args:
            pathname (str)

        Returns:
            success (bool)
        """
        ...

    @overload
    def LoadPrefs(self) -> None:
        """
        Saves the current view prefs to a named configuration

        Load prefs from defaults
        """
        ...

    @overload
    def LoadPrefs(self, configname: str) -> None:
        """
        Saves the current view prefs to a named configuration

        Load prefs from <configname>

        Args:
            configname (str)
        """
        ...

    def ResetView(self) -> None:
        """
        Resets the display to default position etc
        """
        ...

    @overload
    def SavePrefs(self) -> None:
        """
        Saves the current view prefs to a named configuration

        Save prefs to defaults
        """
        ...

    @overload
    def SavePrefs(self, configname: str) -> None:
        """
        Saves the current view prefs to a named configuration

        Save prefs to <configname>

        Args:
            configname (str)
        """
        ...

    def SetBuffer(self, buffer: int, toggle: bool | None = None) -> None:
        """
        Show a particular buffer

        where 'buffer' is one of the following numbers:
        0 = A
        1 = B
        2 = A|B split

        Args:
            buffer (int)
            toggle (Optional[bool])
        """
        ...

    def SetLocked(self, enable: bool | None = None) -> None:
        """
        Lock or unlock the display

        Args:
            enable (Optional[bool])
        """
        ...

    def SetPos(self, x: int, y: int, z: int | None = None) -> bool:
        """
        Set the position of the display

        Args:
            x (int)
            y (int)
            z (Optional[int])

        Returns:
            success (bool)
        """
        ...

    def SetRot(self, x: int, y: int, z: int) -> None:
        """
        Set the x,y,z rotation of the display in degrees

        Args:
            x (int)
            y (int)
            z (int)
        """
        ...

    def SetScale(self, scale: int) -> None:
        """
        Set the scale of the display

        Args:
            scale (int)
        """
        ...

    def SetSplit(self, x: int, y: int, angle: int) -> None:
        """
        Set the split position of the view

        Args:
            x (int)
            y (int)
            angle (int)
        """
        ...

    def SetStereoMethod(self, method: str, option1: None | None = None, option2: None | None = None) -> None:
        """
        Sets the method for stereo display

        method can be one of the following strings:
        'Quad Buffer'	Enable OpenGL quad-buffered stereo mode
        'Anaglyph'		Tint and combine views for anaglyph glasses
        option1 can be 'Red/Cyan', 'Red/Green',	'Red/Blue', 'Amber/Blue' or 'Green/Magenta'
        option2 can be 'Monochrome', 'Half-color',	'Color', 'Optimised' or 'Dubois' (forces 'Red/Cyan')
        'Crosseyed'		Display views side-by-side for crosseyed viewing
        'Interlaced'		Display views on alternate scanlines
        'Checkerboard'		Stereo support for checkerboard DLPs
        option1 is the value for gamma correction of the polariser screen
        'Left Eye Only'	Display left eye view only
        'Right Eye Only'	Display right eye view only

        Args:
            method (str)
            option1 (Optional[None])
            option2 (Optional[None])
        """
        ...

    def SetStereoSource(self, ABsource: bool, stacked: bool, stackmethod: str | None = None) -> None:
        """
        Sets the source for the left & right stereo images

        Pass true for ABsource to use the A and B buffers for left & right views.
        Pass true for stacked to use the two halves of the image for left & right views.
        stackmethod may be 'Horizontal' or 'Vertical' for side-by-side or over-under images, respectively.

        Args:
            ABsource (bool)
            stacked (bool)
            stackmethod (Optional[str])
        """
        ...

    def ShowLUTEditor(self) -> None:
        """
        Pops up the Editor window for the current Monitor LUT
        """
        ...

    def ShowQuadView(self, enable: bool | None = None) -> None:
        """
        Splits the view into four subviews

        Args:
            enable (Optional[bool])
        """
        ...

    def ShowSubView(self, enable: bool | None = None) -> None:
        """
        Enables the inset SubView display

        Args:
            enable (Optional[bool])
        """
        ...

    def ShowingQuadView(self) -> bool:
        """
        Returns true if the view is split into four

        Returns:
            enabled (bool)
        """
        ...

    def ShowingSubView(self) -> bool:
        """
        Returns true if the inset SubView is currently being displayed

        Returns:
            enabled (bool)
        """
        ...

    @overload
    def SwapStereo(self) -> None:
        """
        Swaps left & right stereo eye views

        Toggle eye swap
        """
        ...

    @overload
    def SwapStereo(self, enable: bool | None = None) -> None:
        """
        Swaps left & right stereo eye views

        Set eye swap

        Args:
            enable (Optional[bool])
        """
        ...

    def SwapSubView(self) -> bool:
        """
        Swaps the SubView with the Main View

        Returns:
            enabled (bool)
        """
        ...

    def WipeEnable(self) -> None:
        ...

