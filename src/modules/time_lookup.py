from datetime import datetime

import pytz

timezone_list = pytz.all_timezones


def get_localized_time(word):
    word = word.lower().strip()
    if not word:
        return "Timezone blank"

    for timezone in timezone_list:
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
