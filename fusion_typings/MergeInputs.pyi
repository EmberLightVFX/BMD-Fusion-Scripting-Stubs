from Request import _Request
from TransformMatrix import _TransformMatrix
from TagList import _TagList
from Image import _Image


class _MergeInputs:

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
	def _Merge_TransformMatrix(self, req: _Request, tm: _TransformMatrix, tags: _TagList) -> bool:
		...
	def info_text(self):
		...
	def MergeOf(self, req: _Request, img: _Image, tags: _TagList) -> _Image:
		...
	def header_text(self):
		...
	def _Merge_Image(self, req: _Request, img: _Image, tags: _TagList) -> bool:
		...

MergeInputs = _MergeInputs