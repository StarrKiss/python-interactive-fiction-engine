import textblock

from textblock import Section

from store import Store


class Command:
	obj = Section('assets/nulltest', [])

	commandText = ""

	def __init__(self, nextSection, titleText):
		store = Store()
		self.obj = store.getItem(nextSection)
		self.commandText = titleText

	def callNextSec(self):
		self.obj.call()