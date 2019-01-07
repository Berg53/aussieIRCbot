#!/usr/bin/env python

import sys
from importlib import reload, import_module
import re
from connection import get_bot
from logger import logger
from settings import INSTALLED_MODULES, CHANNEL
import random


def main(argv):
    logger.info('Butts')

    irc_connection = get_bot()
    # Connect
    while True:
        # Reload modules:
        for module in INSTALLED_MODULES:
            module = import_module("modules.{}".format(module))
            reload(module)
        try:
            try:

                text = irc_connection.recv(2040).decode("utf-8")
                logger.debug(text)
            except Exception as e:
                logger.error(e)
                continue
            #rejoin channel on kick
            if text.find('KICK ##aussies Canned_Peaches') != -1:
                irc_connection.send("JOIN {}\n".format(CHANNEL).encode("utf-8"))
            #check for private message
            # Prevent Timeout
            print(text)
            if text.find("PING") != -1:
                irc_connection.send("PONG {}\r\n".format(text.split()[1]).encode("utf-8"))
                print("PONG")
            user = text.split("!")
            user = user[0].strip(":")
            if text.find('PRIVMSG Canned_Peaches :') != -1 or text.find('NOTICE Canned_Peaches :') != -1:
                logger.info('did not find channel message this is a private message too bot')
                irc_connection.send(
                        "PRIVMSG {} :{}\r\n".format(user, insult.random_line()).encode(
                            "utf-8"
                        )
                    )
                text=""
            else:
                pass
            chance = random.randint(1,200)
            chance1 = random.randint(1,200)



            
            if "weather" in INSTALLED_MODULES:
                from modules import weather
                if text.find('my place') != -1:
                    words = text.split(":")[2].strip("\r\n")
                    words = words.split()
                    words = words[0] + words[1]
                    if words == "myplace":
                        irc_connection.send(
                            "PRIVMSG {} :{}\r\n".format(
                                CHANNEL, weather.weather(user, text)
                            ).encode("utf-8")
                        )

            if "time" in INSTALLED_MODULES:
                from modules import time
                if text.find("!t") != -1:
                    city = text.split("!t ")
                    city = city[1]
                    irc_connection.send(
                        "PRIVMSG {} :{}\r\n".format(
                            CHANNEL, time.get_localized_time(city)
                        ).encode("utf-8")
                    )

            if "web_title" in INSTALLED_MODULES:
                from modules import web_title
                match = re.search("(?P<url>https?://[^\s]+)", text)
                if match is not None: 
                    irc_connection.send(
                        "PRIVMSG {} :{}\r\n".format(
                            CHANNEL, web_title.gettitle(match.group("url"), user)
                        ).encode("utf-8")
                    )




            if "insult" in INSTALLED_MODULES:
                from modules import insult
                if chance1 <= 1:
                    irc_connection.send(
                        "PRIVMSG {} :{}\r\n".format(CHANNEL, insult.random_line()).encode(
                            "utf-8"
                        )
                    )

                if text.find("!q") != -1:
                    irc_connection.send(
                        "PRIVMSG {} :{}\r\n".format(
                            CHANNEL, insult.random_text()
                        ).encode("utf-8")
                    )
                try:
                    num = text.split()
                    if text.find("!n") != -1:
                        irc_connection.send(
                            "PRIVMSG {} :{}\r\n".format(
                                CHANNEL, insult.newsfeed(num[4], num[5])
                            ).encode("utf-8")
                        )
                except:
                    irc_connection.send(
                       "PRIVMSG {} :{}\r\n".format(
                           CHANNEL, ('User the format !n num num the first is the news item and the second is the newsfeed. !n # #')
                         ).encode("utf-8")
                    )
        except Exception as e:
            logger.error('end of if aussie_bot' , (e))


if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        ...
