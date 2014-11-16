from iobot.plugins import TextPlugin
from iobot.plugins.decorators import plugin_command
from datetime import datetime
import requests

class BTC(TextPlugin):

    @plugin_command
    def btc_price(self, irc):
	try:
	   symbol = irc.command_args.split()[0]
	   if symbol == None:
	      raise
	except:
	   symbol = 'USD'

	url = 'https://blockchain.info/ticker'
	r = requests.get(url)
	response = r.json()
	for line in response:
	    if line == symbol:
	 	irc.say("The 15 Minute Average for BTC is %s %s" % (response[line]['15m'], symbol)) 
     
Plugin = BTC
