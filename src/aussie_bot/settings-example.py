# Bot
NICK = "MeatLoaf"
PASSWORD = "butts"

# Network
SERVER = "chat.freenode.net"
PORT = 6697
SSL = True
CHANNELS = ("##aussies",)

# Log
LOG_LOCATION="aussiebot_log.txt"

# Modules / plugins.
INSTALLED_MODULES = (
    "aussie_bot.modules.insult",
    "aussie_bot.modules.news_feed",
    "aussie_bot.modules.time",
    "aussie_bot.modules.weather",
    "aussie_bot.modules.web_title",
    "aussie_bot.modules.greeter",
)
