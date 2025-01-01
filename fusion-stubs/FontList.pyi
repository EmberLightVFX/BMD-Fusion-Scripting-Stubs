from typing import Any

class FontList:

	#---Registry---#
	REGI_ClassType: int

	REGB_ControlView: bool

	REGB_Hide: bool

	REGS_ID: str

	REGS_Name: str

	REGI_Priority: int

	REGB_SupportsDoD: bool

	REGB_Unpredictable: bool

	REGI_Version: int

	REGS_VersionString: str


	#---Methods---#
	def AddFont(self, fontfile: str) -> bool:
		"""
		Adds the specified font to the global font list

		where fontfile is the full path to a font to be added.

		Args:
			fontfile (str)

		Returns:
			success (bool)
		"""
		...

	def Clear(self) -> None:
		"""
		Empties the global font list
		"""
		...

	def GetFontList(self) -> dict[Any, Any]:
		"""
		Returns all font files in the global font list

		where fonts is a table of subtables, indexed by font name,
		and each subtable contains filename strings, indexed by style name.

		Returns:
			fonts (dict[Any, Any])
		"""
		...

	def ScanDir(self, dirname: str | None = None) -> None:
		"""
		Adds the specified dir to the global font list

		where dirname is the full path to a directory of fonts to add.
		If dirname is not specified, the list will be cleared and the standard
		font directory will be rescanned.

		Args:
			dirname (Optional[str])
		"""
		...

	def GetFontManager(self) -> FontList:
		...

