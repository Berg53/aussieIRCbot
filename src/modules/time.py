from datetime import datetime

import pytz

from module import ModuleBaseClass

OUTPUT_FORMAT = '{}: {}'
DATE_FORMAT = '%l:%M%p %Z (%z) %b %d, %Y'
ERROR_NOT_FOUND = "Timezone not found: '{}'"

CITY_LOOKUP = {x.split('/')[-1].upper(): x for x in pytz.all_timezones}


class Time(ModuleBaseClass):
    invocation = 't'

    def run(self, message, *args, **kwags):
        self.log.msg('Running Time module with arguments: ')
        self.log.msg(message)
        location = message.strip()
        timezone = CITY_LOOKUP.get(location.upper())
        if not timezone:
            self.errors.append(ERROR_NOT_FOUND.format(location))
            # raise Exception(self.errors)
        else:
            time = datetime.now(pytz.timezone(timezone))
            self.success = self._format_time(timezone, time)
            return self.success

    def _format_time(self, timezone, time):
        formatted_time = datetime.strftime(time, DATE_FORMAT)
        return OUTPUT_FORMAT.format(timezone, formatted_time)

module = Time
