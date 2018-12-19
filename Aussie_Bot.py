#!/usr/bin/env python
import socket
import ssl
import time

try:
    import BotDefines

    for attribute in ("botnick", "password", "admin"):
        try:
            getattr(BotDefines, attribute)
        except AttributeError:
            raise Exception(
                "Ya haven't defined {} in BotDefines.py!  Go do that cuz!".format(
                    attribute
                )
            )
except ImportError:
    raise Exception(
        "BotDefines.py doesn't exist.  Create one and define the following variables: "
        "botnick, password and admin."
    )

import insult
import timelookup
import weatherdefine

from importlib import reload


# Settings
# IRC
server = "chat.freenode.net"
port = 6697
channel = "##aussies"
botnick = BotDefines.botnick
password = BotDefines.password
admin = BotDefines.admin

# Tail
tail_files = ["love.txt"]

irc_C = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # defines the socket
irc = ssl.wrap_socket(irc_C)

print("Establishing connection to [%s]" % (server))
# Connect
irc.connect((server, port))
irc.setblocking(False)
# irc.send("PASS %s\n" % (password))
irc.send("USER {0} {0} {0} :meLon-Test\n".format(botnick).encode("utf-8"))
irc.send("NICK {}\n".format(botnick).encode("utf-8"))
irc.send(
    "PRIVMSG nickserv :identify {} {}\r\n".format(botnick, password).encode("utf-8")
)
time.sleep(10)
irc.send("JOIN {}\n".format(channel).encode("utf-8"))

while True:
    # TODO: Find out where reload should be imported from.
    reload(timelookup)
    reload(weatherdefine)

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
