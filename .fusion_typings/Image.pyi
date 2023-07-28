from typing import Any

from ImgRectI import ImgRectI_
from IntPixel import IntPixel_
from FltPixel import FltPixel_
from TagList import TagList_
from ChanLUTs import ChanLUTs_
from LookUpTable import LookUpTable_
from ColorMatrix import ColorMatrix_
from ColorMatrixFull import ColorMatrixFull_
from Request import Request_
from MemBlock import MemBlock_
from _non_existing import void_, LookUpTable3D_


class Image_:

	#---Properties---#
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
	DataWindow: dict[Any, Any]
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

			1 - alpha only	8 bit integer
			2 - alpha only 16 bit integer
			3 - alpha only 16 bit float
			4 - alpha only 32 bit float
			5 - RGBA				8 bit integer
			6 - RGBA			 16 bit integer
			7 - RGBA			 16 bit float
			8 - RGBA			 32 bit float

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
	ImageWindow: ImgRectI_
	"""
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
	PixelSize: int
	"""
	Read/Write
	"""
	ValidWindow: ImgRectI_
	"""
	Read Only
	"""
	YScale: int
	"""
	Pixel Y Aspect

	Read Only
	"""
	Width: int
	"""
	Actual image width, in pixels

	Read Only
	"""
	ProxyScale: int
	"""
	Image proxy scale multiplier

			ProxyScale may be any positive integer, where 1 indicates no proxy.

	Read Only
	"""
	XOffset: int
	"""
	Image X Offset

	Read Only
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
	def SampleAreaBInt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: IntPixel_) -> None:
		...
	def SampleAreaDFlt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: FltPixel_) -> None:
		...
	def SampleAreaDInt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: IntPixel_) -> None:
		...
	def SampleAreaMFlt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: FltPixel_) -> None:
		...
	def Transform(self, dest: Image_, tags: TagList_) -> Image_:
		...
	def SampleAreaMInt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: IntPixel_) -> None:
		...
	def Resize(self, dest: Image_, tags: TagList_) -> Image_:
		...
	def SampleAreaWFlt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: FltPixel_) -> None:
		...
	def SampleAreaWInt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: IntPixel_) -> None:
		...
	def SamplePixelBFlt(self, x: float, y: float, p: FltPixel_) -> None:
		...
	def SamplePixelBInt(self, x: float, y: float, p: IntPixel_) -> None:
		...
	def SamplePixelDFlt(self, x: float, y: float, p: FltPixel_) -> None:
		...
	def MergeOf(self, fg: Image_, tags: TagList_) -> Image_:
		...
	def Clear(self) -> None:
		...
	def SamplePixelMFlt(self, x: float, y: float, p: FltPixel_) -> None:
		...
	def SamplePixelMInt(self, x: float, y: float, p: IntPixel_) -> None:
		...
	def SamplePixelWFlt(self, x: float, y: float, p: FltPixel_) -> None:
		...
	def SamplePixelWInt(self, x: float, y: float, p: IntPixel_) -> None:
		...
	def Saturate(self, rs: float, gs: float, bs: float) -> None:
		...
	def GainOf(self, r: float, g: float, b: float, a: float, tags: TagList_) -> Image_:
		...
	def Gamma(self, rg: float, gg: float, bg: float, ag: float) -> None:
		...
	def GetCanvasColorFlt(self, p: FltPixel_) -> None:
		...
	def OpenClose(self, dest: Image_, tags: TagList_) -> Image_:
		...
	def GetCanvasColorInt(self, p: IntPixel_) -> None:
		...
	def GetChanLUTs(self) -> ChanLUTs_:
		...
	def GetChanOffset(self) -> int:
		...
	def SetPixelFlt(self, x: int, y: int, pix: FltPixel_) -> None:
		...
	def GetChanType(self) -> int:
		...
	def SetPixelInt(self, x: int, y: int, pix: IntPixel_) -> None:
		...
	def GetPixelFlt(self, x: int, y: int, pix: FltPixel_) -> None:
		...
	def GetPixelInt(self, x: int, y: int, pix: IntPixel_) -> None:
		...
	def GetScanLine(self) -> int:
		...
	def GetScanLineAux(self) -> int:
		...
	def ErodeDilate(self, dest: Image_, tags: TagList_) -> Image_:
		...
	def IsAFlt16(self) -> bool:
		...
	def _new_TagList(self, tags: TagList_) -> Image_:
		...
	def IsAFlt32(self) -> bool:
		...
	def SetCanvasColorFlt(self, p: FltPixel_) -> None:
		...
	def AllocScanLineData(self) -> bool:
		...
	def _GetChanSizeStr(self, chanstr: str) -> int:
		...
	def AlphaDivide(self, dest: Image_) -> None:
		...
	def _GetChanSizeNum(self, chan: int) -> int:
		...
	def AlphaMultiply(self, dest: Image_) -> None:
		...
	def _FromMemory(self, _ptr: void_, fmt: str, topdown: bool) -> None:
		...
	def ApplyLookUpTable(self, lutr: LookUpTable_, lutg: LookUpTable_, lutb: LookUpTable_, luta: LookUpTable_) -> None:
		...
	def header_text(self) -> None:
		...
	def IsFloat128(self) -> bool:
		...
	def _ApplyMatrixCM(self, dest: Image_, cm: ColorMatrix_, tags: TagList_) -> Image_:
		...
	def IsFloat64(self) -> bool:
		...
	def _ApplyMatrixOfCMF(self, cm: ColorMatrixFull_, tags: TagList_) -> Image_:
		...
	def ApplyLookUpTable3D(self, lutr: LookUpTable3D_, lutg: LookUpTable3D_, lutb: LookUpTable3D_) -> None:
		...
	def _BlendOf(self, fg: Image_, map: Image_, blend: float) -> Image_:
		...
	def IsInt(self) -> bool:
		...
	def _ChannelOpOf(self, op: str, img: Image_, funcs: str, data: float, a1: float, a2: float) -> Image_:
		...
	def CSConvert(self, fromstr: str, tostr: str) -> None:
		...
	def _ApplyMatrixOfCM(self, cm: ColorMatrix_, tags: TagList_) -> Image_:
		...
	def IsInt64(self) -> bool:
		...
	def _ApplyMatrixCMF(self, dest: Image_, cm: ColorMatrixFull_, tags: TagList_) -> Image_:
		...
	def CheckAbort(self) -> bool:
		...
	def _FromHexString(self, str: str) -> None:
		...
	def IsRGBAFlt128(self) -> bool:
		...
	def CopyField(self, fromfield: int, dest: Image_, tofield: int, interp: int) -> Image_:
		...
	def IsRGBAFlt64(self) -> bool:
		...
	def UseSAT(self) -> bool:
		...
	def IsRGBAInt32(self) -> bool:
		...
	def SetGPUMemDirtyFlag(self, dirty: bool) -> None:
		...
	def CopyOf(self, tags: TagList_) -> Image_:
		...
	def SetCanvasColorInt(self, p: IntPixel_) -> None:
		...
	def IsReadOnly(self) -> bool:
		...
	def DownloadGPUMem(self, req: Request_) -> bool:
		...
	def IsReadOnlyAux(self) -> bool:
		...
	def _new_MemBlock(self, mb: MemBlock_) -> Image_:
		...
	def IsSimple(self) -> bool:
		...
	def SamplePixelDInt(self, x: float, y: float, p: IntPixel_) -> None:
		...
	def LegalOf(self, vidmode: int, method: int, amplitude: float, softclip: float) -> Image_:
		...
	def FillInt(self, p: IntPixel_, tags: TagList_) -> None:
		...
	def HasChannel(self, chan: int) -> bool:
		...
	def Gain(self, rg: float, gg: float, bg: float, ag: float) -> None:
		...
	def IsRGBAInt64(self) -> bool:
		...
	def MakeLookUpTableOf(self) -> Image_:
		...
	def Crop(self, dest: Image_, tags: TagList_) -> Image_:
		...
	def IsAInt16(self) -> bool:
		...
	def info_text(self) -> None:
		...
	def IsAInt8(self) -> bool:
		...
	def OMerge(self, img: Image_, x: float, y: float) -> None:
		...
	def IsDeep(self) -> bool:
		...
	def OXMerge(self, img: Image_, x: float, y: float) -> None:
		...
	def IsFloat(self) -> bool:
		...
	def IsInt32(self) -> bool:
		...
	def RecycleSAT(self) -> None:
		...
	def FillFlt(self, p: FltPixel_, tags: TagList_) -> None:
		...
	def IsMask(self) -> bool:
		...
	def ReverseFieldDominance(self, shiftup: bool) -> None:
		...
	def Blur(self, dest: Image_, tags: TagList_) -> Image_:
		...
	def IsGPUMemDirty(self) -> bool:
		...
	def SampleAreaBFlt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: FltPixel_) -> None:
		...
	def Merge(self, fg: Image_, tags: TagList_) -> None:
		...

Image = Image_