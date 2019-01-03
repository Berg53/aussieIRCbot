from datetime import datetime

import pytz

from module import ModuleBaseClass

OUTPUT_FORMAT = '{}: {}'
DATE_FORMAT = '%l:%M%p %Z (%z) %b %d, %Y'
ERROR_NOT_FOUND = 'Timezone not found for {}'

CITY_LOOKUP = {x.split('/')[-1].lower(): x for x in pytz.all_timezones}


class Time(ModuleBaseClass):
    invocation = 't'

    def run(self, message):
        location = message.strip().lower()
        timezone = CITY_LOOKUP.get(location)
        if not timezone:
            self.errors.append(ERROR_NOT_FOUND.format(location))
            return
        self.success = location
        return self

    def _format_time(self, timezone, time):
        formatted_time = datetime.strftime(time, DATE_FORMAT)
        return OUTPUT_FORMAT.format(timezone.capitalize(), formatted_time)
