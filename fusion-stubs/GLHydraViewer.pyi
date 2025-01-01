class GLHydraViewer:

	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGS_FileName: str

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

	def GetLighting(self, type: str | None = None) -> None:
		"""
		Returns the current type of lighting of objects

		Type should be one of:
		enable
		scene
		cam
		shadows
		smaterials
		skydome

		Args:
			type (Optional[str])
		"""
		...

	def GetShading(self) -> None:
		"""
		Returns the current object shading method

		Returns one of:
		points
		wireframe
		wireframeonsurface
		flatshading
		smoothshading
		geometryonly
		geometryflat
		geometrysmooth
		"""
		...

	def IsLightingEnabled(self) -> None:
		"""
		Returns boolean state of lighting mode
		"""
		...

	def SetLighting(self, type: str | None = None, enable: bool | None = None) -> None:
		"""
		Controls the type of lighting of objects

		Type should be one of:
		enable
		scene
		cam
		shadows
		smaterials
		skydome

		Args:
			type (Optional[str])
			enable (Optional[bool])
		"""
		...

	def SetShading(self, method: str) -> None:
		"""
		Sets the object shading method

		Method should be one of:
		points
		wireframe
		wireframeonsurface
		flatshading
		smoothshading
		geometryonly
		geometryflat
		geometrysmooth

		Args:
			method (str)
		"""
		...

