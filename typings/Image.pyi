from typing import Any

from ImgRectI import _ImgRectI
from FltPixel import _FltPixel
from Image import _Image
from IntPixel import _IntPixel
from TagList import _TagList
from ColorMatrixFull import _ColorMatrixFull
from ColorMatrix import _ColorMatrix
from LookUpTable import _LookUpTable
from void import _void
from LookUpTable3D import _LookUpTable3D
from Request import _Request
from ChanLUTs import _ChanLUTs
from MemBlock import _MemBlock


class _Image:

	#---Properties---#
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
	ProxyScale: int
	"""
	Image proxy scale multiplier

			ProxyScale may be any positive integer, where 1 indicates no proxy.

	Read Only
	"""
	ValidWindow: _ImgRectI
	"""
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
	DataWindow: dict[Any, Any]
	"""
	Rectangle of valid data pixels, in a table

			Data rectangle coordinates are stored as four entries in a table, in the format
			{ <left>, <bottom>, <right>, <top> }

	Read Only
	"""
	YScale: int
	"""
	Pixel Y Aspect

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

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGS_VersionString: str

	REGI_ClassType: int

	REGI_Priority: int

	REGB_ControlView: bool

	REGS_ID: str

	REGB_Utility_Toggle: bool

	REGB_Unpredictable: bool


	#---Methods---#
	def IsInt64(self) -> bool:
		...
	def IsMask(self) -> bool:
		...
	def IsRGBAFlt128(self) -> bool:
		...
	def Saturate(self, rs: float, gs: float, bs: float) -> None:
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
	def SetPixelFlt(self, x: int, y: int, pix: _FltPixel) -> None:
		...
	def LegalOf(self, vidmode: int, method: int, amplitude: float, softclip: float) -> _Image:
		...
	def SetPixelInt(self, x: int, y: int, pix: _IntPixel) -> None:
		...
	def Crop(self, dest: _Image, tags: _TagList) -> _Image:
		...
	def UseSAT(self) -> bool:
		...
	def MakeLookUpTableOf(self) -> _Image:
		...
	def info_text(self):
		...
	def _ApplyMatrixCMF(self, dest: _Image, cm: _ColorMatrixFull, tags: _TagList) -> _Image:
		...
	def OMerge(self, img: _Image, x: float, y: float) -> None:
		...
	def _ApplyMatrixOfCM(self, cm: _ColorMatrix, tags: _TagList) -> _Image:
		...
	def OXMerge(self, img: _Image, x: float, y: float) -> None:
		...
	def _ApplyMatrixOfCMF(self, cm: _ColorMatrixFull, tags: _TagList) -> _Image:
		...
	def RecycleSAT(self) -> None:
		...
	def MergeOf(self, fg: _Image, tags: _TagList) -> _Image:
		...
	def ReverseFieldDominance(self, shiftup: bool) -> None:
		...
	def Merge(self, fg: _Image, tags: _TagList) -> None:
		...
	def SampleAreaBFlt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: _FltPixel) -> None:
		...
	def AlphaMultiply(self, dest: _Image) -> None:
		...
	def ApplyLookUpTable(self, lutr: _LookUpTable, lutg: _LookUpTable, lutb: _LookUpTable, luta: _LookUpTable) -> None:
		...
	def Clear(self) -> None:
		...
	def _FromMemory(self, _ptr: _void, fmt: str, topdown: bool) -> None:
		...
	def ApplyLookUpTable3D(self, lutr: _LookUpTable3D, lutg: _LookUpTable3D, lutb: _LookUpTable3D) -> None:
		...
	def SampleAreaBInt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: _IntPixel) -> None:
		...
	def SampleAreaDFlt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: _FltPixel) -> None:
		...
	def CSConvert(self, fromstr: str, tostr: str) -> None:
		...
	def SampleAreaDInt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: _IntPixel) -> None:
		...
	def SampleAreaMFlt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: _FltPixel) -> None:
		...
	def CheckAbort(self) -> bool:
		...
	def SampleAreaMInt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: _IntPixel) -> None:
		...
	def CopyField(self, fromfield: int, dest: _Image, tofield: int, interp: int) -> _Image:
		...
	def SampleAreaWInt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: _IntPixel) -> None:
		...
	def Transform(self, dest: _Image, tags: _TagList) -> _Image:
		...
	def SamplePixelBFlt(self, x: float, y: float, p: _FltPixel) -> None:
		...
	def CopyOf(self, tags: _TagList) -> _Image:
		...
	def SamplePixelBInt(self, x: float, y: float, p: _IntPixel) -> None:
		...
	def DownloadGPUMem(self, req: _Request) -> bool:
		...
	def SamplePixelDInt(self, x: float, y: float, p: _IntPixel) -> None:
		...
	def FillFlt(self, p: _FltPixel, tags: _TagList) -> None:
		...
	def SamplePixelMFlt(self, x: float, y: float, p: _FltPixel) -> None:
		...
	def FillInt(self, p: _IntPixel, tags: _TagList) -> None:
		...
	def Gain(self, rg: float, gg: float, bg: float, ag: float) -> None:
		...
	def SamplePixelWInt(self, x: float, y: float, p: _IntPixel) -> None:
		...
	def header_text(self):
		...
	def GainOf(self, r: float, g: float, b: float, a: float, tags: _TagList) -> _Image:
		...
	def Gamma(self, rg: float, gg: float, bg: float, ag: float) -> None:
		...
	def GetCanvasColorFlt(self, p: _FltPixel) -> None:
		...
	def GetCanvasColorInt(self, p: _IntPixel) -> None:
		...
	def _new_TagList(self, tags: _TagList) -> _Image:
		...
	def GetChanLUTs(self) -> _ChanLUTs:
		...
	def _new_MemBlock(self, mb: _MemBlock) -> _Image:
		...
	def GetChanOffset(self) -> int:
		...
	def _GetChanSizeStr(self, chanstr: str) -> int:
		...
	def GetChanType(self) -> int:
		...
	def ErodeDilate(self, dest: _Image, tags: _TagList) -> _Image:
		...
	def GetPixelFlt(self, x: int, y: int, pix: _FltPixel) -> None:
		...
	def _GetChanSizeNum(self, chan: int) -> int:
		...
	def _FromHexString(self, str: str) -> None:
		...
	def GetPixelInt(self, x: int, y: int, pix: _IntPixel) -> None:
		...
	def _ChannelOpOf(self, op: str, img: _Image, funcs: str, data: float, a1: float, a2: float) -> _Image:
		...
	def GetScanLine(self) -> int:
		...
	def _BlendOf(self, fg: _Image, map: _Image, blend: float) -> _Image:
		...
	def GetScanLineAux(self) -> int:
		...
	def _ApplyMatrixCM(self, dest: _Image, cm: _ColorMatrix, tags: _TagList) -> _Image:
		...
	def HasChannel(self, chan: int) -> bool:
		...
	def SetGPUMemDirtyFlag(self, dirty: bool) -> None:
		...
	def SetCanvasColorInt(self, p: _IntPixel) -> None:
		...
	def IsAFlt16(self) -> bool:
		...
	def SetCanvasColorFlt(self, p: _FltPixel) -> None:
		...
	def IsAFlt32(self) -> bool:
		...
	def SamplePixelWFlt(self, x: float, y: float, p: _FltPixel) -> None:
		...
	def IsAInt16(self) -> bool:
		...
	def SamplePixelMInt(self, x: float, y: float, p: _IntPixel) -> None:
		...
	def IsAInt8(self) -> bool:
		...
	def Resize(self, dest: _Image, tags: _TagList) -> _Image:
		...
	def IsDeep(self) -> bool:
		...
	def SamplePixelDFlt(self, x: float, y: float, p: _FltPixel) -> None:
		...
	def IsFloat(self) -> bool:
		...
	def SampleAreaWFlt(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, p: _FltPixel) -> None:
		...
	def IsFloat128(self) -> bool:
		...
	def AllocScanLineData(self) -> bool:
		...
	def OpenClose(self, dest: _Image, tags: _TagList) -> _Image:
		...
	def Blur(self, dest: _Image, tags: _TagList) -> _Image:
		...
	def IsGPUMemDirty(self) -> bool:
		...
	def IsFloat64(self) -> bool:
		...
	def IsInt(self) -> bool:
		...
	def AlphaDivide(self, dest: _Image) -> None:
		...
	def IsInt32(self) -> bool:
		...

Image = _Image