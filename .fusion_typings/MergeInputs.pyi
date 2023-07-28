from Request import Request_
from TransformMatrix import TransformMatrix_
from TagList import TagList_
from Image import Image_


class MergeInputs_:

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
	def _Merge_TransformMatrix(self, req: Request_, tm: TransformMatrix_, tags: TagList_) -> bool:
		...
	def info_text(self) -> None:
		...
	def MergeOf(self, req: Request_, img: Image_, tags: TagList_) -> Image_:
		...
	def header_text(self) -> None:
		...
	def _Merge_Image(self, req: Request_, img: Image_, tags: TagList_) -> bool:
		...

MergeInputs = MergeInputs_