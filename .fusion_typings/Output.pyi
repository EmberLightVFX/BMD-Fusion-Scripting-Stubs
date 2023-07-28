from Request import Request_
from Parameter import Parameter_


class Output_:

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
	def header_text(self) -> None:
		...
	def info_text(self) -> None:
		...
	def _SetParam(self, req: Request_, param: Parameter_) -> None:
		...
	def _SetNum(self, req: Request_, num: float) -> None:
		...

Output = Output_