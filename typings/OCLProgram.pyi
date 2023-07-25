from Image import _Image
from OCLMemory import _OCLMemory
from OCLProgram OCLProgramOCLManager mgr import _OCLProgram OCLProgramOCLManager mgr
from FusionDoc doc import _FusionDoc doc
from string src import _string src
from size_t len import _size_t len


class _OCLProgram:

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
	def CopyToBuffer(self, img: _Image, mem: _OCLMemory, offset: int, wait: bool) -> int:
		...
	def SetWorkgroupSize(self, xsize: int, ysize: int) -> None:
		...
	def Lock(self) -> None:
		...
	def CreateKernel(self, name: str) -> int:
		...
	def WaitForBuild(self, timeout: int) -> bool:
		...
	def ReleaseMemory(self, mem: _OCLMemory) -> bool:
		...
	def info_text(self):
		...
	def RunKernel(self, index: int, block: bool) -> bool:
		...
	def SetSize(self, xsize: int, ysize: int) -> None:
		...
	def Release(self) -> None:
		...
	def Build(self, wait: bool, opts: str) -> bool:
		...
	def OCLProgram(self) -> tuple[_OCLProgram OCLProgramOCLManager mgr, _FusionDoc doc, _string src, _size_t len]:
		"""
		OCLProgram constructor
		"""
		...
	def header_text(self):
		...

OCLProgram = _OCLProgram