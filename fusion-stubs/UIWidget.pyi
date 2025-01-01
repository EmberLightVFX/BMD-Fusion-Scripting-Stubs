from typing import Any

class UIWidget:

	#---Properties---#
	AcceptDrops: Any

	AccessibleDescription: Any

	AccessibleName: Any

	AutoFillBackground: Any

	BackgroundColor: Any

	BaseSize: Any

	ContextMenuPolicy: Any

	Enabled: Any

	FixedSize: Any
	"""
	Write Only
	"""

	FocusPolicy: Any

	FocusProxy: Any

	Geometry: Any

	Hidden: Any

	MaximumSize: Any

	MinimumSize: Any

	MouseTracking: Any

	SizeIncrement: Any

	StatusTip: Any

	StyleSheet: Any

	ToolTip: Any

	ToolTipDuration: Any

	UpdatesEnabled: Any

	Visible: Any

	WhatsThis: Any

	WindowFilePath: Any

	WindowFlags: Any

	WindowIconText: Any

	WindowModality: Any

	WindowOpacity: Any

	WindowRole: Any

	WindowState: Any

	WindowTitle: Any


	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGB_Utility_Toggle: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def ActivateWindow(self) -> None:
		...

	def AddChild(self) -> None:
		...

	def AdjustSize(self) -> None:
		...

	def ChildAt(self) -> None:
		...

	def ChildrenRect(self) -> None:
		...

	def ClearFocus(self) -> None:
		...

	def Close(self) -> None:
		...

	def Find(self) -> None:
		...

	def FocusWidget(self) -> None:
		...

	def FrameGeometry(self) -> None:
		...

	def FrameSize(self) -> None:
		...

	def GetAcceptDrops(self) -> None:
		...

	def GetAccessibleDescription(self) -> None:
		...

	def GetAccessibleName(self) -> None:
		...

	def GetAutoFillBackground(self) -> None:
		...

	def GetBaseSize(self) -> None:
		...

	def GetChildren(self) -> None:
		...

	def GetContextMenuPolicy(self) -> None:
		...

	def GetEnabled(self) -> None:
		...

	def GetFocusPolicy(self) -> None:
		...

	def GetFocusProxy(self) -> None:
		...

	def GetGeometry(self) -> None:
		...

	def GetHidden(self) -> None:
		...

	def GetItems(self) -> None:
		...

	def GetMaximumSize(self) -> None:
		...

	def GetMinimumSize(self) -> None:
		...

	def GetMouseTracking(self) -> None:
		...

	def GetSizeIncrement(self) -> None:
		...

	def GetStatusTip(self) -> None:
		...

	def GetStyleSheet(self) -> None:
		...

	def GetToolTip(self) -> None:
		...

	def GetToolTipDuration(self) -> None:
		...

	def GetUpdatesEnabled(self) -> None:
		...

	def GetVisible(self) -> None:
		...

	def GetWhatsThis(self) -> None:
		...

	def GetWindowFilePath(self) -> None:
		...

	def GetWindowFlags(self) -> None:
		...

	def GetWindowIconText(self) -> None:
		...

	def GetWindowModality(self) -> None:
		...

	def GetWindowOpacity(self) -> None:
		...

	def GetWindowRole(self) -> None:
		...

	def GetWindowState(self) -> None:
		...

	def GetWindowTitle(self) -> None:
		...

	def GrabKeyboard(self) -> None:
		...

	def GrabMouse(self) -> None:
		...

	def HasFocus(self) -> None:
		...

	def Height(self) -> None:
		...

	def Hide(self) -> None:
		...

	def IsActiveWindow(self) -> None:
		...

	def IsAncestorOf(self) -> None:
		...

	def IsEnabledTo(self) -> None:
		...

	def IsEnabledToTLW(self) -> None:
		...

	def IsFullScreen(self) -> None:
		...

	def IsMaximized(self) -> None:
		...

	def IsMinimized(self) -> None:
		...

	def IsModal(self) -> None:
		...

	def IsTopLevel(self) -> None:
		...

	def IsVisibleTo(self) -> None:
		...

	def IsWindow(self) -> None:
		...

	def KeyboardGrabber(self) -> None:
		...

	def Lower(self) -> None:
		...

	def MapFrom(self) -> None:
		...

	def MapFromGlobal(self) -> None:
		...

	def MapFromParent(self) -> None:
		...

	def MapTo(self) -> None:
		...

	def MapToGlobal(self) -> None:
		...

	def MapToParent(self) -> None:
		...

	def MinimumSizeHint(self) -> None:
		...

	def MouseGrabber(self) -> None:
		...

	def Move(self) -> None:
		...

	def NativeParentWidget(self) -> None:
		...

	def NextInFocusChain(self) -> None:
		...

	def NormalGeometry(self) -> None:
		...

	def OverrideWindowFlags(self) -> None:
		...

	def OverrideWindowState(self) -> None:
		...

	def ParentWidget(self) -> None:
		...

	def Pos(self) -> None:
		...

	def PreviousInFocusChain(self) -> None:
		...

	def QueueEvent(self) -> None:
		...

	def Raise(self) -> None:
		...

	def Rect(self) -> None:
		...

	def ReleaseKeyboard(self) -> None:
		...

	def ReleaseMouse(self) -> None:
		...

	def RemoveChild(self) -> None:
		...

	def Repaint(self) -> None:
		...

	def Resize(self) -> None:
		...

	def SetAcceptDrops(self) -> None:
		...

	def SetAccessibleDescription(self) -> None:
		...

	def SetAccessibleName(self) -> None:
		...

	def SetAttribute(self) -> None:
		...

	def SetAutoFillBackground(self) -> None:
		...

	def SetBaseSize(self) -> None:
		...

	def SetContextMenuPolicy(self) -> None:
		...

	def SetEnabled(self) -> None:
		...

	def SetFixedSize(self) -> None:
		...

	def SetFocus(self) -> None:
		...

	def SetFocusPolicy(self) -> None:
		...

	def SetFocusProxy(self) -> None:
		...

	def SetGeometry(self) -> None:
		...

	def SetHidden(self) -> None:
		...

	def SetMaximumSize(self) -> None:
		...

	def SetMinimumSize(self) -> None:
		...

	def SetMouseTracking(self) -> None:
		...

	def SetPaletteColor(self) -> None:
		...

	def SetParent(self) -> None:
		...

	def SetSizeIncrement(self) -> None:
		...

	def SetStatusTip(self) -> None:
		...

	def SetStyleSheet(self) -> None:
		...

	def SetTabOrder(self) -> None:
		...

	def SetToolTip(self) -> None:
		...

	def SetToolTipDuration(self) -> None:
		...

	def SetUpdatesEnabled(self) -> None:
		...

	def SetVisible(self) -> None:
		...

	def SetWhatsThis(self) -> None:
		...

	def SetWindowFilePath(self) -> None:
		...

	def SetWindowFlags(self) -> None:
		...

	def SetWindowIconText(self) -> None:
		...

	def SetWindowModality(self) -> None:
		...

	def SetWindowOpacity(self) -> None:
		...

	def SetWindowRole(self) -> None:
		...

	def SetWindowState(self) -> None:
		...

	def SetWindowTitle(self) -> None:
		...

	def Show(self) -> None:
		...

	def ShowFullScreen(self) -> None:
		...

	def ShowMaximized(self) -> None:
		...

	def ShowMinimized(self) -> None:
		...

	def ShowNormal(self) -> None:
		...

	def Size(self) -> None:
		...

	def SizeHint(self) -> None:
		...

	def StackUnder(self) -> None:
		...

	def TestAttribute(self) -> None:
		...

	def UnderMouse(self) -> None:
		...

	def Update(self) -> None:
		...

	def UpdateGeometry(self) -> None:
		...

	def Width(self) -> None:
		...

	def Window(self) -> None:
		...

	def WindowType(self) -> None:
		...

	def X(self) -> None:
		...

	def Y(self) -> None:
		...

