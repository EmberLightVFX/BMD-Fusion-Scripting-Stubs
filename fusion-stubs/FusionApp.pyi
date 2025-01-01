from ImageCacheManager import ImageCacheManager


class FusionApp:

	#---Properties---#
	CacheManager: ImageCacheManager
	"""
	Read Only
	"""

	MouseX: int
	"""
	Read Only
	"""

	MouseY: int
	"""
	Read Only
	"""


	#---Methods---#
	def PurgeCache(self) -> None:
		...

