class GL3DViewer_:

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
	def GetTransparency(self) -> None:
		"""
		Returns string of transparency mode
		"""
		...
	def SetTransparency(self, mode: str = str()) -> None:
		"""
		Sets transparency mode to zbuffer, sorted, or quicksort
		"""
		...
	def IsShadowsEnabled(self) -> None:
		"""
		Returns boolean state of lighting mode
		"""
		...
	def EnableShadows(self, enable: bool = bool()) -> None:
		"""
		Enables or disables shadowing of objects
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
	def IsWireframeEnabled(self) -> None:
		"""
		Returns boolean state of wireframe mode
		"""
		...
	def EnableWireframe(self, enable: bool = bool()) -> None:
		"""
		Enables or disables wireframe drawing of objects
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
	def CenterSelected(self) -> None:
		"""
		Centers this view on the selected object
		"""
		...
	def header_text(self) -> None:
		...

GL3DViewer = GL3DViewer_