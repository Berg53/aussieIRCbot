""" Run irc bot logic and connection """
from typing import Sequence, Optional
from irc.bot import SingleServerIRCBot, ExponentialBackoff, ReconnectStrategy
from irc.client import ServerConnection, Event

from aussie_bot.logger import LOGGER


class AussieBot(SingleServerIRCBot):
    def __init__(
        self,
        server: str,
        port: int,
        channels: Sequence[str],
        nickname: str,
        realname: Optional[str] = None,
        password: Optional[str] = None,
        recon: ReconnectStrategy = ExponentialBackoff(),
        **connect_params
    ):
        if not realname:
            realname = nickname

        super().__init__(
            server_list=[tuple(x for x in (server, port, password) if x)],
            nickname=nickname,
            realname=realname,
            recon=recon,
            **connect_params
        )

        self.server = server
        self.port = port
        self.initial_channels = channels

    def on_nicknameinuse(self, connection: ServerConnection, event: Event):
        connection.nick("{}_".format(connection.get_nickname()))

    def on_welcome(self, connection: ServerConnection, event: Event):
        for channel in self.initial_channels:
            connection.join(channel)

    def on_kick(self, connection: ServerConnection, event: Event):
        if event.arguments and connection.get_nickname() in event.arguments:
            connection.join(event.target)

    def on_invite(self, connection: ServerConnection, event: Event):
        if event.target == connection.get_nickname() and event.arguments:
            if event.arguments[0] not in self.channels:
                connection.join(event.arguments[0])
