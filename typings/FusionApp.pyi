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
	def header_text(self):
		...
	def info_text(self):
		...
	def PurgeCache(self) -> None:
		...

FusionApp = _FusionApp