from typing import Any, Literal

class _PolylineMask:

	#---Attributes---#
	REGS_FileName: str

	REGS_VersionString: str

	REGB_ControlView: bool

	REGS_Category: str

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGB_ForceCommonCtrls: bool

	REGI_OpIcon: int

	REGB_OperatorControl: bool

	REGI_Version: int

	REGB_Source_GlobalCtrls: bool

	REGB_OpNoMask: bool

	REGB_Source_SizeCtrls: bool

	REGI_DataType: int

	REGB_Source_AspectCtrls: bool

	REGS_OpDescription: str

	REGB_NoAutoProxy: bool

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Priority: int

	REGS_IconID: str

	REGB_NoBlendCtrls: bool

	REGS_ID: str

	REGB_NoObjMatCtrls: bool

	REGS_HelpTopic: str

	REGB_NoMotionBlurCtrls: bool

	REGS_OpIconString: str

	REGS_UIName: str


	#---Methods---#
	def header_text(self):
		...
	def ConvertToBezier(self) -> None:
		"""
		Converts to Bezier polyline
		"""
		...
	def ConvertToBSpline(self) -> None:
		"""
		Converts to b-spline polyline
		"""
		...
	def GetBezierPolyline(self, time: int, which: str = str()) -> dict[Any, Any]:
		"""
		Get a table of bezier polyline

		second argument:	Can be 'outter' in case of retrieving outter polyline (case sensitive)
		Returns: table of Bezier polyline (converts to Bezier if necessary
		"""
		...

PolylineMask = _PolylineMask