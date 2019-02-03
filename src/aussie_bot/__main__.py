import logging
import signal
import ssl
from importlib import reload, import_module

import irc.connection

import aussie_bot.logger
import aussie_bot.settings
from . import AussieBot


# Configure logging.
_LOGGER = logging.getLogger(__name__)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(aussie_bot.logger.FORMATTER)
stream_handler.setLevel(logging.DEBUG)

root_logger = logging.getLogger("")
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(stream_handler)


class IrcHandlerLoadingException(RuntimeError):
    def __init__(self, *args):
        super().__init__(*args)


class IrcBotModuleLoader(object):
    def __init__(self, *modules, irc_bot=None, base_priority=10):
        self._irc_bot = irc_bot
        self.all_modules = modules
        self.loaded_handlers = []
        self.base_priority = base_priority
        self._initialised = False

    @property
    def irc_bot(self):
        return self._irc_bot

    @irc_bot.setter
    def irc_bot(self, irc_bot):
        if self._irc_bot is None:
            self._irc_bot = irc_bot
        else:
            raise IrcHandlerLoadingException("Can only set irc_bot once.")

    def _get_handlers(self, module):
        handlers = getattr(module, "get_handlers", None)

        if handlers is None:
            raise IrcHandlerLoadingException(
                "Not loading %s module as it doesn't have a get_handlers function",
                module.__name__
            )

        # resolve handlers.
        while callable(handlers):
            handlers = handlers()

        if not hasattr(handlers, "__iter__"):
            raise IrcHandlerLoadingException(
                "Not loading %s module as its get_handlers function isn't iterable",
                module.__name__
            )

        return handlers

    def _load_modules(self, reload_module=False):
        if self.irc_bot is None:
            raise IrcHandlerLoadingException(
                "cannot load modules as irc_bot has not been set."
            )

        priority = self.base_priority

        for module_name in self.all_modules:
            module = import_module(module_name)

            if reload_module:
                module = reload(module)

            try:
                handlers = self._get_handlers(module)

                for event_name, handler_function in handlers:
                    self.irc_bot.reactor.add_global_handler(
                        event_name,
                        handler_function
                    )
                    self.loaded_handlers.append((event_name, handler_function))
                    priority += 1
            except IrcHandlerLoadingException as e:
                _LOGGER.warning(*e.args)

    def _remove_module_handlers(self):
        while len(self.loaded_handlers) > 0:
            self.irc_bot.reactor.remove_global_handler(*self.loaded_handlers.pop())

    def init_modules(self):
        self._load_modules()
        self._initialised = True

    def reload_modules(self):
        if self._initialised:
            self._remove_module_handlers()

        self._load_modules(reload_module=self._initialised)
        self._initialised = True


# Configure bot module loader.
bot_module_loader = IrcBotModuleLoader(
    *aussie_bot.settings.INSTALLED_MODULES
)


def signal_handler(signum, frame):
    if signum == signal.SIGHUP:
        _LOGGER.info("SIGHUP received.  Reloading settings and bot modules.")
        reload(aussie_bot.settings)
        bot_module_loader.reload_modules()


# Configure bot.
connect_params = {}

if aussie_bot.settings.SSL:
    connect_params["connect_factory"] = irc.connection.Factory(
        wrapper=ssl.wrap_socket
    )

bot = AussieBot(
    server=aussie_bot.settings.SERVER,
    port=aussie_bot.settings.PORT,
    password=aussie_bot.settings.PASSWORD,
    channels=aussie_bot.settings.CHANNELS,
    nickname=aussie_bot.settings.NICK,
    **connect_params
)

# Configure bot module loaders with bot and load modules.
bot_module_loader.irc_bot = bot
bot_module_loader.init_modules()

# Register signal callbacks.
signal.signal(signal.SIGHUP, signal_handler)

# Start bot.
try:
    bot.start()
except KeyboardInterrupt:
    pass
