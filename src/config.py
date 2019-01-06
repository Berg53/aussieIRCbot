import os

# IRC Network
IRC_HOST = os.getenv('IRC_BOT_HOST', 'irc.freenode.net')
IRC_PORT = os.getenv('IRC_BOT_PORT', 6667)

# Bot:
NICK = os.getenv('IRC_BOT_NICK', 'irc_bot')
CHANNEL = os.getenv('IRC_BOT_CHANNEL', '##BotTesting')

# Log file name and location:
LOG_FILE_NAME = os.getenv('IRC_BOT_LOG_FILE_NAME', '{}.log'.format(NICK))
LOG_FILE_LOCATION = os.getenv('IRC_BOT_LOG_FILE_LOCATION', '.')

# How many lines of scrollback to retain:
SCROLLBACK_SIZE = os.getenv('IRC_BOT_SCROLLBACK_SIZE', 1000)

# Character to invoke bot's commands:
COMMAND_CHARACTER = os.getenv('IRC_BOT_COMMAND_CHARACTER', '!')

# Message sent on join (set to None if not desired):
JOIN_MESSAGE = os.getenv('IRC_BOT_JOIN_MESSAGE', 'Hi! I am {}'.format(NICK))

# Modules:
MODULE_LOCATION = 'modules'
INSTALLED_MODULES = (
    'weather',
    'quote',
    'time'
)

# Module settings:

# Quotes:

# Relative path to file for storing quotes:
QUOTE_FILE_LOCATION = os.getenv('IRC_BOT_QUOTE_FILE_LOCATION', 'quotes.txt')

# String format for quotes:
QUOTE_FORMAT = os.getenv(
        'IRC_BOT_QUOTE_FORMAT', '{} - <{}>: {}\n')  # time, nick, message

# Message to show if the search string isn't present in scrollback:
QUOTE_NOT_FOUND_MESSAGE = os.getenv(
        'IRC_BOT_QUOTE_NOT_FOUND_MESSAGE', '[Quote not found]')

# Message to show if quote save failed:
QUOTE_SAVE_FAILED = os.getenv(
        'IRC_BOT_QUOTE_SAVE_FAILED', 'Could not save quote')
