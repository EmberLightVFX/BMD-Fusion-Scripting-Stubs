from typing import Any

class PolylineMask:

	#---Registry---#
	REGS_Category: str

	REGI_ClassType: int

	REGB_ControlView: bool

	REGI_DataType: int

	REGS_FileName: str

	REGB_ForceCommonCtrls: bool

	REGS_HelpTopic: str

	REGB_Hide: bool

	REGS_ID: str

	REGS_IconID: str

	REGS_Name: str

	REGB_NoAutoProxy: bool

	REGB_NoBlendCtrls: bool

	REGB_NoMotionBlurCtrls: bool

	REGB_NoObjMatCtrls: bool

	REGS_OpDescription: str

	REGI_OpIcon: int

	REGS_OpIconString: str

	REGB_OpNoMask: bool

	REGB_OperatorControl: bool

	REGI_Priority: int

	REGB_Source_SizeCtrls: bool

	REGB_Source_GlobalCtrls: bool

	REGB_Source_AspectCtrls: bool

	REGB_SupportsDoD: bool

	REGS_UIName: str

	REGB_Unpredictable: bool

	REGI_Version: int

	REGS_VersionString: str


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

	def GetBezierPolyline(self, time: int, which: str | None = None) -> dict[Any, Any]:
		"""
		Get a table of bezier polyline

		second argument:  Can be 'outter' in case of retrieving outter polyline (case sensitive)
		Returns: table of Bezier polyline (converts to Bezier if necessary

		Args:
			time (int)
			which (Optional[str])

		Returns:
			poly (dict[Any, Any])
		"""
		...

