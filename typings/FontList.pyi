from typing import Any

from FontList import _FontList


class _FontList:

	#---Attributes---#
	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGS_Name: str

	REGI_Version: int

	REGI_ClassType: int

	REGB_Unpredictable: bool

	REGS_VersionString: str

	REGS_ID: str

	REGB_ControlView: bool

	REGI_Priority: int


	#---Methods---#
	def ScanDir(self, dirname: str = str()) -> None:
		"""
		Adds the specified dir to the global font list

		where dirname is the full path to a directory of fonts to add.
		If dirname is not specified, the list will be cleared and the standard
		font directory will be rescanned.
		"""
		...
	def info_text(self):
		...
	def Clear(self) -> None:
		"""
		Empties the global font list
		"""
		...
	def header_text(self):
		...
	def AddFont(self, fontfile: str) -> bool:
		"""
		Adds the specified font to the global font list

		where fontfile is the full path to a font to be added.
		"""
		...
	def GetFontManager(self) -> _FontList:
		...
	def GetFontList(self) -> dict[Any, Any]:
		"""
		Returns all font files in the global font list

		where fonts is a table of subtables, indexed by font name,
		and each subtable contains filename strings, indexed by style name.
		"""
		...

FontList = _FontList