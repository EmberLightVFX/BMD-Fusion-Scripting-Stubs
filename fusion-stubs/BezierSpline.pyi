from typing import Any

class BezierSpline:

	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_ForceCommonCtrls: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGB_NoAutoProxy: bool

	REGB_NoBlendCtrls: bool

	REGB_NoMotionBlurCtrls: bool

	REGB_NoObjMatCtrls: bool

	REGI_OpIcon: int

	REGB_OpNoMask: bool

	REGB_OperatorControl: bool

	REGI_Priority: int

	REGB_Source_AspectCtrls: bool

	REGB_Source_GlobalCtrls: bool

	REGB_Source_SizeCtrls: bool

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def AdjustKeyFrames(self, start: int, end: int, x: int, y: int, operation: str, pivotx: int | None = None, pivoty: int | None = None) -> None:
		"""
		Set, Offset or Scale a range of key frames

		start, end: Time range of keypoints to adjust (inclusive)
		x, y:       Time and Value offsets/factors
		operation:  Can be 'set', 'offset' or 'scale' (case sensitive)
		pivotx, pivoty: optional values to scale around. Default is zero

		Args:
			start (int)
			end (int)
			x (int)
			y (int)
			operation (str)
			pivotx (Optional[int])
			pivoty (Optional[int])
		"""
		...

	def DeleteKeyFrames(self, start: int, end: int | None = None) -> None:
		"""
		Delete key frames

		Args:
			start (int)
			end (Optional[int])
		"""
		...

	def GetKeyFrames(self) -> dict[Any, Any]:
		"""
		Get a table of keyframes

		Returns:
			keyframes (dict[Any, Any])
		"""
		...

	def SetKeyFrames(self, keyframes: dict[Any, Any], replace: bool | None = None) -> None:
		"""
		Set a table of keyframes

		Args:
			keyframes (dict[Any, Any])
			replace (Optional[bool])
		"""
		...

