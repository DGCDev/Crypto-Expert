from iobot.plugins import TextPlugin
from iobot.plugins.decorators import plugin_command
from datetime import datetime
import requests

class CryptsyInfo(TextPlugin):

    @plugin_command
    def coin_price(self, irc):
	try:
	   symbol = irc.command_args.split()[0]
	   if symbol == None:
	      raise
	except:
	   symbol = 'LTC/BTC'

	url = 'http://pubapi.cryptsy.com/api.php?method=marketdatav2'
	r = requests.get(url)
	response = r.json()['return']['markets']
	for line in response:
	    if line == symbol:
	 	irc.say("%s last traded for %s %s. It currently has %s %s of volume on Cryptsy" % (response[line]['primarycode'], response[line]['lasttradeprice'], response[line]['secondarycode'], response[line]['volume'], response[line]['primarycode'])) 
     
Plugin = CryptsyInfo

