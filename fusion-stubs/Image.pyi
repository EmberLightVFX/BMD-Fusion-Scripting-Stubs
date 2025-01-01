from typing import Any

from Request import Request
from FltPixel import FltPixel
from IntPixel import IntPixel
from ColorMatrix import ColorMatrix
from TagList import TagList
from MemBlock import MemBlock
from ColorMatrixFull import ColorMatrixFull
from ImgRectI import ImgRectI
from LookUpTable import LookUpTable
from ChanLUTs import ChanLUTs
from _non_existing import void, LookUpTable3D


class Image:

	#---Properties---#
	DataWindow: list[int]
	"""
	Rectangle of valid data pixels, in a table

	Data rectangle coordinates are stored as four entries in a table, in the format
	{ <left>, <bottom>, <right>, <top> }

	Read Only
	"""

	Depth: int
	"""
	Image depth indicator (not in bits)

	Depth will be one of the following values:
	
	1 - alpha only  8 bit integer
	2 - alpha only 16 bit integer
	3 - alpha only 16 bit float
	4 - alpha only 32 bit float
	5 - RGBA        8 bit integer
	6 - RGBA       16 bit integer
	7 - RGBA       16 bit float
	8 - RGBA       32 bit float

	Read Only
	"""

	Field: int
	"""
	Field indicator

	Field will be one of the following values:
	
	-1 - Full Frames, no fields
	0 - Odd (NTSC) field
	1 - Even (PAL/HD) field

	Read Only
	"""

	Height: int
	"""
	Actual image height, in pixels

	Read Only
	"""

	OriginalHeight: int
	"""
	Unproxied image height, in pixels

	Read Only
	"""

	OriginalWidth: int
	"""
	Unproxied image width, in pixels

	Read Only
	"""

	OriginalXScale: int
	"""
	Unproxied pixel X Aspect

	Read Only
	"""

	OriginalYScale: int
	"""
	Unproxied pixel Y Aspect

	Read Only
	"""

	ProxyScale: int
	"""
	Image proxy scale multiplier

	ProxyScale may be any positive integer, where 1 indicates no proxy.

	Read Only
	"""

	Width: int
	"""
	Actual image width, in pixels

	Read Only
	"""

	XOffset: int
	"""
	Image X Offset

	Read Only
	"""

	XScale: int
	"""
	Pixel X Aspect

	Read Only
	"""

	YOffset: int
	"""
	Image X Offset

	Read Only
	"""

	YScale: int
	"""
	Pixel Y Aspect

	Read Only
	"""

	ImageWindow: ImgRectI
	"""
	Read Only
	"""

	PixelSize: int

	ValidWindow: ImgRectI
	"""
	Read Only
	"""


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
	def AllocScanLineData(self) -> bool:
		...

	def AlphaDivide(self, dest: Image) -> None:
		...

	def AlphaMultiply(self, dest: Image) -> None:
		...

	def ApplyLookUpTable(self, lutr: LookUpTable, lutg: LookUpTable, lutb: LookUpTable, luta: LookUpTable) -> None:
		...

	def ApplyLookUpTable3D(self, lutr: LookUpTable3D, lutg: LookUpTable3D, lutb: LookUpTable3D) -> None:
		...

	def Blur(self, dest: Image, tags: TagList) -> Image:
		...

	def CSConvert(self, fromstr: str, tostr: str) -> None:
		...

	def CheckAbort(self) -> bool:
		...

	def Clear(self) -> None:
		...

	def CopyField(self, fromfield: int, dest: Image, tofield: int, interp: int) -> Image:
		...

	def CopyOf(self, tags: TagList) -> Image:
		...

	def Crop(self, dest: Image, tags: TagList) -> Image:
		...

	def DownloadGPUMem(self, req: Request) -> bool:
		...

	def ErodeDilate(self, dest: Image, tags: TagList) -> Image:
		...

	def FillFlt(self, p: FltPixel, tags: TagList) -> None:
		...

	def FillInt(self, p: IntPixel, tags: TagList) -> None:
		...

	def Gain(self, rg: float, gg: float, bg: float, ag: float) -> None:
		...

	def GainOf(self, r: float, g: float, b: float, a: float, tags: TagList) -> Image:
		...

	def Gamma(self, rg: float, gg: float, bg: float, ag: float) -> None:
		...

	def GetCanvasColorFlt(self, p: FltPixel) -> None:
		...

	def GetCanvasColorInt(self, p: IntPixel) -> None:
		...

	def GetChanLUTs(self) -> ChanLUTs:
		...

	def GetChanOffset(self) -> int:
		...

	def GetChanType(self) -> int:
		...

	def GetPixelFlt(self, x: int, y: int, pix: FltPixel) -> None:
		...

	def GetPixelInt(self, x: int, y: int, pix: IntPixel) -> None:
		...

	def GetScanLine(self) -> int:
		...

	def GetScanLineAux(self) -> int:
		...

	def HasChannel(self, chan: int) -> bool:
		...

	def IsAFlt16(self) -> bool:
		...

	def IsAFlt32(self) -> bool:
		...

	def IsAInt16(self) -> bool:
		...

	def IsAInt8(self) -> bool:
		...

	def IsDeep(self) -> bool:
		...

	def IsFloat(self) -> bool:
		...

	def IsFloat128(self) -> bool:
		...

	def IsFloat64(self) -> bool:
		...

	def IsGPUMemDirty(self) -> bool:
		...

	def IsInt(self) -> bool:
		...

	def IsInt32(self) -> bool:
		...

	def IsInt64(self) -> bool:
		...

	def IsMask(self) -> bool:
		...

	def IsRGBAFlt128(self) -> bool:
		...

	def IsRGBAFlt64(self) -> bool:
		...

	def IsRGBAInt32(self) -> bool:
		...

	def IsRGBAInt64(self) -> bool:
		...

	def IsReadOnly(self) -> bool:
		...

	def IsReadOnlyAux(self) -> bool:
		...

	def IsSimple(self) -> bool:
		...

	def LegalOf(self, vidmode: int, method: int, amplitude: float, softclip: float) -> Image:
		...

	def MakeLookUpTableOf(self) -> Image:
		...

	def Merge(self, fg: Image, tags: TagList) -> None:
		...

	def MergeOf(self, fg: Image, tags: TagList) -> Image:
		...

	def OMerge(self, img: Image, x: float, y: float) -> None:
		...

	def OXMerge(self, img: Image, x: float, y: float) -> None:
		...

	def OpenClose(self, dest: Image, tags: TagList) -> Image:
		...

	def RecycleSAT(self) -> None:
		...

	def Resize(self, dest: Image, tags: TagList) -> Image:
		...

	def ReverseFieldDominance(self, shiftup: bool) -> None:
		...

	def SampleAreaBFlt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: FltPixel) -> None:
		...

	def SampleAreaBInt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: IntPixel) -> None:
		...

	def SampleAreaDFlt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: FltPixel) -> None:
		...

	def SampleAreaDInt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: IntPixel) -> None:
		...

	def SampleAreaMFlt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: FltPixel) -> None:
		...

	def SampleAreaMInt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: IntPixel) -> None:
		...

	def SampleAreaWFlt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: FltPixel) -> None:
		...

	def SampleAreaWInt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: IntPixel) -> None:
		...

	def SamplePixelBFlt(self, x: float, y: float, p: FltPixel) -> None:
		...

	def SamplePixelBInt(self, x: float, y: float, p: IntPixel) -> None:
		...

	def SamplePixelDFlt(self, x: float, y: float, p: FltPixel) -> None:
		...

	def SamplePixelDInt(self, x: float, y: float, p: IntPixel) -> None:
		...

	def SamplePixelMFlt(self, x: float, y: float, p: FltPixel) -> None:
		...

	def SamplePixelMInt(self, x: float, y: float, p: IntPixel) -> None:
		...

	def SamplePixelWFlt(self, x: float, y: float, p: FltPixel) -> None:
		...

	def SamplePixelWInt(self, x: float, y: float, p: IntPixel) -> None:
		...

	def Saturate(self, rs: float, gs: float, bs: float) -> None:
		...

	def SetCanvasColorFlt(self, p: FltPixel) -> None:
		...

	def SetCanvasColorInt(self, p: IntPixel) -> None:
		...

	def SetGPUMemDirtyFlag(self, dirty: bool) -> None:
		...

	def SetPixelFlt(self, x: int, y: int, pix: FltPixel) -> None:
		...

	def SetPixelInt(self, x: int, y: int, pix: IntPixel) -> None:
		...

	def Transform(self, dest: Image, tags: TagList) -> Image:
		...

	def UseSAT(self) -> bool:
		...

	def _ApplyMatrixCM(self, dest: Image, cm: ColorMatrix, tags: TagList) -> Image:
		...

	def _ApplyMatrixCMF(self, dest: Image, cm: ColorMatrixFull, tags: TagList) -> Image:
		...

	def _ApplyMatrixOfCM(self, cm: ColorMatrix, tags: TagList) -> Image:
		...

	def _ApplyMatrixOfCMF(self, cm: ColorMatrixFull, tags: TagList) -> Image:
		...

	def _BlendOf(self, fg: Image, map: Image, blend: float) -> Image:
		...

	def _ChannelOpOf(self, op: str, img: Image, funcs: str, data: float, a1: float, a2: float) -> Image:
		...

	def _FromHexString(self, str: str) -> None:
		...

	def _FromMemory(self, _ptr: void, fmt: str, topdown: bool) -> None:
		...

	def _GetChanSizeNum(self, chan: int) -> int:
		...

	def _GetChanSizeStr(self, chanstr: str) -> int:
		...

	def _new_MemBlock(self, mb: MemBlock) -> Image:
		...

	def _new_TagList(self, tags: TagList) -> Image:
		...

