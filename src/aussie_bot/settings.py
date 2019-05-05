# Bot
NICK = "kill_Bot"
PASSWORD = "butts"

# Network
SERVER = "chat.freenode.net"
PORT = 6697
SSL = True
CHANNELS = ('##aussies',)
# Log
LOG_LOCATION='/logs/'
LOG_LOCATION="aussiebot_log.txt"

# Modules / plugins.
INSTALLED_MODULES = (
    "aussie_bot.modules.throttletimer",
    "aussie_bot.modules.insult",
    "aussie_bot.modules.news_feed",
    "aussie_bot.modules.time",
    "aussie_bot.modules.weather",
    "aussie_bot.modules.web_title",
    "aussie_bot.modules.greeter",
    "aussie_bot.modules.rules",
    "aussie_bot.modules.quote_find_save",
    "aussie_bot.modules.logging_module",
)
