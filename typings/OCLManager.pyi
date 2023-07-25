from FusionDoc import _FusionDoc
from OCLProgram import _OCLProgram
from OCLManager OCLManager import _OCLManager OCLManager
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
	GLSync: bool
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

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_VersionString: str

	REGS_ID: str

	REGB_ControlView: bool

	REGI_Priority: int


	#---Methods---#
	def info_text(self):
		...
	def _BuildCachedProgramFile(self, id: str, doc: _FusionDoc, filename: str, source: str, len: int, opts: str) -> _OCLProgram:
		...
	def OCLManager(self) -> _OCLManager OCLManager:
		"""
		OCLManager constructor
		"""
		...
	def _BuildCachedProgramReg(self, reg: _Registry, doc: _FusionDoc, source: str, len: int, opts: str) -> _OCLProgram:
		...
	def Create(self, device: str) -> bool:
		...
	def BuildProgram(self, doc: _FusionDoc, source: str, len: int, opts: str) -> _OCLProgram:
		...
	def header_text(self):
		...

OCLManager = _OCLManager