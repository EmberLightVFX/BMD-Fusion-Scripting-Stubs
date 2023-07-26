from typing import Any, overload, Literal

class _GLImageViewer:

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGB_ControlView: bool

	REGB_Utility_Toggle: bool

	REGS_Name: str

	REGB_Unpredictable: bool

	REGS_UIName: str


	#---Methods---#
	def LoadLUTAction(self, pathname: str = str()) -> bool:
		"""
		Used by the Action system to load a LUT file into the View LUT
		"""
		...
	def ShowLUTEditor(self) -> None:
		"""
		Pops up the Editor window for the current View LUT
		"""
		...
	def IsLUTEnabled(self) -> bool:
		"""
		Returns true if the current View LUT is enabled
		"""
		...
	def EnableLUT(self, enable: bool = bool()) -> None:
		"""
		Enables or disables the current View LUT
		"""
		...
	def ShowGainGamma(self):
		...
	def IsShowGainGamma(self):
		...
	def header_text(self):
		...
	def IsDoDShown(self):
		...
	def ShowDoD(self, enable: bool = bool()) -> None:
		"""
		Enables or disables drawing the current View DoD rectangle
		"""
		...
	@overload
	def SetRoI(self) -> None:
		"""
		Sets the current View RoI region
		"""
		...
	@overload
	def SetRoI(self, rect: dict[Any, Any]) -> None:
		"""
		Sets the current View RoI region
		"""
		...
	@overload
	def SetRoI(self, auto: bool) -> None:
		"""
		Sets the current View RoI region
		"""
		...
	def DragRoI(self) -> None:
		"""
		Lets the user drag out an RoI rectangle
		"""
		...
	def LockRoI(self, enable: bool = bool()) -> None:
		"""
		Locks or unlocks the View RoI
		"""
		...
	def ShowRoI(self, enable: bool = bool()) -> None:
		"""
		Enables or disables drawing the current View RoI rectangle
		"""
		...
	def IsEnableRoI(self):
		...
	def EnableRoI(self, enable: bool = bool()) -> None:
		"""
		Enables or disables the current View RoI
		"""
		...
	def ExportTo3DLUT(self, pathname: str = str(), cubesize: int = int(), precision: int = int(), rangemin: int = int(), rangemax: int = int()) -> tuple[bool, str]:
		"""
		Exports the current LUTs to a 3D LUT file

		Exports a 3D LUT with cubesize x cubesize x cubesize entries (default 33x33x33).
		Passing nil or no pathname displays a dialog to the user.
		For precision, pass 1 for uint8, 2 for uint16 or 9 for float32 (default float32).
		For HDR LUTs, pass rangemin/rangemax (default is 0.0 to 1.0).
		Returns: boolean success, and the saved LUT's filename.
		"""
		...
	def SaveLUTFile(self, pathname: str = str()) -> bool:
		"""
		Saves current LUTs into a .viewlut file
		"""
		...
	def LoadLUTFile(self, pathname: str = str()) -> bool:
		"""
		Loads a LUT file, setting or LUT plugin ID into the View LUT
		"""
		...

GLImageViewer = _GLImageViewer