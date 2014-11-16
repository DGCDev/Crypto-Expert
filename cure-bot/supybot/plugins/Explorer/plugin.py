###
# Copyright (c) 2014, Ahmed Bodiwala
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import requests 

try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Explorer')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x

class Explorer(callbacks.Plugin):
    """ Chainz CryptoID Explorer Plugin"""
    threaded = True

    def blockcount(self, irc, msg, args, symbol='DGC'):
	""" Fetch BlockCount for a CryptoID Explorer Coin e.g. @blockcount DGC"""
        url = 'http://chainz.cryptoid.info/%s/api.dws?q=getblockcount' % symbol
        r = requests.get(url)
        response = r.content
        irc.reply("%s currently has a block count of %s" % (symbol.upper(), response))
    blockcount = wrap(blockcount, ['text'])

    def difficulty(self, irc, msg, args, symbol='DGC'):
	""" Fetch Difficulty for a CryptoID Explorer Coin e.g. @difficulty DGC"""
        url = 'http://chainz.cryptoid.info/%s/api.dws?q=getdifficulty' % symbol
        r = requests.get(url)
        response = r.content
        irc.reply("%s currently has a difficulty of %s" % (symbol.upper(), response))
    difficulty = wrap(difficulty, ['text'])

    def nethash(self, irc, msg, args, symbol='DGC'):
	""" Fetch NetHash for a CryptoID Explorer Coin e.g. @nethash DGC"""
        url = 'http://chainz.cryptoid.info/%s/api.dws?q=netmhashps' % symbol
        r = requests.get(url)
        response = r.content
        irc.reply("%s currently has a Network Hashrate of %s MH/s" % (symbol.upper(), response))
    nethash = wrap(nethash, ['text'])

    def balance(self, irc, msg, args, symbol, address):
	""" Fetch Balance for a CryptoID Explorer Coin e.g. @balance DGC <address>"""
	if symbol == None:
	   symbol = 'DGC'
        url = 'http://chainz.cryptoid.info/%s/api.dws?q=getbalance&a=%s' % (symbol, address)
        r = requests.get(url)
        response = r.content
        irc.reply("%s currently has a balance of %s %s" % (address, response, symbol))

Class = Explorer


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
