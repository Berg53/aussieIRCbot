#!/usr/bin/env python
import socket
import ssl
import time

from settings import NICK, PASSWORD, SERVER, PORT, CHANNEL, LOG_LOCATION



# import insult
# import timelookup
# import weatherdefine
#
# from importlib import reload
#



irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc = ssl.wrap_socket(irc_socket)

# TODO: Log
print('Establishing connection to [{}]'.format(SERVER))
# Connect
irc.connect((SERVER, PORT))
irc.setblocking(False)
# irc.send("PASS %s\n" % (password))
irc.send("USER {0} {0} {0} :meLon-Test\n".format(NICK).encode("utf-8"))
irc.send("NICK {}\n".format(NICK).encode("utf-8"))
# irc.send(
#     "PRIVMSG nickserv :identify {} {}\r\n".format(botnick, password).encode("utf-8")
# )
# time.sleep(10)
irc.send("JOIN {}\n".format(CHANNEL).encode("utf-8"))

while True:
    print('BUTTS!')
    # TODO: Find out where reload should be imported from.
    # reload(timelookup)
    # reload(weatherdefine)

    try:
        text = irc.recv(2040)
        print(text)
        user = text.split(b"!")
        user = user[0].strip(b":")

        if text.find(b"my place") != -1:
            print(user)
            irc.send(
                "PRIVMSG {} :{}\r\n".format(
                    channel, weatherdefine.weather(user, text)
                ).encode("utf-8")
            )

        if text.find(b"!t") != -1:
            city = text.split(b"!t ")
            city = city[1]
            print(city)
            irc.send(
                "PRIVMSG {} :{}\r\n".format(
                    channel, timelookup.get_localized_time(city)
                ).encode("utf-8")
            )

        if text.find(b"insult") != -1:
            irc.send(
                "PRIVMSG {} :{}\r\n".format(channel, insult.random_line()).encode(
                    "utf-8"
                )
            )

        if text.find(b"random") != -1:
            irc.send(
                "PRIVMSG {} :{}\r\n".format(channel, insult.random_text()).encode(
                    "utf-8"
                )
            )

        """if text.find(":hi") !=-1:
            user = text.split("!")
            user = user[0].strip(":")
            print user
            irc.send("PRIVMSG "+ channel +" :Hello!\r\n")"""

        # Prevent Timeout
        if text.find(b"PING") != -1:
            irc.send("PONG {}\r\n".format(text.split()[1]).encode("utf-8"))
            print("PONG")
    except Exception:
        # TODO: You should probably log here bro!
        continue
