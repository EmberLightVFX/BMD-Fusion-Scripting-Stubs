class GL3DViewer:

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
	def CenterSelected(self) -> None:
		"""
		Centers this view on the selected object
		"""
		...

	def EnableLighting(self, enable: bool | None = None) -> None:
		"""
		Enables or disables lighting of objects

		Args:
			enable (Optional[bool])
		"""
		...

	def EnableShadows(self, enable: bool | None = None) -> None:
		"""
		Enables or disables shadowing of objects

		Args:
			enable (Optional[bool])
		"""
		...

	def EnableWireframe(self, enable: bool | None = None) -> None:
		"""
		Enables or disables wireframe drawing of objects

		Args:
			enable (Optional[bool])
		"""
		...

	def FitAll(self) -> None:
		"""
		Fits this view to the entire scene
		"""
		...

	def FitSelected(self) -> None:
		"""
		Fits this view to the selected object
		"""
		...

	def GetTransparency(self) -> None:
		"""
		Returns string of transparency mode
		"""
		...

	def IsLightingEnabled(self) -> None:
		"""
		Returns boolean state of lighting mode
		"""
		...

	def IsShadowsEnabled(self) -> None:
		"""
		Returns boolean state of lighting mode
		"""
		...

	def IsWireframeEnabled(self) -> None:
		"""
		Returns boolean state of wireframe mode
		"""
		...

	def SetTransparency(self, mode: str | None = None) -> None:
		"""
		Sets transparency mode to zbuffer, sorted, or quicksort

		Args:
			mode (Optional[str])
		"""
		...

