from ImageCacheManager import _ImageCacheManager


class _FusionApp:

	#---Properties---#
	MouseX: int
	"""
	Read Only
	"""
	MouseY: int
	"""
	Read Only
	"""
	CacheManager: _ImageCacheManager
	"""
	Read Only
	"""

	#---Methods---#
	def info_text(self):
		...
	def PurgeCache(self) -> None:
		...
	def header_text(self):
		...

FusionApp = _FusionApp