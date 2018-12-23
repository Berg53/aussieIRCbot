from twisted.internet import protocol
from twisted.python import log
from twisted.words.protocols import irc

import config as c
from bot import Bot


class IRCProtocol(irc.IRCClient):
    nickname = c.NICK

    def signedOn(self):
        self.join(self.factory.channel)
        log.msg('Joined channel: {}'.format(self.factory.channel))
        if c.JOIN_MESSAGE:
            self.msg(user=self.factory.channel, message=c.JOIN_MESSAGE)
            log.msg('Sent JOIN message: {}'.format(c.JOIN_MESSAGE))

    def privmsg(self, user, channel, message):
        return self._message_handler(user, channel, message)

    def kickedFrom(self, channel, kicker, message):
        log.msg('Got kicked by {}'.format(kicker))
        self.signedOn()

    def _message_handler(self, sender, channel, message):
        # Delegate to bot:
        d = self.factory.bot.handle_message(sender, channel, message)
        if d:
            d.addCallbacks(
                self._messageChannelSuccess,
                self._messageChannelFailure
            )

    def _messageChannelSuccess(self, message):
        self.msg(user=self.factory.channel, message=message)

    def _messageChannelFailure(self, failure):
        log.err(failure.getErrorMessage())
        self.msg(
            user=self.factory.channel,
            message='Ruh roh! Check your logs!'
        )


class IRCBotFactory(protocol.ClientFactory):
    protocol = IRCProtocol

    def __init__(self):
        self.channel = c.CHANNEL
        self.bot = Bot()
