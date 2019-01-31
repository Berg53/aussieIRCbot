""" Run irc bot logic and connection """
import irc.bot

from aussie_bot.logger import LOGGER


class AussieBot(irc.bot.SingleServerIRCBot):
    def __init__(
        self,
        server,
        port,
        channels,
        nickname,
        realname=None,
        password=None,
        reconnection_interval=irc.bot.missing,
        recon=irc.bot.ExponentialBackoff(),
        **connect_params
    ):
        if not realname:
            realname = nickname

        super().__init__(
            server_list=[tuple(x for x in (server, port, password) if x)],
            nickname=nickname,
            realname=realname,
            reconnection_interval=reconnection_interval,
            recon=recon,
            **connect_params
        )

        self.server = server
        self.port = port
        self.initial_channels = channels

        # TODO: Implement throttling.

    def on_nicknameinuse(self, connection, event):
        connection.nick("{}_".format(connection.get_nickname()))

    def on_welcome(self, connection, event):
        for channel in self.initial_channels:
            # TODO: May need to ensure a pause is done before each join command
            # otherwise the IRC Server may drop connection due to flooding.
            connection.join(channel)
