class _Custom:

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

	REGB_Source_GlobalCtrls: bool

	REGB_OpNoMask: bool

	REGB_Source_SizeCtrls: bool

	REGI_Version: int

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
	def GetPtY(self, inp: int, time: float) -> float:
		...
	def info_text(self):
		...
	def header_text(self):
		...
	def GetPtX(self, inp: int, time: float) -> float:
		...
	def GetNum(self, inp: int, time: float) -> float:
		...
	def GetLUT(self, inp: int, v: float) -> float:
		...

Custom = _Custom