class Custom:

	#---Registry---#
	REGS_Category: str

	REGI_ClassType: int

	REGB_ControlView: bool

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
	def GetLUT(self, inp: int, v: float) -> float:
		...

	def GetNum(self, inp: int, time: float) -> float:
		...

	def GetPtX(self, inp: int, time: float) -> float:
		...

	def GetPtY(self, inp: int, time: float) -> float:
		...

