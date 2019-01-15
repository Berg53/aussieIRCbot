'''docstring connectiong to irc'''
import socket
import ssl
from settings import NICK, PASSWORD, SERVER, PORT, CHANNEL
from logger import LOGGER


def get_bot():
    '''set up bot for irc connection'''
    LOGGER.info("Establishing connection to [%s]...", SERVER)
    irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc = ssl.wrap_socket(irc_socket)

    irc.connect((SERVER, PORT))
    LOGGER.info("Connected!")
    irc.setblocking(True)
    # irc.send("PASS %s\n" % (password))

    LOGGER.info("Authenticating...")
    irc.send("USER {0} {0} {0} :meLon-Test\n".format(NICK).encode("utf-8"))
    irc.send("NICK {}\n".format(NICK).encode("utf-8"))
    LOGGER.info("Authenticated!")

    irc.send("PRIVMSG nickserv :identify {}\r\n".format(
        PASSWORD).encode("utf-8"))
    # time.sleep(10)
    # irc.send("PASS %s\n" % (password))
    LOGGER.info("Joining channel...")
    irc.send("JOIN {}\n".format(CHANNEL).encode("utf-8"))
    LOGGER.info("Joined!")
    return irc
