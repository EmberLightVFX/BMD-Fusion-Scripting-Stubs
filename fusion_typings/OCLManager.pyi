from FusionDoc import FusionDoc_
from OCLProgram import OCLProgram_
from Registry import Registry_


class OCLManager_:

	#---Properties---#
	SupportsImage: bool
	"""
	Read Only
	"""
	FP16: bool
	"""
	Read Only
	"""
	FP64: bool
	"""
	Read Only
	"""
	GLSync: bool
	"""
	Read Only
	"""
	GLSharing: bool
	"""
	Read Only
	"""

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def info_text(self):
		...
	def _BuildCachedProgramFile(self, id: str, doc: FusionDoc_, filename: str, source: str, len: int, opts: str) -> OCLProgram_:
		...
	def _BuildCachedProgramReg(self, reg: Registry_, doc: FusionDoc_, source: str, len: int, opts: str) -> OCLProgram_:
		...
	def header_text(self):
		...
	def OCLManager(self) -> OCLManager_:
		"""
		OCLManager constructor
		"""
		...
	def BuildProgram(self, doc: FusionDoc_, source: str, len: int, opts: str) -> OCLProgram_:
		...
	def Create(self, device: str) -> bool:
		...

OCLManager = OCLManager_