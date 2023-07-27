from typing import Any

from ImgRectI import _ImgRectI
from IntPixel import _IntPixel
from FltPixel import _FltPixel
from TagList import _TagList
from ChanLUTs import _ChanLUTs
from LookUpTable import _LookUpTable
from ColorMatrix import _ColorMatrix
from ColorMatrixFull import _ColorMatrixFull
from Request import _Request
from MemBlock import _MemBlock
from _non_existing import _void, _LookUpTable3D


class _Image:

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
	ImageWindow: _ImgRectI
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
	ValidWindow: _ImgRectI
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
	def SampleAreaBInt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: _IntPixel) -> None:
		...
	def SampleAreaDFlt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: _FltPixel) -> None:
		...
	def SampleAreaDInt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: _IntPixel) -> None:
		...
	def SampleAreaMFlt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: _FltPixel) -> None:
		...
	def Transform(self, dest: _Image, tags: _TagList) -> _Image:
		...
	def SampleAreaMInt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: _IntPixel) -> None:
		...
	def Resize(self, dest: _Image, tags: _TagList) -> _Image:
		...
	def SampleAreaWFlt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: _FltPixel) -> None:
		...
	def SampleAreaWInt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: _IntPixel) -> None:
		...
	def SamplePixelBFlt(self, x: float, y: float, p: _FltPixel) -> None:
		...
	def SamplePixelBInt(self, x: float, y: float, p: _IntPixel) -> None:
		...
	def SamplePixelDFlt(self, x: float, y: float, p: _FltPixel) -> None:
		...
	def MergeOf(self, fg: _Image, tags: _TagList) -> _Image:
		...
	def Clear(self) -> None:
		...
	def SamplePixelMFlt(self, x: float, y: float, p: _FltPixel) -> None:
		...
	def SamplePixelMInt(self, x: float, y: float, p: _IntPixel) -> None:
		...
	def SamplePixelWFlt(self, x: float, y: float, p: _FltPixel) -> None:
		...
	def SamplePixelWInt(self, x: float, y: float, p: _IntPixel) -> None:
		...
	def Saturate(self, rs: float, gs: float, bs: float) -> None:
		...
	def GainOf(self, r: float, g: float, b: float, a: float, tags: _TagList) -> _Image:
		...
	def Gamma(self, rg: float, gg: float, bg: float, ag: float) -> None:
		...
	def GetCanvasColorFlt(self, p: _FltPixel) -> None:
		...
	def OpenClose(self, dest: _Image, tags: _TagList) -> _Image:
		...
	def GetCanvasColorInt(self, p: _IntPixel) -> None:
		...
	def GetChanLUTs(self) -> _ChanLUTs:
		...
	def GetChanOffset(self) -> int:
		...
	def SetPixelFlt(self, x: int, y: int, pix: _FltPixel) -> None:
		...
	def GetChanType(self) -> int:
		...
	def SetPixelInt(self, x: int, y: int, pix: _IntPixel) -> None:
		...
	def GetPixelFlt(self, x: int, y: int, pix: _FltPixel) -> None:
		...
	def GetPixelInt(self, x: int, y: int, pix: _IntPixel) -> None:
		...
	def GetScanLine(self) -> int:
		...
	def GetScanLineAux(self) -> int:
		...
	def ErodeDilate(self, dest: _Image, tags: _TagList) -> _Image:
		...
	def IsAFlt16(self) -> bool:
		...
	def _new_TagList(self, tags: _TagList) -> _Image:
		...
	def IsAFlt32(self) -> bool:
		...
	def SetCanvasColorFlt(self, p: _FltPixel) -> None:
		...
	def AllocScanLineData(self) -> bool:
		...
	def _GetChanSizeStr(self, chanstr: str) -> int:
		...
	def AlphaDivide(self, dest: _Image) -> None:
		...
	def _GetChanSizeNum(self, chan: int) -> int:
		...
	def AlphaMultiply(self, dest: _Image) -> None:
		...
	def _FromMemory(self, _ptr: _void, fmt: str, topdown: bool) -> None:
		...
	def ApplyLookUpTable(self, lutr: _LookUpTable, lutg: _LookUpTable, lutb: _LookUpTable, luta: _LookUpTable) -> None:
		...
	def header_text(self):
		...
	def IsFloat128(self) -> bool:
		...
	def _ApplyMatrixCM(self, dest: _Image, cm: _ColorMatrix, tags: _TagList) -> _Image:
		...
	def IsFloat64(self) -> bool:
		...
	def _ApplyMatrixOfCMF(self, cm: _ColorMatrixFull, tags: _TagList) -> _Image:
		...
	def ApplyLookUpTable3D(self, lutr: _LookUpTable3D, lutg: _LookUpTable3D, lutb: _LookUpTable3D) -> None:
		...
	def _BlendOf(self, fg: _Image, map: _Image, blend: float) -> _Image:
		...
	def IsInt(self) -> bool:
		...
	def _ChannelOpOf(self, op: str, img: _Image, funcs: str, data: float, a1: float, a2: float) -> _Image:
		...
	def CSConvert(self, fromstr: str, tostr: str) -> None:
		...
	def _ApplyMatrixOfCM(self, cm: _ColorMatrix, tags: _TagList) -> _Image:
		...
	def IsInt64(self) -> bool:
		...
	def _ApplyMatrixCMF(self, dest: _Image, cm: _ColorMatrixFull, tags: _TagList) -> _Image:
		...
	def CheckAbort(self) -> bool:
		...
	def _FromHexString(self, str: str) -> None:
		...
	def IsRGBAFlt128(self) -> bool:
		...
	def CopyField(self, fromfield: int, dest: _Image, tofield: int, interp: int) -> _Image:
		...
	def IsRGBAFlt64(self) -> bool:
		...
	def UseSAT(self) -> bool:
		...
	def IsRGBAInt32(self) -> bool:
		...
	def SetGPUMemDirtyFlag(self, dirty: bool) -> None:
		...
	def CopyOf(self, tags: _TagList) -> _Image:
		...
	def SetCanvasColorInt(self, p: _IntPixel) -> None:
		...
	def IsReadOnly(self) -> bool:
		...
	def DownloadGPUMem(self, req: _Request) -> bool:
		...
	def IsReadOnlyAux(self) -> bool:
		...
	def _new_MemBlock(self, mb: _MemBlock) -> _Image:
		...
	def IsSimple(self) -> bool:
		...
	def SamplePixelDInt(self, x: float, y: float, p: _IntPixel) -> None:
		...
	def LegalOf(self, vidmode: int, method: int, amplitude: float, softclip: float) -> _Image:
		...
	def FillInt(self, p: _IntPixel, tags: _TagList) -> None:
		...
	def HasChannel(self, chan: int) -> bool:
		...
	def Gain(self, rg: float, gg: float, bg: float, ag: float) -> None:
		...
	def IsRGBAInt64(self) -> bool:
		...
	def MakeLookUpTableOf(self) -> _Image:
		...
	def Crop(self, dest: _Image, tags: _TagList) -> _Image:
		...
	def IsAInt16(self) -> bool:
		...
	def info_text(self):
		...
	def IsAInt8(self) -> bool:
		...
	def OMerge(self, img: _Image, x: float, y: float) -> None:
		...
	def IsDeep(self) -> bool:
		...
	def OXMerge(self, img: _Image, x: float, y: float) -> None:
		...
	def IsFloat(self) -> bool:
		...
	def IsInt32(self) -> bool:
		...
	def RecycleSAT(self) -> None:
		...
	def FillFlt(self, p: _FltPixel, tags: _TagList) -> None:
		...
	def IsMask(self) -> bool:
		...
	def ReverseFieldDominance(self, shiftup: bool) -> None:
		...
	def Blur(self, dest: _Image, tags: _TagList) -> _Image:
		...
	def IsGPUMemDirty(self) -> bool:
		...
	def SampleAreaBFlt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: _FltPixel) -> None:
		...
	def Merge(self, fg: _Image, tags: _TagList) -> None:
		...

Image = _Image