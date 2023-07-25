class _GL3DViewer:

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGS_VersionString: str

	REGS_UIName: str

	REGI_ClassType: int

	REGI_Priority: int

	REGB_ControlView: bool

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGB_Unpredictable: bool


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
	def header_text(self):
		...

GL3DViewer = _GL3DViewer