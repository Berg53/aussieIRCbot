'''docstring connectiong to irc'''
import socket
import ssl
from settings import NICK, PASSWORD, SERVER, PORT, CHANNEL
from logger import logger


def get_bot():
    '''set up bot for irc connection'''
    logger.info("Establishing connection to [%s]...", SERVER)
    irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc = ssl.wrap_socket(irc_socket)

    irc.connect((SERVER, PORT))
    logger.info("Connected!")
    irc.setblocking(True)
    # irc.send("PASS %s\n" % (password))

    logger.info("Authenticating...")
    irc.send("USER {0} {0} {0} :meLon-Test\n".format(NICK).encode("utf-8"))
    irc.send("NICK {}\n".format(NICK).encode("utf-8"))
    logger.info("Authenticated!")

    irc.send("PRIVMSG nickserv :identify {}\r\n".format(
        PASSWORD).encode("utf-8"))
    # time.sleep(10)
    # irc.send("PASS %s\n" % (password))
    logger.info("Joining channel...")
    irc.send("JOIN {}\n".format(CHANNEL).encode("utf-8"))
    logger.info("Joined!")
    return irc
