from typing import Literal

class _ScriptServer:

	#---Methods---#
	def FindHost(self):
		...
	def NotifyHosts(self):
		...
	def Connect(self):
		...
	def AddHost(self):
		...
	def header_text(self):
		...
	def StartHost(self):
		...
	def GetHostList(self):
		...
	def RemoveHost(self):
		...

ScriptServer = _ScriptServer