###
# Copyright (c) 2017 laaabaseball
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.ircmsgs as ircmsgs
import os

import re

try:
    from supybot.i18n import PluginInternationalization, internationalizeDocstring
except:
    PluginInternationalization, internationalizeDocstring = lambda x:x, lambda x:x

# This will be used to change the name of the class to the folder name
PluginName=os.path.dirname( __file__ ).split(os.sep)[-1]

_ = PluginInternationalization(PluginName)
@internationalizeDocstring
class _Plugin(callbacks.Plugin):
    """Add the help for "@plugin help <Plugin Name>" here
    """
    threaded = True
    def fuck(self, irc, msg, args):
        """
        fuck you ixrs
        """
        channel = msg.args[0]
        irc.sendMsg(ircmsgs.privmsg(channel, 'fuck you ixrs'))
    fuck = wrap(fuck, [])

    def ltbu(self, irc, msg, args):
        """
        LIGHT THAT BABY UP!!!
        """
        channel = msg.args[0]
        irc.sendMsg(ircmsgs.privmsg(channel, 'LIGHT THAT BABY UP!!!!'))
    ltbu = wrap(ltbu, [])

    def rip(self, irc, msg, args):
        """
        rip!!!
        """
        channel = msg.args[0]
        irc.sendMsg(ircmsgs.privmsg(channel, 'RIP NOISOMEONE'))
    rip = wrap(rip, [])

    def trout(self, irc, msg, args):
        """
        trout!!!
        """
        channel = msg.args[0]
        irc.sendMsg(ircmsgs.privmsg(channel, 'MIKE FUCKING TROUT!!!!'))
    trout = wrap(trout, [])

    def buttercup(self, irc, msg, args):
        """
        buttercup!!!
        """
        channel = msg.args[0]
        irc.sendMsg(ircmsgs.privmsg(channel, 'Why do you build me up (build me up) Buttercup, baby Just to let me down (let me down) '))
    buttercup = wrap(buttercup, [])

    def donger(self, irc, msg, args):
        """
        donger!!!
        """
        channel = msg.args[0]
        irc.sendMsg(ircmsgs.privmsg(channel, 'RAISE YOUR DONGERS'))
    donger = wrap(donger, [])

    def stream(self, irc, msg, args):
        """
        stream!!!
        """
        channel = msg.args[0]
        irc.sendMsg(ircmsgs.privmsg(channel, 'http://reddit.com/r/mlbstreams'))
    stream = wrap(stream, [])


_Plugin.__name__=PluginName
Class = _Plugin


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
