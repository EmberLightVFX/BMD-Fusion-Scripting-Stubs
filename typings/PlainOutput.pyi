from typing import Any

from Parameter import _Parameter


class _PlainOutput:

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
	def GetConnectedInputs(self):
		...
	def ShowDiskCacheDlg(self) -> bool:
		"""
		Displays Cache-To-Disk dialog for user interaction

		Returns: boolean ok - true if user clicked OK/Pre-Render, false for Cancel
		"""
		...
	def GetValue(self, time: int = int(), flags: int = int(), proxy: int = int()) -> tuple[_Parameter, dict[Any, Any]]:
		"""
		Returns the value at the given time

		Args:
			time:		 The frame to fetch the value for (default is the current time).
			reqflags: Quality flags (default is final quality).
			proxy:		Proxy level (default is no proxy).

		Returns:
			value may be nil, or a number of different types:
				 Number - returns a number
				 Point	- returns a table with X and Y members
				 Text	 - returns a string
				 Clip	 - returns the filename string
				 Image	- returns an Image object
		 attrs is a table with the following entries:
				 Valid		- table with Start and End entries
				 DataType - string ID for the parameter type
				 TimeCost - time take to render this parameter
				 DoD			- table of { left,bottom,right,top } coords
		"""
		...
	def header_text(self):
		...
	def ClearDiskCache(self, start: int, end: int) -> bool:
		"""
		Clears frames from the disk cache

		Start..End: Frame range to clear from the cache (inclusive)
		"""
		...
	def GetDoD(self, time: int = int(), flags: int = int(), proxy: int = int()) -> dict[Any, Any]:
		"""
		Returns the Domain of Definition at the given time

		Args:
			time:		 The frame to fetch the value for (default is the current time).
			reqflags: Quality flags (default is final quality).
			proxy:		Proxy level (default is no proxy).

		Returns:
			may be nil, or a table containing { left,bottom,right,top } coords.
		"""
		...
	def EnableDiskCache(self, enable: bool = bool(), path: str = str(), lockcache: bool = bool(), lockbranch: bool = bool(), delete: bool = bool(), prerender: bool = bool(), usenetwork: bool = bool()) -> tuple[bool, str]:
		"""
		Controls disk-based caching

		Args:
			Enable:		 Enables or disables the cache
			Path:			 Path to create the cache at
			LockCache:	Preserves the cache despite upstream changes (default false)
			LockBranch: Locks all upstream tools (default false)
			Delete:		 Deletes the cache at <Path> (default false)
			PreRender:	Do a render now to create the cache (default true)
			UseNetwork: Use Network Rendering when PreRendering (default false)
		"""
		...

PlainOutput = _PlainOutput