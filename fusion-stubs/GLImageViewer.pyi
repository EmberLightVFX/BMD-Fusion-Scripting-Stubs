from typing import Any, overload

class GLImageViewer:

	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGS_UIName: str

	REGB_Unpredictable: bool

	REGB_Utility_Toggle: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def DragRoI(self) -> None:
		"""
		Lets the user drag out an RoI rectangle
		"""
		...

	def EnableLUT(self, enable: bool | None = None) -> None:
		"""
		Enables or disables the current View LUT

		Args:
			enable (Optional[bool])
		"""
		...

	def EnableRoI(self, enable: bool | None = None) -> None:
		"""
		Enables or disables the current View RoI

		Args:
			enable (Optional[bool])
		"""
		...

	def ExportTo3DLUT(self, pathname: str | None = None, cubesize: int | None = None, precision: int | None = None, rangemin: int | None = None, rangemax: int | None = None) -> bool | str:
		"""
		Exports the current LUTs to a 3D LUT file

		Exports a 3D LUT with cubesize x cubesize x cubesize entries (default 33x33x33).
		Passing nil or no pathname displays a dialog to the user.
		For precision, pass 1 for uint8, 2 for uint16 or 9 for float32 (default float32).
		For HDR LUTs, pass rangemin/rangemax (default is 0.0 to 1.0).
		Returns: boolean success, and the saved LUT's filename.

		Args:
			pathname (Optional[str])
			cubesize (Optional[int])
			precision (Optional[int])
			rangemin (Optional[int])
			rangemax (Optional[int])

		Returns:
			success (bool)
			filename (str)
		"""
		...

	def IsDoDShown(self) -> None:
		...

	def IsEnableRoI(self) -> None:
		...

	def IsLUTEnabled(self) -> bool:
		"""
		Returns true if the current View LUT is enabled

		Returns:
			enabled (bool)
		"""
		...

	def IsShowGainGamma(self) -> None:
		...

	def LoadLUTAction(self, pathname: str | None = None) -> bool:
		"""
		Used by the Action system to load a LUT file into the View LUT

		Args:
			pathname (Optional[str])

		Returns:
			success (bool)
		"""
		...

	def LoadLUTFile(self, pathname: str | None = None) -> bool:
		"""
		Loads a LUT file, setting or LUT plugin ID into the View LUT

		Args:
			pathname (Optional[str])

		Returns:
			success (bool)
		"""
		...

	def LockRoI(self, enable: bool | None = None) -> None:
		"""
		Locks or unlocks the View RoI

		Args:
			enable (Optional[bool])
		"""
		...

	def SaveLUTFile(self, pathname: str | None = None) -> bool:
		"""
		Saves current LUTs into a .viewlut file

		Args:
			pathname (Optional[str])

		Returns:
			success (bool)
		"""
		...

	@overload
	def SetRoI(self) -> None:
		"""
		Sets the current View RoI region

		Reset RoI to full image
		"""
		...

	@overload
	def SetRoI(self, rect: dict[Any, Any]) -> None:
		"""
		Sets the current View RoI region

		Set to table of four normalised coords {left,bottom,right,top} e.g { 0,0,1,1 }

		Args:
			rect (dict[Any, Any])
		"""
		...

	@overload
	def SetRoI(self, auto: bool) -> None:
		"""
		Sets the current View RoI region

		true enables automatic sizing of RoI to the view window

		Args:
			auto (bool)
		"""
		...

	def ShowDoD(self, enable: bool | None = None) -> None:
		"""
		Enables or disables drawing the current View DoD rectangle

		Args:
			enable (Optional[bool])
		"""
		...

	def ShowGainGamma(self) -> None:
		...

	def ShowLUTEditor(self) -> None:
		"""
		Pops up the Editor window for the current View LUT
		"""
		...

	def ShowRoI(self, enable: bool | None = None) -> None:
		"""
		Enables or disables drawing the current View RoI rectangle

		Args:
			enable (Optional[bool])
		"""
		...

