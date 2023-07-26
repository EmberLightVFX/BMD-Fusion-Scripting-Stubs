from typing import Any

class _BezierSpline:

	#---Attributes---#
	REGS_VersionString: str

	REGB_ControlView: bool

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGB_ForceCommonCtrls: bool

	REGI_OpIcon: int

	REGB_Source_GlobalCtrls: bool

	REGB_OpNoMask: bool

	REGB_Source_SizeCtrls: bool

	REGB_Source_AspectCtrls: bool

	REGB_NoAutoProxy: bool

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Priority: int

	REGB_NoBlendCtrls: bool

	REGB_NoObjMatCtrls: bool

	REGS_ID: str

	REGB_NoMotionBlurCtrls: bool

	REGI_Version: int

	REGB_OperatorControl: bool


	#---Methods---#
	def DeleteKeyFrames(self, start: int, end: int = int()) -> None:
		"""
		Delete key frames
		"""
		...
	def AdjustKeyFrames(self, start: int, end: int, x: int, y: int, operation: str, pivotx: int = int(), pivoty: int = int()) -> None:
		"""
		Set, Offset or Scale a range of key frames

		start, end: Time range of keypoints to adjust (inclusive)
		x, y:			 Time and Value offsets/factors
		operation:	Can be 'set', 'offset' or 'scale' (case sensitive)
		pivotx, pivoty: optional values to scale around. Default is zero
		"""
		...
	def GetKeyFrames(self) -> dict[Any, Any]:
		"""
		Get a table of keyframes
		"""
		...
	def header_text(self):
		...
	def SetKeyFrames(self, keyframes: dict[Any, Any], replace: bool = bool()) -> None:
		"""
		Set a table of keyframes
		"""
		...

BezierSpline = _BezierSpline