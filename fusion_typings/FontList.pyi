from typing import Any

class FontList_:

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	def AddFont(self, fontfile: str) -> bool:
		"""
		Adds the specified font to the global font list

		where fontfile is the full path to a font to be added.
		"""
		...
	def GetFontList(self) -> dict[Any, Any]:
		"""
		Returns all font files in the global font list

		where fonts is a table of subtables, indexed by font name,
		and each subtable contains filename strings, indexed by style name.
		"""
		...
	def GetFontManager(self) -> FontList_:
		...
	def header_text(self):
		...
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

FontList = FontList_