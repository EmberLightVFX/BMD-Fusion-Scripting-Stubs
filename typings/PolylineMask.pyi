from typing import Any

class _PolylineMask:

	#---Attributes---#
	REGB_NoMotionBlurCtrls: bool

	REGS_OpIconString: str

	REGS_OpDescription: str

	REGS_Name: str

	REGB_ControlView: bool

	REGS_Category: str

	REGS_VersionString: str

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_UIName: str

	REGB_ForceCommonCtrls: bool

	REGS_IconID: str

	REGB_OperatorControl: bool

	REGS_ID: str

	REGB_Source_GlobalCtrls: bool

	REGB_OpNoMask: bool

	REGB_Source_SizeCtrls: bool

	REGI_DataType: int

	REGB_Source_AspectCtrls: bool

	REGS_HelpTopic: str

	REGB_NoAutoProxy: bool

	REGS_FileName: str

	REGI_Version: int

	REGI_OpIcon: int

	REGI_Priority: int

	REGB_Hide: bool

	REGB_NoBlendCtrls: bool

	REGB_SupportsDoD: bool

	REGB_NoObjMatCtrls: bool


	#---Methods---#
	def ConvertToBSpline(self) -> None:
		"""
		Converts to b-spline polyline
		"""
		...
	def ConvertToBezier(self) -> None:
		"""
		Converts to Bezier polyline
		"""
		...
	def GetBezierPolyline(self, time: int, which: str = str()) -> dict[Any, Any]:
		"""
		Get a table of bezier polyline

		second argument:	Can be 'outter' in case of retrieving outter polyline (case sensitive)
		Returns: table of Bezier polyline (converts to Bezier if necessary
		"""
		...
	def header_text(self):
		...

PolylineMask = _PolylineMask