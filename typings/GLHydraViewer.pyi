class _GLHydraViewer:

	#---Attributes---#
	REGS_VersionString: str

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGS_UIName: str

	REGB_ControlView: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_FileName: str

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGB_Unpredictable: bool


	#---Methods---#
	def FitAll(self) -> None:
		"""
		Fits this view to the entire scene
		"""
		...
	def SetLighting(self, type: str = str(), enable: bool = bool()) -> None:
		"""
		Controls the type of lighting of objects

		Type should be one of:
			enable
			scene
			cam
			shadows
			smaterials
			skydome
		"""
		...
	def IsLightingEnabled(self) -> None:
		"""
		Returns boolean state of lighting mode
		"""
		...
	def EnableLighting(self, enable: bool = bool()) -> None:
		"""
		Enables or disables lighting of objects
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
		"""
		...
	def GetLighting(self, type: str = str()) -> None:
		"""
		Returns the current type of lighting of objects

		Type should be one of:
			enable
			scene
			cam
			shadows
			smaterials
			skydome
		"""
		...
	def FitSelected(self) -> None:
		"""
		Fits this view to the selected object
		"""
		...
	def CenterSelected(self) -> None:
		"""
		Centers this view on the selected object
		"""
		...
	def header_text(self):
		...

GLHydraViewer = _GLHydraViewer