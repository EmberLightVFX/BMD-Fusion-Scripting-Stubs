from typing import Literal

class _RenderNode:

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
	def Abort(self):
		...
	def IsDisconnecting(self):
		...
	def IsIdle(self):
		...
	def GetJob(self):
		...
	def header_text(self):
		...
	def IsProcessing(self):
		...

RenderNode = _RenderNode