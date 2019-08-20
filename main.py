import textblock

from textblock import Section

import commands

from commands import Command


text2 = Section('assets/text2', [])

text3 = Section('assets/text3', [])

text4 = Section('assets/text4', [])



command1 = Command(text2, "West")

command2 = Command(text3, "East")

command3 = Command(text4, "North")





text1 = Section('assets/text1', [command1, command3, command2])


text1.call()

#text1.call()




