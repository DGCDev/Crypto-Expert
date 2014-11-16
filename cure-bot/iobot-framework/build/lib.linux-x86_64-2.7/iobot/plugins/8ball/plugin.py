from iobot.plugins import TextPlugin
from iobot.plugins.decorators import plugin_command
import random

class Eight_Ball(TextPlugin):


    @plugin_command
    def ask(self, irc):
	choices = ["sure", "yerp", "no", "nope", "I'm not sure" , "Im too tired right now, ask later."]
	response = "%s" % (random.choice(choices))
	print(response)
	irc.say("%s" % response)

Plugin = Eight_Ball
