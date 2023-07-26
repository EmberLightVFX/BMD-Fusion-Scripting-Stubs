from typing import Literal

from OCLMemory import _OCLMemory
from Image import _Image
from OCLManager import _OCLManager
from FusionDoc import _FusionDoc


class _OCLProgram:

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
	def ReleaseMemory(self, mem: _OCLMemory) -> bool:
		...
	def info_text(self):
		...
	def RunKernel(self, index: int, block: bool) -> bool:
		...
	def SetSize(self, xsize: int, ysize: int) -> None:
		...
	def Build(self, wait: bool, opts: str) -> bool:
		...
	def CopyToBuffer(self, img: _Image, mem: _OCLMemory, offset: int, wait: bool) -> int:
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
	def OCLProgram(self, mgr: _OCLManager, doc: _FusionDoc, src: str, len: int) -> _OCLProgram:
		"""
		OCLProgram constructor
		"""
		...

OCLProgram = _OCLProgram