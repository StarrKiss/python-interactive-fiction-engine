
class Section:
	text = ""
	commands = []
	def __init__(self, text, commandArray):
		self.text = open(text, 'r').read()
		self.commands = commandArray
	def call(self):
		print(self.text)
		print("These are your options: ")
		for x in self.commands:
			print(x.commandText)
		tempInput = input("Enter your command: ")
		print("You Chose " + tempInput)
		for x in self.commands:
			if tempInput == x.commandText:
				x.callNextSec()
				break


class Command:
    
	obj = Section('assets/nulltest', [])

	commandText = ""

	def __init__(self, nextSection, titleText):
		store = Store()
		self.obj = store.getItem(nextSection)
		self.commandText = titleText

	def callNextSec(self):
		self.obj.call()

class Store:


	
	text1 = Section('assets/text1', [Command('text2', "West")])
	text5 = Section('assets/text5', [])
	text2 = Section('assets/text2', [Command('text5', "Investigate"), Command('text1', "Go Back")])

	def getItem(self, item):
		return self.__dict__.get(item)
