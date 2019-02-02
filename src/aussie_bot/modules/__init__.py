import abc
from typing import Sequence, Tuple, Callable, NewType

from irc.client import ServerConnection, Event

from aussie_bot.throttling import Throttle, DefaultThrottle

IrcHandlerCallback = NewType(
    "IrcHandlerCallback", Callable[[ServerConnection, Event], None]
)


class IrcHandler(object):
    def __init__(self, throttle: Throttle = None):
        if throttle is None:
            throttle = DefaultThrottle()

        self._throttle = throttle

    def __call__(self, *args, **kwargs) -> Sequence[Tuple[str, IrcHandlerCallback]]:
        return self.get_handlers()

    @property
    def throttle(self) -> Throttle:
        return self._throttle

    @abc.abstractmethod
    def get_handlers(self) -> Sequence[Tuple[str, IrcHandlerCallback]]:
        raise NotImplementedError()
