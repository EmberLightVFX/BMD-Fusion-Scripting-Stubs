from Registry import Registry
from OCLProgram import OCLProgram
from FusionDoc import FusionDoc


class OCLManager:

	#---Properties---#
	FP16: bool
	"""
	Read Only
	"""

	FP64: bool
	"""
	Read Only
	"""

	GLSharing: bool
	"""
	Read Only
	"""

	GLSync: bool
	"""
	Read Only
	"""

	SupportsImage: bool
	"""
	Read Only
	"""


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
	def BuildProgram(self, doc: FusionDoc, source: str, len: int, opts: str) -> OCLProgram:
		...

	def Create(self, device: str) -> bool:
		...

	def _BuildCachedProgramFile(self, id: str, doc: FusionDoc, filename: str, source: str, len: int, opts: str) -> OCLProgram:
		...

	def _BuildCachedProgramReg(self, reg: Registry, doc: FusionDoc, source: str, len: int, opts: str) -> OCLProgram:
		...

	def __new(self) -> OCLManager:
		"""
		OCLManager constructor

		Returns:
			OCLManager
		"""
		...

