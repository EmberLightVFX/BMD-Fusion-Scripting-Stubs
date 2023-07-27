from OCLMemory import OCLMemory_
from Image import Image_
from OCLManager import OCLManager_
from FusionDoc import FusionDoc_


class OCLProgram_:

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
	def ReleaseMemory(self, mem: OCLMemory_) -> bool:
		...
	def info_text(self):
		...
	def RunKernel(self, index: int, block: bool) -> bool:
		...
	def SetSize(self, xsize: int, ysize: int) -> None:
		...
	def Build(self, wait: bool, opts: str) -> bool:
		...
	def CopyToBuffer(self, img: Image_, mem: OCLMemory_, offset: int, wait: bool) -> int:
		...
	def SetWorkgroupSize(self, xsize: int, ysize: int) -> None:
		...
	def CreateKernel(self, name: str) -> int:
		...
	def WaitForBuild(self, timeout: int) -> bool:
		...
	def header_text(self):
		...
	def Release(self) -> None:
		...
	def Lock(self) -> None:
		...
	def OCLProgram(self, mgr: OCLManager_, doc: FusionDoc_, src: str, len: int) -> OCLProgram_:
		"""
		OCLProgram constructor
		"""
		...

OCLProgram = OCLProgram_