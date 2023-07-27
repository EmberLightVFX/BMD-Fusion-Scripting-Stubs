from FusionDoc import _FusionDoc
from OCLProgram import _OCLProgram
from Registry import _Registry


class _OCLManager:

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
	def _BuildCachedProgramFile(self, id: str, doc: _FusionDoc, filename: str, source: str, len: int, opts: str) -> _OCLProgram:
		...
	def _BuildCachedProgramReg(self, reg: _Registry, doc: _FusionDoc, source: str, len: int, opts: str) -> _OCLProgram:
		...
	def header_text(self):
		...
	def OCLManager(self) -> _OCLManager:
		"""
		OCLManager constructor
		"""
		...
	def BuildProgram(self, doc: _FusionDoc, source: str, len: int, opts: str) -> _OCLProgram:
		...
	def Create(self, device: str) -> bool:
		...

OCLManager = _OCLManager