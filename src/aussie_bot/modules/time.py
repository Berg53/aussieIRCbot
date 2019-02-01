"""Find the time zone to compare with city var"""
import logging
from datetime import datetime

import pytz


_LOGGER = logging.getLogger(__name__)
TIMEZONE_LIST = pytz.all_timezones


def get_localized_time(word):
    """retrieve the time zone for city"""
    word = word.lower().strip()
    if not word:
        return "Timezone blank"

    for timezone in TIMEZONE_LIST:
        split_timezone = timezone.split("/")[1] if "/" in timezone else timezone

        if word not in split_timezone.lower().replace("_", " "):
            continue

        timezone = timezone.replace('"', "").strip(", \n\r")
        time = datetime.now(pytz.timezone(timezone))

        formatted_string = "{timezone}:{time}".format(
            timezone=timezone, time=time.strftime("%l:%M%p %Z (%z) %b %d, %Y")
        )

        return formatted_string.replace("_", " ")

    return (
        " {} is not a timezone on list. Use a listed time zone from link in "
        "topic.".format(word)
    )


def handler(connection, event):
    if event.arguments and event.arguments[0].startswith("!t"):
        args = event.arguments[0].split()

        if len(args) > 1:
            connection.privmsg(event.target, get_localized_time(args[1]))


def get_handlers():
    return (("pubmsg", handler),)
