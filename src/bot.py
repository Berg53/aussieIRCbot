from collections import deque
from datetime import datetime

from twisted.python import log
from twisted.internet import defer

import config as c
from module import setup_modules


class Bot:
    def __init__(self):
        self.messages = deque(maxlen=c.SCROLLBACK_SIZE)
        self.module_dispatch = setup_modules()

    def handle_message(self, sender, channel, message):
        saved_message = Message(sender=sender, text=message)
        if not saved_message.text.startswith(c.COMMAND_CHARACTER):
            self.messages.appendleft(saved_message)
            return

        # Command dispatch:
        command, *message_text = saved_message.text.lstrip('!').partition(' ')
        log.msg('Command sent: {}'.format(command))
        module = self.module_dispatch.get(command)
        if not module:
            return

        # Wrap in Deferred avoid blocking:
        return defer.maybeDeferred(
            module.execute,
            self,
            ' '.join(message_text)
        )


class Message:
    def __init__(self, sender, text):
        self.sender = self._get_message_nick(sender)
        self.text = text.strip()
        self.time = datetime.now()
        log.msg('Message in queue: <{}>: {}'.format(self.sender, self.text))

    def _get_message_nick(self, user):
        return user.split('!')[0]

    def __contains__(self, substring):
        log.msg('Quote search query: {}'.format(substring))
        return substring in self.text

    def __repr__(self):
        return 'Message: '.format(self.text)
