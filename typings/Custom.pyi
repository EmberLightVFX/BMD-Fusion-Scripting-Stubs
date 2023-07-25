class _Custom:

	#---Attributes---#
	REGB_NoMotionBlurCtrls: bool

	REGS_OpIconString: str

	REGS_OpDescription: str

	REGS_Name: str

	REGB_ControlView: bool

	REGS_Category: str

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_VersionString: str

	REGB_ForceCommonCtrls: bool

	REGS_UIName: str

	REGI_OpIcon: int

	REGS_IconID: str

	REGB_Source_GlobalCtrls: bool

	REGB_OpNoMask: bool

	REGB_Source_SizeCtrls: bool

	REGB_Hide: bool

	REGB_Source_AspectCtrls: bool

	REGS_ID: str

	REGB_NoAutoProxy: bool

	REGS_HelpTopic: str

	REGS_FileName: str

	REGI_Version: int

	REGI_Priority: int

	REGB_OperatorControl: bool

	REGB_NoBlendCtrls: bool

	REGB_SupportsDoD: bool

	REGB_NoObjMatCtrls: bool


	#---Methods---#
	def GetLUT(self, inp: int, v: float) -> float:
		...
	def info_text(self):
		...
	def GetNum(self, inp: int, time: float) -> float:
		...
	def GetPtY(self, inp: int, time: float) -> float:
		...
	def GetPtX(self, inp: int, time: float) -> float:
		...
	def header_text(self):
		...

Custom = _Custom