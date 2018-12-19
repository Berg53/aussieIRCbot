import socket
import ssl

from settings import NICK, PASSWORD, SERVER, PORT, CHANNEL

from logger import logger



def get_bot():
    logger.info('Establishing connection to [{}]...'.format(SERVER))
    irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc = ssl.wrap_socket(irc_socket)

    irc.connect((SERVER, PORT))
    logger.info('Connected!')
    irc.setblocking(False)
    # irc.send("PASS %s\n" % (password))

    logger.info('Authenticating...')
    irc.send("USER {0} {0} {0} :meLon-Test\n".format(NICK).encode("utf-8"))
    irc.send("NICK {}\n".format(NICK).encode("utf-8"))
    logger.info('Authenticated!')

    # irc.send(
    #     "PRIVMSG nickserv :identify {} {}\r\n".format(botnick, password).encode("utf-8")
    # )
    # time.sleep(10)

    logger.info('Joining channel...')
    irc.send("JOIN {}\n".format(CHANNEL).encode("utf-8"))
    logger.info('Joined!')
    return irc
