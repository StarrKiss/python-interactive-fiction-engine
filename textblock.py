class Section:
	text = ""
	commands = []
	def __init__(self, text, commandArray):
		self.text = text
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


