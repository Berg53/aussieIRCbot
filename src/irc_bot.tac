from twisted.application import internet, service
from twisted.python.log import ILogObserver, FileLogObserver
from twisted.python.logfile import LogFile

from irc import IRCBotFactory
import config as c

application = service.Application('IRCBot')
logfile = LogFile(c.LOG_FILE_NAME, c.LOG_FILE_LOCATION)
application.setComponent(ILogObserver, FileLogObserver(logfile).emit)

serviceCollection = service.IServiceCollection(application)

internet.TCPClient(
  c.IRC_HOST,
  c.IRC_PORT,
  IRCBotFactory()
).setServiceParent(serviceCollection)
