class Point:

	#---Properties---#
	X: float

	Y: float

	Z: float


	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGB_Utility_Toggle: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def __add(self, pt: Point) -> Point:
		...

	def __div(self, num: float) -> Point:
		...

	def __eq(self, pt: Point) -> bool:
		...

	def __mul(self, num: float) -> Point:
		...

	def __new(self, x: float, y: float, z: float) -> Point:
		"""
		Point constructor

		Args:
			x (float)
			y (float)
			z (float)

		Returns:
			Point
		"""
		...

	def __sub(self, pt: Point) -> Point:
		...

	def __unm(self) -> Point:
		...

