import textblock

from textblock import Section


class Command:
	obj = Section("Null", [])

	commandText = ""

	def __init__(self, nextSection, titleText):
		self.obj = nextSection
		self.commandText = titleText

	def callNextSec(self):
		self.obj.call()