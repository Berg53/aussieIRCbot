import logging
import re
from typing import Sequence, Tuple, Pattern

from irc.client import ServerConnection, Event

from aussie_bot.throttling import Throttle
from . import IrcHandler


_LOGGER = logging.getLogger(__name__)


class Greeter(IrcHandler):
    RESPONSES = (
        (re.compile(r"^\.?o/"), r"\o"),
        (re.compile(r"^(\\o\.?|hi |hello|bonjour|salut|snott)"), "o/"),
    )

    def __init__(
        self, responses: Sequence[Tuple[Pattern, str]] = None, throttle: Throttle = None
    ):
        super().__init__(throttle)

        if responses is None:
            responses = self.RESPONSES

        self.responses = responses

    def handler(self, connection: ServerConnection, event: Event):
        if event.arguments:
            occurrence_key = connection.server, event.target
            if not self.throttle.is_throttled(*occurrence_key):
                for pattern, response in self.responses:
                    if pattern.match(event.arguments[0]):
                        if not self.throttle.occurrence(*occurrence_key):
                            if event.type == "privmsg":
                                target = event.source.nick
                            else:
                                target = event.target
                            connection.privmsg(target, response)
                        break

    def get_handlers(self):
        return (("pubmsg", self.handler), ("privmsg", self.handler))


get_handlers = Greeter()
