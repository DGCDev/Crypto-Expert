from iobot.plugins import TextPlugin
from iobot.plugins.decorators import plugin_command
from datetime import datetime
import requests

class Explorer(TextPlugin):

    @plugin_command
    def blockcount(self, irc):
	try:
	   symbol = irc.command_args.split()[0].lower()
	   if symbol == None:
	      raise
	except:
	   symbol = 'dgc'

	url = 'http://chainz.cryptoid.info/%s/api.dws?q=getblockcount' % symbol
	r = requests.get(url)
	response = r.content
 	irc.say("%s currently has a block count of %s" % (symbol.upper(), response))
     
    @plugin_command
    def difficulty(self, irc):
        try:
           symbol = irc.command_args.split()[0].lower()
           if symbol == None:
              raise
        except:
           symbol = 'dgc'

        url = 'http://chainz.cryptoid.info/%s/api.dws?q=getdifficulty' % symbol
        r = requests.get(url)
        response = r.content
        irc.say("%s currently has a difficulty of %s" % (symbol.upper(), response))

    @plugin_command
    def nethash(self, irc):
        try:
           symbol = irc.command_args.split()[0].lower()
           if symbol == None:
              raise
        except:
           symbol = 'dgc'

        url = 'http://chainz.cryptoid.info/%s/api.dws?q=netmhashps' % symbol
        r = requests.get(url)
        response = r.content
        irc.say("%s currently has a Network Hashrate of %s MH/s" % (symbol.upper(), response))

    @plugin_command
    def balance(self, irc):
        address = irc.command_args.split()[0]
	symbol  = irc.comamnd_args.split()[1]
        url = 'http://chainz.cryptoid.info/%s/api.dws?q=getbalance&a=%s' % (symbol, address)
        r = requests.get(url)
        response = r.content
        irc.say("%s currently has a balance of %s %s" % (address, response, symbol))


Plugin = Explorer
