import textblock

from textblock import Section

import commands

from commands import Command

class Store:
	text1 = Section('assets/nulltest', [])
	text2 = Section('assets/nulltest', [])
	text5 = Section('assets/nulltest', [])

	def __init__(self):
		self.text1 = Section('assets/text1', [Command('text2', "West")])
		self.text5 = Section('assets/text5', [])
		self.text2 = Section('assets/text2', [Command('text5', "Investigate"), Command('text1', "Go Back")])


	def getItem(self, item):
		return self.text1