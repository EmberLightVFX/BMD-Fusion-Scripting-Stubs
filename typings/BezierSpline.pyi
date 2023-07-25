from typing import Any

class _BezierSpline:

	#---Attributes---#
	REGB_NoMotionBlurCtrls: bool

	REGS_Name: str

	REGB_ControlView: bool

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGB_ForceCommonCtrls: bool

	REGI_OpIcon: int

	REGB_Source_GlobalCtrls: bool

	REGB_OpNoMask: bool

	REGB_Source_SizeCtrls: bool

	REGB_Hide: bool

	REGB_Source_AspectCtrls: bool

	REGB_NoAutoProxy: bool

	REGS_VersionString: str

	REGS_ID: str

	REGI_Version: int

	REGI_Priority: int

	REGB_OperatorControl: bool

	REGB_NoBlendCtrls: bool

	REGB_SupportsDoD: bool

	REGB_NoObjMatCtrls: bool


	#---Methods---#
	def GetKeyFrames(self) -> dict[Any, Any]:
		"""
		Get a table of keyframes
		"""
		...
	def SetKeyFrames(self, keyframes: dict[Any, Any], replace: bool = bool()) -> None:
		"""
		Set a table of keyframes
		"""
		...
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
	def header_text(self):
		...

BezierSpline = _BezierSpline