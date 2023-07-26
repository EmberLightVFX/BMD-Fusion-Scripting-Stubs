from typing import Any, Literal

class _UIWidget:

	#---Properties---#
	SizeIncrement: Any
	"""
	Read/Write
	"""
	BaseSize: Any
	"""
	Read/Write
	"""
	WindowTitle: Any
	"""
	Read/Write
	"""
	WindowFlags: Any
	"""
	Read/Write
	"""
	MouseTracking: Any
	"""
	Read/Write
	"""
	MinimumSize: Any
	"""
	Read/Write
	"""
	MaximumSize: Any
	"""
	Read/Write
	"""
	Enabled: Any
	"""
	Read/Write
	"""
	BackgroundColor: Any
	"""
	Read/Write
	"""
	FocusProxy: Any
	"""
	Read/Write
	"""
	Visible: Any
	"""
	Read/Write
	"""
	WindowFilePath: Any
	"""
	Read/Write
	"""
	ToolTip: Any
	"""
	Read/Write
	"""
	WindowRole: Any
	"""
	Read/Write
	"""
	WindowIconText: Any
	"""
	Read/Write
	"""
	Hidden: Any
	"""
	Read/Write
	"""
	AccessibleDescription: Any
	"""
	Read/Write
	"""
	Font: Any
	StatusTip: Any
	"""
	Read/Write
	"""
	AccessibleName: Any
	"""
	Read/Write
	"""
	StyleSheet: Any
	"""
	Read/Write
	"""
	ToolTipDuration: Any
	"""
	Read/Write
	"""
	AcceptDrops: Any
	"""
	Read/Write
	"""
	AutoFillBackground: Any
	"""
	Read/Write
	"""
	UpdatesEnabled: Any
	"""
	Read/Write
	"""
	WindowState: Any
	"""
	Read/Write
	"""
	WindowOpacity: Any
	"""
	Read/Write
	"""
	FocusPolicy: Any
	"""
	Read/Write
	"""
	ContextMenuPolicy: Any
	"""
	Read/Write
	"""
	FixedSize: Any
	"""
	Write Only
	"""
	Geometry: Any
	"""
	Read/Write
	"""
	WhatsThis: Any
	"""
	Read/Write
	"""
	WindowModality: Any
	"""
	Read/Write
	"""

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def ShowMaximized(self) -> None:
		...
	def ShowMinimized(self) -> None:
		...
	def IsFullScreen(self) -> None:
		...
	def IsMaximized(self) -> None:
		...
	def IsMinimized(self) -> None:
		...
	def IsModal(self) -> None:
		...
	def IsEnabledToTLW(self) -> None:
		...
	def UnderMouse(self) -> None:
		...
	def IsWindow(self) -> None:
		...
	def IsTopLevel(self) -> None:
		...
	def MapFrom(self) -> None:
		...
	def MapTo(self) -> None:
		...
	def MapFromParent(self) -> None:
		...
	def MapToParent(self) -> None:
		...
	def MapFromGlobal(self) -> None:
		...
	def MapToGlobal(self) -> None:
		...
	def GetItems(self) -> None:
		...
	def GetVisible(self) -> None:
		...
	def SetFocus(self) -> None:
		...
	def GetMouseTracking(self) -> None:
		...
	def SetStyleSheet(self) -> None:
		...
	def GetStyleSheet(self) -> None:
		...
	def SetEnabled(self) -> None:
		...
	def GetEnabled(self) -> None:
		...
	def SetContextMenuPolicy(self) -> None:
		...
	def GetContextMenuPolicy(self) -> None:
		...
	def SetFocusPolicy(self) -> None:
		...
	def GetFocusPolicy(self) -> None:
		...
	def SetWindowModality(self) -> None:
		...
	def GetWindowModality(self) -> None:
		...
	def SetWindowState(self) -> None:
		...
	def GetWindowState(self) -> None:
		...
	def SetWindowFlags(self) -> None:
		...
	def AddChild(self) -> None:
		...
	def Update(self) -> None:
		...
	def RemoveChild(self) -> None:
		...
	def Close(self) -> None:
		...
	def Lower(self) -> None:
		...
	def Move(self) -> None:
		...
	def GetWindowFlags(self) -> None:
		...
	def SetFocusProxy(self) -> None:
		...
	def GetFocusProxy(self) -> None:
		...
	def SetWindowFilePath(self) -> None:
		...
	def GetWindowFilePath(self) -> None:
		...
	def SetWindowRole(self) -> None:
		...
	def GetWindowRole(self) -> None:
		...
	def SetWindowIconText(self) -> None:
		...
	def GetWindowIconText(self) -> None:
		...
	def SetUpdatesEnabled(self) -> None:
		...
	def GetUpdatesEnabled(self) -> None:
		...
	def SetAccessibleDescription(self) -> None:
		...
	def GetAccessibleDescription(self) -> None:
		...
	def SetAccessibleName(self) -> None:
		...
	def GetAccessibleName(self) -> None:
		...
	def SetToolTipDuration(self) -> None:
		...
	def GetToolTipDuration(self) -> None:
		...
	def SetAcceptDrops(self) -> None:
		...
	def GetAcceptDrops(self) -> None:
		...
	def SetAutoFillBackground(self) -> None:
		...
	def GetAutoFillBackground(self) -> None:
		...
	def SetWindowOpacity(self) -> None:
		...
	def GetWindowOpacity(self) -> None:
		...
	def SetWindowTitle(self) -> None:
		...
	def GetWindowTitle(self) -> None:
		...
	def SetFixedSize(self) -> None:
		...
	def SetSizeIncrement(self) -> None:
		...
	def GetSizeIncrement(self) -> None:
		...
	def SetBaseSize(self) -> None:
		...
	def GetBaseSize(self) -> None:
		...
	def SetMaximumSize(self) -> None:
		...
	def GetMaximumSize(self) -> None:
		...
	def SetMinimumSize(self) -> None:
		...
	def GetMinimumSize(self) -> None:
		...
	def SetPaletteColor(self) -> None:
		...
	def GetChildren(self) -> None:
		...
	def SetTabOrder(self) -> None:
		...
	def Height(self) -> None:
		...
	def SetParent(self) -> None:
		...
	def Width(self) -> None:
		...
	def Y(self) -> None:
		...
	def X(self) -> None:
		...
	def SetAttribute(self) -> None:
		...
	def Window(self) -> None:
		...
	def GrabKeyboard(self) -> None:
		...
	def GetStatusTip(self) -> None:
		...
	def Repaint(self) -> None:
		...
	def SizeHint(self) -> None:
		...
	def Size(self) -> None:
		...
	def header_text(self):
		...
	def SetVisible(self) -> None:
		...
	def SetMouseTracking(self) -> None:
		...
	def ActivateWindow(self) -> None:
		...
	def ClearFocus(self) -> None:
		...
	def Resize(self) -> None:
		...
	def QueueEvent(self) -> None:
		...
	def Show(self) -> None:
		...
	def WindowType(self) -> None:
		...
	def Hide(self) -> None:
		...
	def OverrideWindowFlags(self) -> None:
		...
	def Find(self) -> None:
		...
	def GetWhatsThis(self) -> None:
		...
	def GetToolTip(self) -> None:
		...
	def HasFocus(self) -> None:
		...
	def FrameSize(self) -> None:
		...
	def Pos(self) -> None:
		...
	def UpdateGeometry(self) -> None:
		...
	def AdjustSize(self) -> None:
		...
	def ChildrenRect(self) -> None:
		...
	def Rect(self) -> None:
		...
	def NormalGeometry(self) -> None:
		...
	def SetGeometry(self) -> None:
		...
	def GetGeometry(self) -> None:
		...
	def FrameGeometry(self) -> None:
		...
	def SetWhatsThis(self) -> None:
		...
	def OverrideWindowState(self) -> None:
		...
	def TestAttribute(self) -> None:
		...
	def SetToolTip(self) -> None:
		...
	def ReleaseKeyboard(self) -> None:
		...
	def SetStatusTip(self) -> None:
		...
	def ReleaseMouse(self) -> None:
		...
	def GrabMouse(self) -> None:
		...
	def MinimumSizeHint(self) -> None:
		...
	def KeyboardGrabber(self) -> None:
		...
	def MouseGrabber(self) -> None:
		...
	def IsEnabledTo(self) -> None:
		...
	def IsVisibleTo(self) -> None:
		...
	def PreviousInFocusChain(self) -> None:
		...
	def NextInFocusChain(self) -> None:
		...
	def FocusWidget(self) -> None:
		...
	def StackUnder(self) -> None:
		...
	def ChildAt(self) -> None:
		...
	def IsAncestorOf(self) -> None:
		...
	def NativeParentWidget(self) -> None:
		...
	def ParentWidget(self) -> None:
		...
	def SetHidden(self) -> None:
		...
	def GetHidden(self) -> None:
		...
	def IsActiveWindow(self) -> None:
		...
	def Raise(self) -> None:
		...
	def ShowNormal(self) -> None:
		...
	def ShowFullScreen(self) -> None:
		...

UIWidget = _UIWidget