class Point_:

	#---Properties---#
	X: float
	"""
	Read/Write
	"""
	Z: float
	"""
	Read/Write
	"""
	Y: float
	"""
	Read/Write
	"""

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def __mul(self, num: float) -> Point_:
		...
	def info_text(self) -> None:
		...
	def Point(self, x: float, y: float, z: float) -> Point_:
		"""
		Point constructor
		"""
		...
	def __eq(self, pt: Point_) -> bool:
		...
	def __unm(self) -> Point_:
		...
	def header_text(self) -> None:
		...
	def __div(self, num: float) -> Point_:
		...
	def __add(self, pt: Point_) -> Point_:
		...
	def __sub(self, pt: Point_) -> Point_:
		...

Point = Point_