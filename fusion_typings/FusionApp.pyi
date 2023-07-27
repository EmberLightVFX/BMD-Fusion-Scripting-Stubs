from ImageCacheManager import ImageCacheManager_


class FusionApp_:

	#---Properties---#
	MouseX: int
	"""
	Read Only
	"""
	MouseY: int
	"""
	Read Only
	"""
	CacheManager: ImageCacheManager_
	"""
	Read Only
	"""

	#---Methods---#
	def header_text(self):
		...
	def info_text(self):
		...
	def PurgeCache(self) -> None:
		...

FusionApp = FusionApp_