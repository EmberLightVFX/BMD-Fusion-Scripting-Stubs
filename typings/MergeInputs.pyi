from Request import _Request
from Image import _Image
from TagList import _TagList
from TransformMatrix import _TransformMatrix


class _MergeInputs:

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
	def _Merge_Image(self, req: _Request, img: _Image, tags: _TagList) -> bool:
		...
	def MergeOf(self, req: _Request, img: _Image, tags: _TagList) -> _Image:
		...
	def _Merge_TransformMatrix(self, req: _Request, tm: _TransformMatrix, tags: _TagList) -> bool:
		...
	def info_text(self):
		...
	def header_text(self):
		...

MergeInputs = _MergeInputs