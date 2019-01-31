import logging
import ssl
from importlib import reload, import_module

import irc.connection

import aussie_bot.logger
from . import AussieBot
from .settings import SERVER, PORT, PASSWORD, NICK, CHANNELS, SSL, INSTALLED_MODULES


_LOGGER = logging.getLogger(__name__)


def init_modules(irc_bot, *modules, base_priority=10):
    priority = base_priority
    for module_name in modules:
        module = import_module(module_name)
        handlers = getattr(module, "get_handlers", None)

        if handlers is None:
            _LOGGER.warning(
                "Not loading %s module as it doesn't have a get_handlers function",
                module_name,
            )
            continue

        if callable(handlers):
            handlers = handlers()

        if not hasattr(handlers, "__iter__"):
            _LOGGER.warning(
                "Not loading %s module as its get_handlers function isn't iterable",
                module_name,
            )
            continue

        for event_name, handler_function in handlers:
            irc_bot.reactor.add_global_handler(event_name, handler_function)
            priority += 1


try:
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(aussie_bot.logger.FORMATTER)
    stream_handler.setLevel(logging.DEBUG)

    root_logger = logging.getLogger("")
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(stream_handler)

    connect_params = {}

    if SSL:
        connect_params["connect_factory"] = irc.connection.Factory(
            wrapper=ssl.wrap_socket
        )

    bot = AussieBot(
        server=SERVER,
        port=PORT,
        password=PASSWORD,
        channels=CHANNELS,
        nickname=NICK,
        **connect_params
    )

    init_modules(bot, *INSTALLED_MODULES)

    bot.start()
except KeyboardInterrupt:
    pass
