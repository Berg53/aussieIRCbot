#!/usr/bin/env python

import time
from importlib import reload

from settings import INSTALLED_MODULES

from connection import get_bot


irc_connection = get_bot()


# Connect
while True:
    # Reload modules:
    # TODO: Find out where reload should be imported from.
    # for module in INSTALLED_MODULES:
        # reload(module)

    try:
        text = irc_connection.recv(2040)
        log.info(text)
    except Exception as e:
        logging.error(e)
        continue
        # user = text.split(b"!")
        # user = user[0].strip(b":")

#         if text.find(b"my place") != -1:
#             print(user)
#             irc.send(
#                 "PRIVMSG {} :{}\r\n".format(
#                     channel, weatherdefine.weather(user, text)
#                 ).encode("utf-8")
#             )
#
#         if text.find(b"!t") != -1:
#             city = text.split(b"!t ")
#             city = city[1]
#             print(city)
#             irc.send(
#                 "PRIVMSG {} :{}\r\n".format(
#                     channel, timelookup.get_localized_time(city)
#                 ).encode("utf-8")
#             )
#
#         if text.find(b"insult") != -1:
#             irc.send(
#                 "PRIVMSG {} :{}\r\n".format(channel, insult.random_line()).encode(
#                     "utf-8"
#                 )
#             )
#
#         if text.find(b"random") != -1:
#             irc.send(
#                 "PRIVMSG {} :{}\r\n".format(channel, insult.random_text()).encode(
#                     "utf-8"
#                 )
#             )
#
#         """if text.find(":hi") !=-1:
#             user = text.split("!")
#             user = user[0].strip(":")
#             print user
#             irc.send("PRIVMSG "+ channel +" :Hello!\r\n")"""
#
#         # Prevent Timeout
#         if text.find(b"PING") != -1:
#             irc.send("PONG {}\r\n".format(text.split()[1]).encode("utf-8"))
#             print("PONG")
