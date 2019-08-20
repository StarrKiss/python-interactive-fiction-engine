import textblock

from textblock import Section

import commands

from commands import Command


text2 = Section("Testing1", [])

text3 = Section("Testing1", [])

text4 = Section("TestingAgain", [])



command1 = Command(text2, "West")

command2 = Command(text2, "East")

command3 = Command(text3, "North")





text1 = Section("You arrive at a fork. There are three directions you can go, marked clearly.", [command1, command3, command2])


text1.call()

#text1.call()




